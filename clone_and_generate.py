# -*- coding: utf-8 -*-
"""
clone_and_generate.py — клонирует репозитории и запускает checker_writer_agent.

Usage:
    python clone_and_generate.py
    python clone_and_generate.py --out ./checkers/ --repos ./repos/
    python clone_and_generate.py --dry-run
    python clone_and_generate.py --only libuv lua mimalloc

LLM config (те же переменные что у checker_writer_agent.py):
    export LLM_BASE_URL="http://localhost:11434/v1"
    export LLM_MODEL="qwen2.5-coder:32b"
    export LLM_API_KEY="ollama"
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from typing import Optional

# init_updater живёт рядом с этим скриптом
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from init_updater import register_checker_from_saved_file


# ---------------------------------------------------------------------------
# Список компонентов — URL известен заранее, агент не угадывает
# ---------------------------------------------------------------------------

@dataclass
class Component:
    url:     str   # git clone URL
    name:    str   # имя директории и идентификатор
    # Подсказки для агента — передаются в промпт отдельной строкой
    vendor:  str = ""   # NVD vendor (если известен)
    product: str = ""   # NVD product (если известен)


COMPONENTS: list[Component] = [
    Component("https://github.com/a4z/libsl3",                         "libsl3",        vendor="a4z",                    product="libsl3"),
    Component("https://github.com/libuv/libuv",                        "libuv",         vendor="libuv",                  product="libuv"),
    Component("https://github.com/lua/lua",                            "lua",           vendor="lua",                    product="lua"),
    Component("https://github.com/microsoft/mimalloc",                 "mimalloc",      vendor="microsoft",              product="mimalloc"),
    Component("https://github.com/TsudaKageyu/minhook",                "minhook",       vendor="tsudakageyu",            product="minhook"),
    Component("https://github.com/hrydgard/minitrace",                 "minitrace",     vendor="hrydgard",               product="minitrace"),
    Component("https://github.com/kraj/musl",                          "musl",          vendor="musl-libc",              product="musl"),
    Component("https://github.com/AcademySoftwareFoundation/openexr",  "openexr",       vendor="openexr",                product="openexr"),
    Component("https://github.com/Totus-Floreo/otris",                 "otris",         vendor="totus-floreo",           product="otris"),
    Component("https://github.com/richgel999/miniz",                   "miniz",         vendor="richgel999",             product="miniz"),
    Component("https://github.com/svaarala/duktape",                   "duktape",       vendor="duktape",                product="duktape"),
    Component("https://github.com/Roboterbastler/hpgl2gcode",          "hpgl2gcode",    vendor="roboterbastler",         product="hpgl2gcode"),
    Component("https://github.com/BYVoid/uchardet",                    "uchardet",      vendor="mozilla",                product="uchardet"),
    Component("https://github.com/LibreDWG/libredwg",                  "libredwg",      vendor="gnu",                   product="libredwg"),
    Component("https://github.com/libharu/libharu",                    "libharu",       vendor="libharu",                product="libharu"),
    Component("https://github.com/admesh/admesh",                      "admesh",        vendor="admesh_project",         product="admesh"),
    Component("https://github.com/easysoftware/xapian-core",           "xapian-core",   vendor="xapian",                 product="xapian-core"),
    Component("https://github.com/GNOME/libxslt",                      "libxslt",       vendor="xmlsoft",                product="libxslt"),
    Component("https://github.com/xkbcommon/libxkbcommon",             "libxkbcommon",  vendor="xkbcommon",              product="libxkbcommon"),
    Component("https://github.com/iplinux/libxcb",                     "libxcb",        vendor="x",                     product="libxcb"),
    Component("https://github.com/xiph/vorbis",                        "vorbis",        vendor="xiph",                  product="libvorbis"),
    Component("https://github.com/andrewrk/libsoundio",                "libsoundio",    vendor="libsound",               product="libsoundio"),
    Component("https://github.com/eidy/libogg",                        "libogg",        vendor="xiph",                  product="libogg"),
    Component("https://github.com/libjpeg-turbo/libjpeg-turbo",        "libjpeg-turbo", vendor="libjpeg-turbo",          product="libjpeg-turbo"),
    Component("https://github.com/alsa-project/alsa-lib",              "alsa-lib",      vendor="alsa-project",           product="alsa-lib"),
    Component("https://github.com/libarchive/libarchive",              "libarchive",    vendor="libarchive",             product="libarchive"),
    Component("https://github.com/kwikius/dxflib",                     "dxflib",        vendor="ribbonsoft",             product="dxflib"),
    Component("https://github.com/mathog/libUEMF",                     "libUEMF",       vendor="mathog",                 product="libuemf"),
    Component("https://github.com/hamonikr/recoll",                    "recoll",        vendor="lesbonscomptes",         product="recoll"),
    # https://github.com/topics/netfiltersdk — страница топика, не репозиторий.
    # Замени на конкретный репозиторий если знаешь какой именно нужен.
    # Component("https://github.com/???/netfilter",  "netfilter", ...),
]


# ---------------------------------------------------------------------------
# Git clone
# ---------------------------------------------------------------------------

def clone(comp: Component, repos_dir: str, depth: int = 1) -> Optional[str]:
    """Клонировать репозиторий. Вернуть путь или None при ошибке."""
    dest = os.path.join(repos_dir, comp.name)

    if os.path.isdir(os.path.join(dest, ".git")):
        print(f"  [SKIP] already cloned: {dest}", flush=True)
        return dest

    print(f"  [GIT]  cloning {comp.url} -> {dest}", flush=True)
    cmd = ["git", "clone", "--depth", str(depth), "--quiet", comp.url, dest]
    try:
        subprocess.run(cmd, check=True, timeout=120,
                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        return dest
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode("utf-8", errors="replace").strip()
        print(f"  [ERROR] clone failed: {err}", flush=True)
        return None
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] clone timed out", flush=True)
        return None


# ---------------------------------------------------------------------------
# Запуск агента
# ---------------------------------------------------------------------------

def _load_agent(agent_script: str):
    """Загрузить модуль checker_writer_agent один раз и закешировать."""
    import importlib.util
    sys.path.insert(0, os.path.dirname(os.path.abspath(agent_script)))
    spec = importlib.util.spec_from_file_location("cwa", agent_script)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_agent_mod = None  # ленивый кеш


def run_agent(
    comp: Component,
    repo_dir: str,
    out_dir: str,
    agent_script: str,
    examples_dir: str = "",
    init_path: str = "",
) -> bool:
    """
    Запустить checker_writer_agent для компонента.
    Vendor/product/url передаются как HINT — LLM не угадывает.
    Если examples_dir задан — агент найдёт похожий checker через RAG.
    Если init_path задан — сразу регистрирует checker в __init__.py.
    """
    global _agent_mod
    if _agent_mod is None:
        _agent_mod = _load_agent(agent_script)
    mod = _agent_mod

    # HINT — точные значения которые LLM должен использовать verbatim
    hint_lines = ["## HINT — use these exact values, do not change them"]
    hint_lines.append(f"LINK_SOURCE = {comp.url!r}")
    if comp.vendor:
        hint_lines.append(f"VENDOR      = {comp.vendor!r}")
    if comp.product:
        hint_lines.append(f"PRODUCT     = {comp.product!r}")
    hint = "\n".join(hint_lines) + "\n"

    prompt = mod.build_prompt(repo_dir, hint=hint, examples_dir=examples_dir)
    print(f"  [LLM]  prompt {len(prompt)} chars, RAG={'yes' if examples_dir else 'no'}",
          flush=True)

    try:
        raw  = mod.call_llm(prompt)
        code = mod.validate_and_fix(raw)
    except Exception as e:
        print(f"  [ERROR] LLM failed: {e}", flush=True)
        return False

    out_path = mod._save(code, repo_dir, out_dir)
    print(f"  [OK]   {out_path}", flush=True)

    # Регистрируем в __init__.py если задан
    if init_path:
        try:
            changed, cls = register_checker_from_saved_file(init_path, out_path)
            if changed:
                print(f"  [INIT] registered {cls} in {init_path}", flush=True)
            else:
                print(f"  [INIT] already registered, skipped", flush=True)
        except Exception as e:
            print(f"  [WARN] __init__.py update failed: {e}", flush=True)

    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Clone repos and generate BaseChecker subclasses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "LLM config via env vars (same as checker_writer_agent.py):\n"
            "  LLM_BASE_URL, LLM_MODEL, LLM_API_KEY\n"
        ),
    )
    ap.add_argument("--repos",  default="./repos",    metavar="DIR",
                    help="Directory to clone repos into (default: ./repos)")
    ap.add_argument("--out",    default="./checkers", metavar="DIR",
                    help="Directory to write generated checkers (default: ./checkers)")
    ap.add_argument("--examples", metavar="DIR", default="",
                    help="Directory with existing checkers for RAG lookup. "
                         "Pass your ./checkers/ to let the agent find similar examples.")
    ap.add_argument("--init",     metavar="FILE", default="",
                    help="Path to checkers/__init__.py — new checkers will be "
                         "registered here automatically after generation.")
    ap.add_argument("--agent",  default=os.path.join(os.path.dirname(__file__),
                                                      "checker_writer_agent.py"),
                    metavar="FILE", help="Path to checker_writer_agent.py")
    ap.add_argument("--depth",  default=1, type=int,
                    help="git clone --depth (default: 1)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Clone repos but don't call LLM")
    ap.add_argument("--only",   nargs="+", metavar="NAME",
                    help="Process only these components by name (e.g. --only libuv lua)")
    ap.add_argument("--skip-clone", action="store_true",
                    help="Skip git clone, use existing repos dir")
    args = ap.parse_args()

    if not os.path.isfile(args.agent):
        sys.exit(f"[ERROR] agent not found: {args.agent}")

    components = COMPONENTS
    if args.only:
        only_set = set(args.only)
        components = [c for c in COMPONENTS if c.name in only_set]
        missing = only_set - {c.name for c in components}
        if missing:
            print(f"[WARN] unknown components: {', '.join(sorted(missing))}", flush=True)

    os.makedirs(args.repos,  exist_ok=True)
    os.makedirs(args.out,    exist_ok=True)

    ok = err = skipped = 0

    for comp in components:
        print(f"\n[{comp.name}]", flush=True)

        # 1. Clone
        if not args.skip_clone:
            repo_dir = clone(comp, args.repos, depth=args.depth)
        else:
            repo_dir = os.path.join(args.repos, comp.name)
            if not os.path.isdir(repo_dir):
                print(f"  [ERROR] not found: {repo_dir}", flush=True)
                err += 1
                continue

        if repo_dir is None:
            err += 1
            continue

        if args.dry_run:
            # Показать какие файлы были бы отправлены
            sys.path.insert(0, os.path.dirname(os.path.abspath(args.agent)))
            import importlib.util
            spec = importlib.util.spec_from_file_location("cwa", args.agent)
            mod  = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            files = mod._collect(repo_dir)
            print(f"  [DRY-RUN] top files:", flush=True)
            for _, rel in files[:mod.MAX_FILES]:
                print(f"    {rel}", flush=True)
            skipped += 1
            continue

        # 2. Generate checker
        success = run_agent(comp, repo_dir, args.out, args.agent,
                            examples_dir=args.examples,
                            init_path=args.init)
        if success:
            ok += 1
        else:
            err += 1

    print(f"\n{'='*50}")
    print(f"Done — ok={ok}  err={err}  skipped={skipped}")
    print(f"Checkers saved to: {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
