# -*- coding: utf-8 -*-
"""
checker_writer_agent.py — генератор checker'ов по исходникам компонента.

Usage (как kilo code / оркестратор):
    python main.py --repo /path/to/repo --llm-command "python checker_writer_agent.py"
    Промпт на stdin — plain text, ответ в stdout — plain text.

Usage (прямой запуск):
    python checker_writer_agent.py /path/to/zlib
    python checker_writer_agent.py /path/to/zlib --out ./checkers/
    python checker_writer_agent.py /path/to/zlib --examples ./checkers/
    python checker_writer_agent.py /path/to/third_party/ --batch --out ./checkers/
    python checker_writer_agent.py /path/to/zlib --dry-run

Configuration via environment variables:
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
import urllib.request
import urllib.error
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL:    str = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1")
MODEL:       str = os.environ.get("LLM_MODEL",    "qwen2.5-coder:32b")
API_KEY:     str = os.environ.get("LLM_API_KEY",  os.environ.get("ANTHROPIC_API_KEY", "ollama"))
MAX_TOKENS:  int = 4096
TIMEOUT_SEC: int = 180


# ---------------------------------------------------------------------------
# Few-shot examples — архетипы из реальной кодовой базы
#
# Каждый пример демонстрирует один из 4 паттернов:
#   1. VERSION_PATTERNS only          — Asn1c    (configure.ac + AC_INIT regex)
#   2. custom check_file_versions_only — Jemalloc (ChangeLog, нестандартный источник)
#   3. check_meta с обходом путей     — OpenCV   (version.hpp глубоко в дереве)
#   4. MAJOR+MINOR+PATCH комбинация   — OpenCV   (несколько #define)
# ---------------------------------------------------------------------------

FEW_SHOT_EXAMPLES = '''\
## Examples from the real checker codebase

Study these examples carefully. They show all supported patterns.
Your output must follow the same style exactly.

### Example 1 — VERSION_PATTERNS only (configure.ac + AC_INIT)
Use this pattern when the version is in configure.ac or CMakeLists.txt as a single string.

```python
# -*- coding: utf-8 -*-
from checkers.base_checker import BaseChecker

class Asn1c(BaseChecker):
    VENDOR = "asn1c_project"
    PRODUCT = "asn1c"
    LINK_SOURCE = "https://github.com/vlm/asn1c.git"

    CONTAINS_PATTERNS = [
        r"ASN\\.1\\s+Compiler",
        r"Abstract\\s+Syntax\\s+Notation\\s+1",
    ]

    SOURCE_FILENAME_PATTERNS = [
        r"(^|/)configure\\.ac$",
    ]

    VERSION_PATTERNS = [
        r"AC_INIT\\(\\s*\\[asn1c\\]\\s*,\\s*\\[([^\\]]+)\\]",
    ]
```

### Example 2 — VERSION_PATTERNS only (header #define)
Use this pattern when the version is a single #define string in a header file.

```python
# -*- coding: utf-8 -*-
from checkers.base_checker import BaseChecker

class Mongoose(BaseChecker):
    VENDOR = "cesanta"
    PRODUCT = "mongoose"
    LINK_SOURCE = "https://github.com/cesanta/mongoose.git"

    CONTAINS_PATTERNS = [
        r"Sergey\\s+Lyubka",
    ]

    SOURCE_FILENAME_PATTERNS = [
        r"(^|/)mongoose\\.h$",
        r"(^|/)mg\\.h$",
    ]

    VERSION_PATTERNS = [
        r\'#\\s*define\\s+(?:MONGOOSE_VERSION|MG_VERSION)\\s+"([\\d\\.]+)"\',
    ]
```

### Example 3 — custom check_file_versions_only (ChangeLog, non-standard source)
Use this pattern when the version lives in a non-standard file like ChangeLog.

```python
# -*- coding: utf-8 -*-
import os
import re
from checkers.base_checker import BaseChecker

class Jemalloc(BaseChecker):
    VENDOR = "jemalloc"
    PRODUCT = "jemalloc"
    LINK_SOURCE = "https://github.com/jemalloc/jemalloc.git"

    CONTAINS_PATTERNS = [
        r"jemalloc/internal",
    ]

    SOURCE_FILENAME_PATTERNS = [
        r"(^|/)ChangeLog$",
    ]

    RX_VERSION  = re.compile(r"jemalloc/([0-9]+(?:\\.[0-9]+){1,3})", re.IGNORECASE)
    RX_CHANGELOG = re.compile(r"^\\*\\s*([0-9]+\\.[0-9]+\\.[0-9]+)\\s*\\(", re.MULTILINE)

    def check_file_versions_only(self, content: str, path: str):
        if not self.match_source_filename(path):
            return []
        s = content or ""
        src_abs = os.path.abspath(path)
        m = self.RX_VERSION.search(s)
        if m:
            return [self.make_result(m.group(1), src_abs, extra={"version_source_abs": src_abs})]
        if os.path.basename(path) == "ChangeLog" and "https://github.com/jemalloc" in s:
            m = self.RX_CHANGELOG.search(s)
            if m:
                return [self.make_result(m.group(1), src_abs, extra={"version_source_abs": src_abs})]
        return []
```

### Example 4 — check_meta + MAJOR/MINOR/PATCH combination
Use this pattern when:
  - the version header is nested deep in the source tree, OR
  - the version is split across multiple #define MAJOR / MINOR / PATCH

```python
# -*- coding: utf-8 -*-
import os
import re
from checkers.base_checker import BaseChecker

class OpenCV(BaseChecker):
    VENDOR = "opencv"
    PRODUCT = "opencv"
    LINK_SOURCE = "https://github.com/opencv/opencv.git"

    CONTAINS_PATTERNS = [
        r"This file is part of OpenCV project\\.",
    ]

    RX_MAJOR  = re.compile(r"#define\\s+CV_VERSION_MAJOR\\s+(\\d+)")
    RX_MINOR  = re.compile(r"#define\\s+CV_VERSION_MINOR\\s+(\\d+)")
    RX_REV    = re.compile(r"#define\\s+CV_VERSION_REVISION\\s+(\\d+)")
    RX_STATUS = re.compile(r\'#define\\s+CV_VERSION_STATUS\\s+"([^"]+)"\')

    def _extract_version(self, text: str):
        s = text or ""
        a = self.RX_MAJOR.search(s)
        b = self.RX_MINOR.search(s)
        c = self.RX_REV.search(s)
        if not (a and b and c):
            return None
        ver = f"{a.group(1)}.{b.group(1)}.{c.group(1)}"
        st = self.RX_STATUS.search(s)
        return f"{ver}{st.group(1).strip()}" if st and st.group(1).strip() else ver

    def check_meta(self, directory: str):
        for rel in (
            os.path.join("opencv2", "core", "version.hpp"),
            os.path.join("include", "opencv2", "core", "version.hpp"),
        ):
            full = os.path.join(directory, rel)
            if not os.path.isfile(full):
                continue
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except OSError:
                continue
            ver = self._extract_version(text)
            if not ver:
                continue
            return [self.make_result(ver, full, extra={
                "version_source_abs": full,
                "origin": f"meta:{rel.replace(os.sep, \'/')}",
            })]
        return []
```

---

## Pattern selection guide

Look at the source files provided and choose ONE of:

| Pattern | When to use |
|---------|-------------|
| VERSION_PATTERNS only | Version in configure.ac / CMakeLists.txt / single-line `#define VERSION "x.y.z"` |
| custom check_file_versions_only | Non-standard source: ChangeLog, custom version file, libtool versioning |
| check_meta + MAJOR/MINOR/PATCH | Version split across 3 defines, OR header nested deep in the tree |
| check_meta only | Version is ONLY discoverable by walking the directory tree |

Never mix patterns unnecessarily. If VERSION_PATTERNS works, do not write check_meta.
'''


# ---------------------------------------------------------------------------
# System prompt (hard rules only — examples are in FEW_SHOT_EXAMPLES)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert at writing Python checkers that detect open-source library versions in source trees.

You will receive:
  1. Source files from a third-party component directory
  2. Real examples from the existing checker codebase
  3. HINT lines with VENDOR / PRODUCT / LINK_SOURCE to use verbatim

Your task: write ONE complete, ready-to-use Python checker class.

""" + FEW_SHOT_EXAMPLES + """

## Hard rules

- Return ONLY valid Python source code — no prose, no markdown fences
- Start with exactly: # -*- coding: utf-8 -*-
- Import BaseChecker exactly as: from checkers.base_checker import BaseChecker
- Use str regexes only — never bytes regexes like rb"..."
- In check_file_versions_only(): first line must be `if not self.match_source_filename(path): return []`
- In check_meta(): use os.path.join(), os.path.isfile(), catch OSError, verify ownership
- Use os.path.abspath(path) for version_source_abs
- Use VENDOR / PRODUCT / LINK_SOURCE exactly as given in the HINT
- If VERSION_PATTERNS is sufficient — do NOT write check_file_versions_only or check_meta
"""


# ---------------------------------------------------------------------------
# RAG — поиск похожего checker'а из существующей коллекции
# ---------------------------------------------------------------------------

# Ключевые слова, по которым классифицируем "тип" компонента из исходников
_RAG_SOURCE_SIGNALS = [
    # (regex_to_detect_in_sources,  tag)
    (re.compile(r"AC_INIT\s*\(", re.IGNORECASE),            "configure.ac"),
    (re.compile(r"project\s*\(.*VERSION", re.IGNORECASE),   "cmake_version"),
    (re.compile(r"cmake_minimum_required", re.IGNORECASE),  "cmake"),
    (re.compile(r"#define\s+\w+_VERSION_MAJOR", re.IGNORECASE), "major_minor_patch"),
    (re.compile(r"#define\s+\w+_VERSION\s+\"", re.IGNORECASE),  "define_string"),
    (re.compile(r"ChangeLog|CHANGELOG", re.MULTILINE),       "changelog"),
    (re.compile(r"meson\.build", re.IGNORECASE),             "meson"),
]

_RAG_CHECKER_TAGS: dict[str, list[str]] = {
    # tag -> список паттернов которые ищем в теле checker'а
    "configure.ac":      ["configure.ac", "AC_INIT"],
    "cmake_version":     ["CMakeLists", "cmake", "project("],
    "cmake":             ["CMakeLists", "cmake"],
    "major_minor_patch": ["MAJOR", "MINOR", "PATCH", "REVISION"],
    "define_string":     ["VERSION_STRING", "define.*VERSION.*\""],
    "changelog":         ["ChangeLog", "CHANGELOG"],
    "meson":             ["meson.build", "meson"],
}


def _read_checker_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


def _detect_source_tags(source_context: str) -> list[str]:
    """Определить какие паттерны версионирования встречаются в исходниках."""
    tags = []
    for rx, tag in _RAG_SOURCE_SIGNALS:
        if rx.search(source_context):
            tags.append(tag)
    return tags


def _score_checker_for_tags(checker_code: str, tags: list[str]) -> int:
    """Насколько checker из коллекции соответствует найденным тегам."""
    score = 0
    low = checker_code.lower()
    for tag in tags:
        for kw in _RAG_CHECKER_TAGS.get(tag, []):
            if kw.lower() in low:
                score += 1
    return score


def find_similar_checker(examples_dir: str, source_context: str) -> Optional[str]:
    """
    Найти из папки examples_dir checker наиболее похожий на текущий компонент.
    Возвращает содержимое файла или None.
    """
    if not examples_dir or not os.path.isdir(examples_dir):
        return None

    tags = _detect_source_tags(source_context)
    if not tags:
        return None

    best_score = 0
    best_code  = None

    for fname in os.listdir(examples_dir):
        if not fname.endswith(".py"):
            continue
        fpath = os.path.join(examples_dir, fname)
        code  = _read_checker_file(fpath)
        if not code:
            continue
        score = _score_checker_for_tags(code, tags)
        if score > best_score:
            best_score = score
            best_code  = code

    return best_code if best_score > 0 else None


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
            {"role": "user",   "content": prompt},
        ],
        "temperature": 0.0,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type":  "application/json",
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
# Entry point — stdin mode (kilo code / orchestrator)
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
    "changelog", "changelog.md", "changes", "changes.md",
    "readme", "readme.md", "readme.rst", "license", "copying",
}
_CODE_EXTS = {".c", ".cc", ".cxx", ".cpp", ".h", ".hh", ".hpp", ".hxx", ".ipp"}
_META_EXTS = {".ac", ".in", ".cmake", ".mk", ".am", ".m4",
              ".txt", ".md", ".rst", ".json", ".yml", ".yaml"}
_SKIP = re.compile(
    r"(^|[/\\])(test|tests|testing|doc|docs|example|examples|"
    r"bench|benchmarks|samples|unittests?)([/\\]|$)",
    re.IGNORECASE,
)

MAX_FILES      = 20
MAX_FILE_BYTES = 32_000
MAX_CHARS      = 4_000


def _score(rel: str, bn: str) -> int:
    if _SKIP.search(rel):
        return -1
    if bn in _HIGH:       return 100
    if bn in _MED:        return 60
    if bn in _LOW_META:   return 15
    ext = os.path.splitext(bn)[1]
    if ext in _CODE_EXTS and any(k in bn for k in ("version", "config", "ver")):
        return 80
    if ext in _CODE_EXTS:
        return max(10, 50 - (rel.count("/") + rel.count("\\")) * 5)
    if ext in _META_EXTS: return 20
    return 5


def _collect(root: str) -> List[Tuple[str, str]]:
    scored = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            full = os.path.join(dirpath, fname)
            rel  = os.path.relpath(full, root).replace("\\", "/")
            s    = _score(rel, fname.lower())
            if s >= 0:
                scored.append((s, full, rel))
    scored.sort(key=lambda x: (-x[0], x[2]))
    return [(f, r) for _, f, r in scored]


def _snippet(path: str) -> str:
    try:
        size = os.path.getsize(path)
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            if size > MAX_FILE_BYTES:
                head = fh.read(MAX_CHARS // 2)
                fh.seek(max(0, size - MAX_CHARS // 2))
                return head + "\n...[truncated]...\n" + fh.read(MAX_CHARS // 2)
            return fh.read(MAX_CHARS)
    except Exception:
        return ""


def build_prompt(root: str, hint: str = "", examples_dir: str = "") -> str:
    """
    Собрать промпт для LLM:
      - содержимое файлов компонента
      - HINT с vendor/product/url (если передан)
      - ближайший похожий checker из коллекции (RAG, если examples_dir задан)
    """
    file_parts = []
    for full, rel in _collect(root)[:MAX_FILES]:
        content = _snippet(full)
        if content.strip():
            file_parts.append(f"=== FILE: {rel} ===\n{content}\n")

    source_context = "\n".join(file_parts)

    parts = [f"Write a checker for the component at: {os.path.abspath(root)}\n"]

    # RAG — найти похожий checker и показать его как "closest example"
    if examples_dir:
        similar = find_similar_checker(examples_dir, source_context)
        if similar:
            parts.append(
                "## Closest existing checker from your codebase\n"
                "Use this as your primary style reference for THIS specific component:\n\n"
                "```python\n" + similar + "\n```\n"
            )

    # HINT — vendor/product/url задаётся снаружи, LLM не угадывает
    if hint:
        parts.append(hint)

    parts.append("## Source files\n")
    parts.extend(file_parts)

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Post-processing — strip fences, validate syntax, fix if broken
# ---------------------------------------------------------------------------

def _strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:python)?\s*\n?", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


# Модули которые должны быть импортированы если код их использует
_REQUIRED_IMPORTS = [
    ("os",       re.compile(r"\bos\s*\.\s*\w+|\bos\.path\b")),
    ("re",       re.compile(r"\bre\s*\.\s*(compile|search|match|findall|sub|IGNORECASE|MULTILINE)\b")),
    ("tempfile", re.compile(r"\btempfile\b")),
]

# Строка после которой вставляем недостающие импорты
_CODING_RE    = re.compile(r"^#\s*-\*-\s*coding[^\n]*\n", re.MULTILINE)
_IMPORT_INS_RE = re.compile(r"^(from\s+\S+\s+import\s+\S+|import\s+\S+)", re.MULTILINE)


def _ensure_imports(code: str) -> str:
    """
    Детектирует использование os/re/etc. и добавляет недостающие import-строки.
    Вставляет их сразу после coding-заголовка (или в начало файла).
    """
    missing = []
    for module, usage_rx in _REQUIRED_IMPORTS:
        already = re.search(
            rf"^\s*(import\s+{module}\b|from\s+{module}\s+import\b)",
            code, re.MULTILINE
        )
        if not already and usage_rx.search(code):
            missing.append(f"import {module}")

    if not missing:
        return code

    insert_block = "\n".join(missing) + "\n"
    print(f"[FIX]  adding missing imports: {missing}", file=sys.stderr)

    # Вставить после # -*- coding ... -*-
    m = _CODING_RE.search(code)
    if m:
        pos = m.end()
        return code[:pos] + insert_block + code[pos:]

    # Вставить перед первым import/from
    m = _IMPORT_INS_RE.search(code)
    if m:
        pos = m.start()
        return code[:pos] + insert_block + code[pos:]

    # Fallback — в начало
    return insert_block + code


def validate_and_fix(code: str) -> str:
    code = _strip_fences(code)
    code = _ensure_imports(code)   # ← гарантируем os/re перед парсингом
    try:
        ast.parse(code)
        return code
    except SyntaxError as e:
        print(f"[WARN] Syntax error, fixing: {e}", file=sys.stderr)

    fixed = _strip_fences(call_llm(
        "Fix the Python syntax error. Return ONLY valid Python, no markdown.\n"
        f"Error: {e}\n\nCode:\n{code}"
    ))
    fixed = _ensure_imports(fixed)
    try:
        ast.parse(fixed)
        print("[INFO] Syntax fixed OK", file=sys.stderr)
        return fixed
    except SyntaxError as e2:
        print(f"[ERROR] Still broken: {e2}", file=sys.stderr)
        return f"# SYNTAX ERROR: {e2}\n# Fix manually\n\n{fixed}"


# ---------------------------------------------------------------------------
# CLI helpers
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


def process_one(
    root: str,
    out_dir: Optional[str],
    dry_run: bool,
    verbose: bool,
    hint: str = "",
    examples_dir: str = "",
) -> None:
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

    prompt = build_prompt(root, hint=hint, examples_dir=examples_dir)
    if verbose:
        print(f"[DEBUG] prompt {len(prompt)} chars", file=sys.stderr)

    print("[INFO]   calling LLM...", file=sys.stderr)
    raw  = call_llm(prompt)
    code = validate_and_fix(raw)

    if out_dir:
        print(f"[OK]   {_save(code, root, out_dir)}", file=sys.stderr)
    else:
        sys.stdout.write(code)
        sys.stdout.flush()


def process_batch(
    root: str,
    out_dir: Optional[str],
    dry_run: bool,
    verbose: bool,
    examples_dir: str = "",
) -> None:
    subdirs = sorted(
        e.path for e in os.scandir(root)
        if e.is_dir() and not e.name.startswith(".")
    ) or [root]
    print(f"[BATCH] {len(subdirs)} components", file=sys.stderr)
    ok = err = 0
    for sub in subdirs:
        try:
            process_one(sub, out_dir=out_dir, dry_run=dry_run,
                        verbose=verbose, examples_dir=examples_dir)
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
    ap.add_argument("path",
                    help="Component directory (or root dir with --batch)")
    ap.add_argument("--out",      metavar="DIR",
                    help="Write generated .py files here")
    ap.add_argument("--examples", metavar="DIR",
                    help="Directory with existing checkers for RAG lookup "
                         "(e.g. ./checkers/). Enables automatic similar-example injection.")
    ap.add_argument("--batch",    action="store_true",
                    help="Process each subdirectory separately")
    ap.add_argument("--dry-run",  action="store_true",
                    help="List files without calling LLM")
    ap.add_argument("--verbose",  action="store_true",
                    help="Print debug info")
    args = ap.parse_args()

    if not os.path.isdir(args.path):
        sys.exit(f"[ERROR] not a directory: {args.path}")
    if not args.dry_run and not API_KEY:
        sys.exit("[ERROR] set LLM_API_KEY or ANTHROPIC_API_KEY")

    examples_dir = args.examples or ""

    if args.batch:
        process_batch(args.path, args.out, args.dry_run, args.verbose,
                      examples_dir=examples_dir)
    else:
        process_one(args.path, args.out, args.dry_run, args.verbose,
                    examples_dir=examples_dir)


# ---------------------------------------------------------------------------
# Dispatch: stdin (orchestrator) vs CLI (direct)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.stdin.isatty():
        cli()
    else:
        main()
