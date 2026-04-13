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
Or hardcode the values below.
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
# Configuration — edit these or set via environment variables
# ---------------------------------------------------------------------------

BASE_URL:    str = os.environ.get("LLM_BASE_URL", "http://localhost:11434/v1")
MODEL:       str = os.environ.get("LLM_MODEL",    "qwen2.5-coder:32b")
API_KEY:     str = os.environ.get("LLM_API_KEY",  os.environ.get("ANTHROPIC_API_KEY", "ollama"))
MAX_TOKENS:  int = 4096
TIMEOUT_SEC: int = 180


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert at writing Python checkers that detect open-source library versions in source trees.

You will receive the contents of files from a third-party component directory.
Your task: write a complete, ready-to-use Python checker class that inherits from BaseChecker.

## BaseChecker API

```python
class BaseChecker:
    VENDOR: str = ""          # NVD vendor, e.g. "zlib", "openssl", "facebook"
    PRODUCT: str = ""         # NVD product name, e.g. "zlib", "openssl", "zstandard"
    LINK_SOURCE: str = ""     # git URL

    CONTAINS_PATTERNS: List[str] = []
    # Regex patterns that CONFIRM this component is present (signature strings).
    # Used as fallback when no version found. Pick distinctive copyright lines
    # or unique error messages — not generic words.

    SOURCE_FILENAME_PATTERNS: List[str] = []
    # Regex patterns for filenames that BELONG to this checker.
    # Use anchored patterns: r"(^|/)zstd\\.h$" or r"(^|/)configure\\.ac$"

    def make_result(self, version: str, source_path: str, extra: dict = None) -> dict:
        ...  # returns a finding dict — always use this, never build dicts manually

    def match_source_filename(self, path: str) -> bool:
        ...  # True if path matches SOURCE_FILENAME_PATTERNS

    def check_file_versions_only(self, content: str, path: str) -> List[dict]:
        # Called for every candidate file during scan.
        # Return [] if path does not match or version not found.

    def check_meta(self, directory: str) -> List[dict]:
        # Called for every directory during scan.
        # Look at CHANGELOG, CMakeLists.txt, configure.ac, etc.
        # Always verify the file mentions this component before extracting version.
```

## Rules

1. CLASS NAME: CamelCase from product name. "openssl" -> OpenSsl, "libjpeg-turbo" -> LibjpegTurbo

2. VENDOR/PRODUCT — use NVD CPE names:
   zlib         -> vendor="zlib"         product="zlib"
   openssl      -> vendor="openssl"      product="openssl"
   libjpeg      -> vendor="ijg"          product="libjpeg"
   libjpeg-turbo-> vendor="libjpeg-turbo" product="libjpeg-turbo"
   libpng       -> vendor="libpng"       product="libpng"
   zstandard    -> vendor="facebook"     product="zstandard"
   curl         -> vendor="haxx"         product="curl"
   sqlite       -> vendor="sqlite"       product="sqlite"

3. SOURCE_FILENAME_PATTERNS: only the most version-authoritative files.
   Prefer version.h, configure.ac, CMakeLists.txt, the main public header.
   Keep the list short — 1-3 patterns max.

4. CONTAINS_PATTERNS: 1-3 distinctive strings as fallback.
   Good: copyright lines with author names, unique function names, project taglines.
   Bad: generic words like "version", "library", "copyright".

5. check_file_versions_only:
   - First check: if not self.match_source_filename(path): return []
   - Use compiled class-level regex attributes named RX_...
   - Return [self.make_result(version, abs_path, extra={"version_source_abs": abs_path})]
   - For components with MAJOR/MINOR/PATCH defines — combine them

6. check_meta (implement when changelog/cmake/configure.ac is the best version source):
   - Always guard: if component name not in content.lower(): return []
   - Read the specific file, extract version, return result

## Output format

Return ONLY valid Python source code. No prose, no markdown fences, no explanation.
Start directly with: # -*- coding: utf-8 -*-
"""


# ---------------------------------------------------------------------------
# HTTP call — stdlib only, no pip installs required
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
# Entry point — stdin mode (kilo code / orchestrator integration)
# ---------------------------------------------------------------------------

def main() -> None:
    prompt = sys.stdin.read()
    if not prompt.strip():
        sys.exit("Error: empty prompt on stdin")
    result = call_llm(prompt)
    sys.stdout.write(result)
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# File collection — used by CLI mode to build the prompt
# ---------------------------------------------------------------------------

_HIGH = {
    "version.h", "version.hpp", "configure.ac", "configure.in",
    "cmakelists.txt", "meson.build", "vcpkg.json",
    "version", "version.txt", "version.in", "package.json",
    "changelog", "changelog.md", "changes", "news",
    "readme", "readme.md", "readme.rst",
}
_MED = {
    "config.h", "config.h.in", "config.h.cmake",
    "makefile", "makefile.am", "makefile.in",
    "build.gradle", "pom.xml", "license", "copying",
}
_CODE_EXTS = {".c", ".cc", ".cxx", ".cpp", ".h", ".hh", ".hpp", ".hxx", ".ipp"}
_META_EXTS = {".ac", ".in", ".cmake", ".mk", ".am", ".m4", ".txt", ".md", ".rst",
              ".json", ".yml", ".yaml"}
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
    if bn in _HIGH:
        return 100
    ext = os.path.splitext(bn)[1]
    if bn in _MED:
        return 60
    if ext in _CODE_EXTS and any(k in bn for k in ("version", "config", "ver")):
        return 80
    if ext in _CODE_EXTS:
        return max(10, 50 - (rel.count("/") + rel.count("\\")) * 5)
    if ext in _META_EXTS:
        return 30
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
    scored.sort(key=lambda x: -x[0])
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


def build_prompt(root: str) -> str:
    """Собрать содержимое файлов компонента в один промпт для LLM."""
    parts = [f"Analyze these source files and write a checker for: {os.path.abspath(root)}\n"]
    for full, rel in _collect(root)[:MAX_FILES]:
        content = _snippet(full)
        if content.strip():
            parts.append(f"=== FILE: {rel} ===\n{content}\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Post-processing — strip fences, validate syntax, fix if broken
# ---------------------------------------------------------------------------

def _strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:python)?\s*\n?", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text.strip()


def validate_and_fix(code: str) -> str:
    code = _strip_fences(code)
    try:
        ast.parse(code)
        return code
    except SyntaxError as e:
        print(f"[WARN] Syntax error, retrying fix: {e}", file=sys.stderr)

    fixed = _strip_fences(call_llm(
        f"Fix the Python syntax error. Return ONLY valid Python, no markdown.\n"
        f"Error: {e}\n\nCode:\n{code}"
    ))
    try:
        ast.parse(fixed)
        print("[INFO] Syntax fixed OK", file=sys.stderr)
        return fixed
    except SyntaxError as e2:
        print(f"[ERROR] Still broken: {e2}", file=sys.stderr)
        return f"# SYNTAX ERROR: {e2}\n# Fix manually\n\n{fixed}"


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
    code = validate_and_fix(call_llm(prompt))

    if out_dir:
        print(f"[OK]   {_save(code, root, out_dir)}", file=sys.stderr)
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
    ap.add_argument("--out",     metavar="DIR")
    ap.add_argument("--batch",   action="store_true")
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
