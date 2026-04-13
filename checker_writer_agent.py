# -*- coding: utf-8 -*-
"""
checker_writer_agent.py — генератор checker'ов по исходникам компонента.

Usage (как kilo code / оркестратор):
    python main.py --repo /path/to/repo --llm-command "python checker_writer_agent.py"

    Промпт на stdin  — plain text, содержимое файлов компонента
    Ответ в stdout   — plain text, готовый Python-код checker'а

Usage (прямой запуск):
    python checker_writer_agent.py /path/to/zlib
    python checker_writer_agent.py /path/to/zlib --out ./checkers/
    python checker_writer_agent.py /path/to/third_party/ --batch --out ./checkers/
    python checker_writer_agent.py /path/to/zlib --dry-run

Configuration via environment variables (recommended):
    export LLM_BASE_URL="http://localhost:11434/v1"
    export LLM_MODEL="qwen2.5-coder:32b"
    export LLM_API_KEY="ollama"
"""

from __future__ import annotations

import ast
import argparse
import json
import os
import re
import sys
import tempfile
import textwrap
import urllib.error
import urllib.request
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL: str = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1")
MODEL: str = os.environ.get("LLM_MODEL", "qwen2.5-coder:32b")
API_KEY: str = os.environ.get("LLM_API_KEY", os.environ.get("ANTHROPIC_API_KEY", "ollama"))
MAX_TOKENS: int = 4096
TIMEOUT_SEC: int = 180

# Сколько раз разрешаем ремонтировать checker после первичной генерации.
MAX_REPAIR_PASSES: int = 2


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert at writing Python checkers that detect open-source library versions in source trees.

You will receive the contents of files from a third-party component directory.
Your task: write a complete, ready-to-use Python checker class that inherits from BaseChecker.

## Hard requirements

- Return ONLY valid Python source code.
- Start with exactly: # -*- coding: utf-8 -*-
- Import BaseChecker exactly as:
  from .base import BaseChecker
- Use Python str regexes only. Never use bytes regexes such as rb"...".
- Use os.path.join(), never manual path concatenation like f"{directory}/file".
- In check_meta():
  - use os.path.isfile(path) before opening any file
  - catch OSError, not only FileNotFoundError
  - return [] on any read/open failure
  - verify the file or directory clearly belongs to this component before extracting version
- Never use generic metadata files (CHANGES, CHANGELOG, README, VERSION.txt) unless:
  - the directory clearly belongs to this component, and
  - the file text explicitly mentions this component
- Never use substring path checks like "configure.ac" in path.
  Use os.path.basename(path).lower() == "configure.ac".
- Never emit a version from a generic plain semver regex alone unless the file is a clearly authoritative version source for this component.
- Prefer configure.ac, CMakeLists.txt, version headers, or the main public header.
- Keep SOURCE_FILENAME_PATTERNS short: 1-3 patterns max.
- Avoid check_meta() entirely if authoritative version extraction already works in check_file_versions_only().

## BaseChecker API

class BaseChecker:
    VENDOR: str = ""
    PRODUCT: str = ""
    LINK_SOURCE: str = ""

    CONTAINS_PATTERNS: List[str] = []
    VERSION_PATTERNS: List[str] = []
    SOURCE_FILENAME_PATTERNS: List[str] = []

    def make_result(self, version: str, source_path: str, extra: dict = None) -> dict:
        ...

    def match_source_filename(self, path: str) -> bool:
        ...

    def check_file_versions_only(self, content: str, path: str) -> List[dict]:
        ...

    def check_meta(self, directory: str) -> List[dict]:
        ...

## Rules

1. CLASS NAME: CamelCase from product name.
   Examples:
   - openssl -> Openssl
   - libjpeg-turbo -> LibjpegTurbo
   - xapian-core -> XapianCore

2. Use exact VENDOR / PRODUCT / LINK_SOURCE values from user hints if provided.

3. SOURCE_FILENAME_PATTERNS:
   - only the most version-authoritative files
   - prefer version.h, configure.ac, CMakeLists.txt, public header
   - keep the list short — 1-3 patterns max
   - use anchored regexes like r"(^|/)configure\\.ac$"

4. CONTAINS_PATTERNS:
   - 1-3 distinctive strings as fallback
   - use strings, not bytes
   - good: unique copyright lines with names, unique taglines, rare identifiers
   - bad: generic words like "version", "library", "copyright"

5. check_file_versions_only:
   - first line must be:
         if not self.match_source_filename(path):
             return []
   - use compiled class-level regex attributes named RX_...
   - use os.path.basename(path).lower() for filename branching
   - return findings only through self.make_result(...)
   - use absolute path:
         abs_path = os.path.abspath(path)
         return [self.make_result(version, abs_path, extra={"version_source_abs": abs_path})]
   - for MAJOR/MINOR/PATCH defines: combine them

6. check_meta:
   - implement it only when really needed
   - if not needed, return []
   - if implemented:
     - use os.path.isfile()
     - use os.path.join()
     - catch OSError
     - verify ownership before opening/using file
     - verify content mentions this component before extracting version

## Output format

Return ONLY valid Python source code.
No prose.
No markdown fences.
Start directly with: # -*- coding: utf-8 -*-
"""


# ---------------------------------------------------------------------------
# HTTP call — stdlib only
# ---------------------------------------------------------------------------

def call_llm(prompt: str) -> str:
    url = BASE_URL.rstrip("/") + "/chat/completions"
    payload = json.dumps({
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.0,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} from {url}: {body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot reach {url}: {e.reason}") from e

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"Unexpected response shape: {data}") from e


# ---------------------------------------------------------------------------
# Entry point — stdin mode
# ---------------------------------------------------------------------------

def main() -> None:
    prompt = sys.stdin.read()
    if not prompt.strip():
        sys.exit("Error: empty prompt on stdin")
    result = call_llm(prompt)
    sys.stdout.write(result)
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

_HIGH = {
    "version.h", "version.hpp", "configure.ac", "configure.in",
    "cmakelists.txt", "meson.build", "vcpkg.json",
    "version", "version.txt", "version.in",
}
_MED = {
    "config.h", "config.h.in", "config.h.cmake",
    "makefile", "makefile.am", "makefile.in",
    "package.json", "build.gradle", "pom.xml",
}
_LOW_META = {
    "changelog", "changelog.md", "changes", "changes.md", "news", "news.md",
    "readme", "readme.md", "readme.rst", "license", "copying",
}
_CODE_EXTS = {".c", ".cc", ".cxx", ".cpp", ".h", ".hh", ".hpp", ".hxx", ".ipp"}
_META_EXTS = {
    ".ac", ".in", ".cmake", ".mk", ".am", ".m4",
    ".txt", ".md", ".rst", ".json", ".yml", ".yaml"
}
_SKIP = re.compile(
    r"(^|[/\\])(test|tests|testing|doc|docs|example|examples|"
    r"bench|benchmarks|samples|unittests?)([/\\]|$)",
    re.IGNORECASE,
)

MAX_FILES = 20
MAX_FILE_BYTES = 32_000
MAX_CHARS = 4_000


def _score(rel: str, bn: str) -> int:
    if _SKIP.search(rel):
        return -1

    if bn in _HIGH:
        return 100
    if bn in _MED:
        return 60
    if bn in _LOW_META:
        return 15

    ext = os.path.splitext(bn)[1]
    if ext in _CODE_EXTS and any(k in bn for k in ("version", "config", "ver")):
        return 80
    if ext in _CODE_EXTS:
        return max(10, 50 - (rel.count("/") + rel.count("\\")) * 5)
    if ext in _META_EXTS:
        return 20
    return 5


def _collect(root: str) -> List[Tuple[str, str]]:
    scored = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, root).replace("\\", "/")
            score = _score(rel, fname.lower())
            if score >= 0:
                scored.append((score, full, rel))
    scored.sort(key=lambda x: (-x[0], x[2]))
    return [(f, r) for _, f, r in scored]


def _snippet(path: str) -> str:
    try:
        size = os.path.getsize(path)
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            if size > MAX_FILE_BYTES:
                head = fh.read(MAX_CHARS // 2)
                fh.seek(max(0, size - MAX_CHARS // 2))
                tail = fh.read(MAX_CHARS // 2)
                return head + "\n...[truncated]...\n" + tail
            return fh.read(MAX_CHARS)
    except Exception:
        return ""


def build_prompt(root: str) -> str:
    """Собрать содержимое файлов компонента в один промпт для LLM."""
    parts = [
        f"Analyze these source files and write a checker for: {os.path.abspath(root)}\n",
        "Runtime requirements:\n"
        "- Import BaseChecker exactly as: from .base import BaseChecker\n"
        "- Use str regexes only, never bytes regexes\n"
        "- Use os.path.join() in check_meta()\n"
        "- check_meta() must use os.path.isfile() before open()\n"
        "- check_meta() must catch OSError\n"
        "- Avoid generic CHANGES/README/VERSION.txt unless clearly necessary\n"
        "- Prefer authoritative version sources such as configure.ac, CMakeLists.txt, version headers\n"
        "- If check_meta() is not necessary, return []\n",
    ]
    for full, rel in _collect(root)[:MAX_FILES]:
        content = _snippet(full)
        if content.strip():
            parts.append(f"=== FILE: {rel} ===\n{content}\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Post-processing — syntax, policy, smoke
# ---------------------------------------------------------------------------

def _strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:python)?\s*\n?", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def _syntax_check(code: str) -> Tuple[bool, str]:
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as e:
        return False, str(e)


def _syntax_fix(code: str, error_text: str) -> str:
    repaired = call_llm(
        "Fix the Python syntax error in this checker.\n"
        "Return ONLY valid Python source code. No markdown.\n\n"
        f"Syntax error:\n{error_text}\n\n"
        f"Code:\n{code}"
    )
    return _strip_fences(repaired)


def validate_checker_policy(code: str) -> List[str]:
    errors: List[str] = []

    if not code.lstrip().startswith("# -*- coding: utf-8 -*-"):
        errors.append("missing utf-8 header at the start of the file")

    allowed_import = re.search(
        r"^\s*from\s+\.base\s+import\s+BaseChecker\s*$",
        code,
        re.MULTILINE,
    )
    if not allowed_import:
        errors.append("BaseChecker must be imported exactly as: from .base import BaseChecker")

    if re.search(r"\brb[\"']", code):
        errors.append("bytes regexes are forbidden; use str regexes")

    if re.search(r"from\s+\.(?:base_checker|basecheck|base_class)\s+import\s+BaseChecker", code):
        errors.append("wrong BaseChecker import path")

    if re.search(r"""f["']\{directory\}[\\/]" """, code):
        errors.append("manual path concatenation with f-string is forbidden; use os.path.join")

    if re.search(r"""directory\s*\+\s*["'][\\/]" """, code):
        errors.append("manual path concatenation is forbidden; use os.path.join")

    if re.search(r"""if\s+["'][^"']+["']\s+in\s+path\s*:""", code):
        errors.append("substring path checks are forbidden; use os.path.basename(path).lower()")

    if "def check_meta(" in code:
        if "os.path.isfile" not in code:
            errors.append("check_meta() must use os.path.isfile() before opening files")
        if "except OSError" not in code:
            errors.append("check_meta() must catch OSError")
        if "os.path.join" not in code:
            errors.append("check_meta() must use os.path.join()")

    return errors


def _repair_quality(code: str, issues: List[str]) -> str:
    prompt = textwrap.dedent(f"""\
        Rewrite this Python checker so it satisfies all requirements.

        Requirements:
        - import BaseChecker exactly as: from .base import BaseChecker
        - use str regexes only, never bytes regexes
        - use os.path.join() in check_meta()
        - use os.path.isfile() before opening any file in check_meta()
        - catch OSError in check_meta()
        - avoid generic metadata files unless ownership is verified
        - never use substring path checks like "configure.ac" in path
        - use os.path.basename(path).lower() for filename branching
        - if check_meta() is unnecessary, implement it as return []

        Detected issues:
        {chr(10).join("- " + x for x in issues)}

        Return ONLY valid Python source code. No markdown.

        Code:
        {code}
    """)
    repaired = call_llm(prompt)
    return _strip_fences(repaired)


def _prepare_code_for_smoke_exec(code: str) -> str:
    code = re.sub(
        r"^\s*from\s+\.(?:base|base_checker|basecheck|base_class)\s+import\s+BaseChecker\s*$",
        "",
        code,
        flags=re.MULTILINE,
    )
    code = re.sub(
        r"^\s*from\s+checkers\.base\s+import\s+BaseChecker\s*$",
        "",
        code,
        flags=re.MULTILINE,
    )

    stub = textwrap.dedent("""\
        import os
        import re
        from typing import Dict, List, Optional, Set

        class BaseChecker:
            CONTAINS_PATTERNS = []
            VERSION_PATTERNS = []
            SOURCE_FILENAME_PATTERNS = []
            VENDOR = ""
            PRODUCT = ""
            LINK_SOURCE = ""

            def __init__(self) -> None:
                self._compiled_source_name_patterns = None

            def _compile_source_name_patterns(self):
                pats = []
                for p in getattr(self, "SOURCE_FILENAME_PATTERNS", []) or []:
                    pats.append(re.compile(p, re.IGNORECASE))
                return pats

            def match_source_filename(self, path: str) -> bool:
                if not getattr(self, "SOURCE_FILENAME_PATTERNS", None):
                    return False
                if self._compiled_source_name_patterns is None:
                    self._compiled_source_name_patterns = self._compile_source_name_patterns()
                norm = (path or "").replace("\\\\", "/")
                for rx in self._compiled_source_name_patterns:
                    if rx.search(norm):
                        return True
                return False

            def make_result(self, version: Optional[str], source_path: str, extra: Optional[Dict] = None) -> Dict:
                out = {
                    "name": self.PRODUCT,
                    "version": (version or "unknown").strip(),
                    "version_source": os.path.abspath(source_path) if source_path else "inline",
                    "vendor": self.VENDOR,
                    "link": self.LINK_SOURCE,
                    "cpe": "",
                }
                if extra:
                    out.update(extra)
                return out
    """)
    return stub + "\n" + code


def smoke_test_checker_code(code: str) -> List[str]:
    """
    Лёгкий runtime-smoke-test без импорта пакета checkers.
    Мы подставляем stub BaseChecker и исполняем код в отдельном namespace.
    """
    errors: List[str] = []
    prepared = _prepare_code_for_smoke_exec(code)
    ns: Dict[str, object] = {}

    try:
        exec( պատրաստված := prepared, ns, ns)  # noqa: S102
    except Exception as e:
        return [f"checker code failed to exec in smoke test: {e}"]

    base_cls = ns.get("BaseChecker")
    checker_cls = None
    for obj in ns.values():
        if isinstance(obj, type) and obj is not base_cls and base_cls is not None:
            try:
                if issubclass(obj, base_cls):
                    checker_cls = obj
                    break
            except TypeError:
                continue

    if checker_cls is None:
        return ["checker class not found in generated code"]

    try:
        checker = checker_cls()
    except Exception as e:
        return [f"checker class failed to instantiate: {e}"]

    try:
        checker.check_file_versions_only("", "dummy.txt")
    except Exception as e:
        errors.append(f"check_file_versions_only crashed on dummy input: {e}")

    with tempfile.TemporaryDirectory() as tmp:
        try:
            checker.check_meta(tmp)
        except Exception as e:
            errors.append(f"check_meta crashed on empty directory: {e}")

        dummy_file = os.path.join(tmp, "dummy.txt")
        try:
            with open(dummy_file, "w", encoding="utf-8") as fh:
                fh.write("dummy")
        except Exception:
            pass

        try:
            checker.check_file_versions_only("dummy", dummy_file)
        except Exception as e:
            errors.append(f"check_file_versions_only crashed on temp file: {e}")

    return errors


def validate_and_fix(code: str) -> str:
    code = _strip_fences(code)

    ok, err_text = _syntax_check(code)
    if not ok:
        print(f"[WARN] Syntax error, retrying fix: {err_text}", file=sys.stderr)
        code = _syntax_fix(code, err_text)
        ok, err_text = _syntax_check(code)
        if not ok:
            print(f"[ERROR] Still broken after syntax fix: {err_text}", file=sys.stderr)
            return f"# SYNTAX ERROR: {err_text}\n# Fix manually\n\n{code}"

    for attempt in range(1, MAX_REPAIR_PASSES + 1):
        policy_errors = validate_checker_policy(code)
        smoke_errors = smoke_test_checker_code(code)

        if not policy_errors and not smoke_errors:
            return code

        issues = policy_errors + smoke_errors
        print(f"[WARN] Checker quality issues (pass {attempt}): {issues}", file=sys.stderr)

        code = _repair_quality(code, issues)
        ok, err_text = _syntax_check(code)
        if not ok:
            print(f"[WARN] Syntax error after quality repair: {err_text}", file=sys.stderr)
            code = _syntax_fix(code, err_text)
            ok, err_text = _syntax_check(code)
            if not ok:
                print(f"[ERROR] Still broken after repair: {err_text}", file=sys.stderr)
                return f"# SYNTAX ERROR: {err_text}\n# Fix manually\n\n{code}"

    final_policy_errors = validate_checker_policy(code)
    final_smoke_errors = smoke_test_checker_code(code)
    if final_policy_errors or final_smoke_errors:
        print(
            f"[WARN] Returning checker with remaining issues: "
            f"{final_policy_errors + final_smoke_errors}",
            file=sys.stderr,
        )

    return code


# ---------------------------------------------------------------------------
# CLI mode helpers
# ---------------------------------------------------------------------------

def _save(code: str, component_dir: str, out_dir: str) -> str:
    m = re.search(r"^class\s+(\w+)\s*\(", code, re.MULTILINE)
    cls = m.group(1) if m else os.path.basename(component_dir).replace("-", "_").title()
    fname = re.sub(r"(?<!^)(?=[A-Z])", "_", cls).lower().lstrip("_") + ".py"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(code)
    return path


def process_one(root: str, out_dir: Optional[str], dry_run: bool, verbose: bool) -> None:
    root = os.path.abspath(root)
    print(f"[INFO] {os.path.basename(root)}", file=sys.stderr)

    files = _collect(root)
    print(f"[INFO]   {len(files)} candidate files", file=sys.stderr)
    if not files:
        print("[WARN]   no files, skipping", file=sys.stderr)
        return

    if dry_run:
        for _, rel in files[:MAX_FILES]:
            print(f"  {rel}", file=sys.stderr)
        return

    prompt = build_prompt(root)
    if verbose:
        print(f"[DEBUG] prompt {len(prompt)} chars", file=sys.stderr)

    print("[INFO]   calling LLM...", file=sys.stderr)
    raw = call_llm(prompt)
    code = validate_and_fix(raw)

    if out_dir:
        saved = _save(code, root, out_dir)
        print(f"[OK]   {saved}", file=sys.stderr)
    else:
        sys.stdout.write(code)
        sys.stdout.flush()


def process_batch(root: str, out_dir: Optional[str], dry_run: bool, verbose: bool) -> None:
    subdirs = sorted(
        e.path for e in os.scandir(root)
        if e.is_dir() and not e.name.startswith(".")
    ) or [root]
    print(f"[BATCH] {len(subdirs)} components", file=sys.stderr)
    ok = err = 0
    for sub in subdirs:
        try:
            process_one(sub, out_dir=out_dir, dry_run=dry_run, verbose=verbose)
            ok += 1
        except Exception as e:
            print(f"[ERROR] {os.path.basename(sub)}: {e}", file=sys.stderr)
            err += 1
    print(f"[BATCH] ok={ok} err={err}", file=sys.stderr)


def cli() -> None:
    ap = argparse.ArgumentParser(
        description="Generate BaseChecker subclasses from component source trees.",
        epilog=(
            "LLM config via env vars:\n"
            "  LLM_BASE_URL  (default: http://localhost:11434/v1)\n"
            "  LLM_MODEL     (default: qwen2.5-coder:32b)\n"
            "  LLM_API_KEY   (default: ollama)\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("path")
    ap.add_argument("--out", metavar="DIR")
    ap.add_argument("--batch", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.path):
        sys.exit(f"[ERROR] not a directory: {args.path}")
    if not args.dry_run and not API_KEY:
        sys.exit("[ERROR] set LLM_API_KEY or ANTHROPIC_API_KEY")

    if args.batch:
        process_batch(args.path, args.out, args.dry_run, args.verbose)
    else:
        process_one(args.path, args.out, args.dry_run, args.verbose)


# ---------------------------------------------------------------------------
# Dispatch: stdin (orchestrator) vs CLI (direct)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.stdin.isatty():
        cli()
    else:
        main()
