# -*- coding: utf-8 -*-
"""
init_updater.py — атомарно обновляет checkers/__init__.py

Добавляет новый checker:
  1. import-строку в блок imports (sorted, дедупликация)
  2. Имя класса в список ALL_CHECKERS (sorted, дедупликация)

Формат __init__.py который мы поддерживаем:
    from .foo import Foo
    from .bar import Bar
    ...

    ALL_CHECKERS = [
        Foo(),
        Bar(),
    ]

Использование:
    from init_updater import register_checker
    register_checker(
        init_path   = "./checkers/__init__.py",
        module_file = "./checkers/zlib.py",   # или просто имя файла "zlib.py"
        class_name  = "Zlib",                 # если None — угадывается из файла
    )
"""
from __future__ import annotations

import os
import re
import shutil
import tempfile
from typing import Optional


# ---------------------------------------------------------------------------
# Парсинг имени класса из .py файла
# ---------------------------------------------------------------------------

def extract_class_name(py_path: str) -> Optional[str]:
    """Найти первый class Foo(BaseChecker) в файле."""
    try:
        with open(py_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = re.match(r"^class\s+(\w+)\s*\(", line)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return None


def module_name_from_path(py_path: str) -> str:
    """
    'checkers/zlib.py' → 'zlib'
    '/abs/path/checkers/libharu.py' → 'libharu'
    """
    return os.path.splitext(os.path.basename(py_path))[0]


# ---------------------------------------------------------------------------
# Разбор __init__.py на части
# ---------------------------------------------------------------------------

_IMPORT_RE = re.compile(
    r"^from\s+\.(\w+)\s+import\s+(\w+)\s*$"
)

_ALL_CHECKERS_START_RE = re.compile(
    r"^ALL_CHECKERS\s*=\s*\["
)

_ALL_CHECKERS_END_RE = re.compile(r"^\]")

_INSTANCE_RE = re.compile(r"^\s+(\w+)\(\s*\),?\s*$")


def _parse_init(text: str):
    """
    Разобрать __init__.py на три части:
      imports   — list of (module, class_name) из строк "from .foo import Foo"
      instances — list of class_name из строк "    Foo(),"
      pre       — текст до ALL_CHECKERS = [
      post      — текст после закрывающей ]
    """
    lines = text.splitlines(keepends=True)

    imports: list[tuple[str, str]] = []
    instances: list[str] = []

    pre_lines:  list[str] = []
    body_lines: list[str] = []
    post_lines: list[str] = []

    state = "pre"  # pre | body | post

    for line in lines:
        stripped = line.rstrip("\n").rstrip()

        if state == "pre":
            m = _IMPORT_RE.match(stripped)
            if m:
                imports.append((m.group(1), m.group(2)))
                pre_lines.append(line)
                continue

            if _ALL_CHECKERS_START_RE.match(stripped):
                state = "body"
                # не добавляем эту строку — пересоберём сами
                continue

            pre_lines.append(line)

        elif state == "body":
            if _ALL_CHECKERS_END_RE.match(stripped):
                state = "post"
                continue
            m = _INSTANCE_RE.match(line)
            if m:
                instances.append(m.group(1))

        else:  # post
            post_lines.append(line)

    return imports, instances, pre_lines, post_lines


def _render_init(
    imports:   list[tuple[str, str]],
    instances: list[str],
    pre_lines: list[str],
    post_lines: list[str],
) -> str:
    """Собрать __init__.py обратно из частей."""

    # Пересортировать imports по имени модуля (lowercase), сохранить порядок pre_lines
    # pre_lines уже содержит import-строки — пересобираем секцию imports отдельно.

    # Вычислим какие строки в pre_lines — это import-строки
    non_import_pre = [
        ln for ln in pre_lines
        if not _IMPORT_RE.match(ln.rstrip("\n").rstrip())
    ]

    # Отсортировать imports по module
    sorted_imports = sorted(imports, key=lambda x: x[0].lower())
    import_block   = "".join(f"from .{mod} import {cls}\n" for mod, cls in sorted_imports)

    # Отсортировать instances
    sorted_instances = sorted(instances, key=str.lower)
    instances_block  = "".join(f"    {cls}(),\n" for cls in sorted_instances)

    # Собрать
    parts = []
    if non_import_pre:
        parts.append("".join(non_import_pre))
    parts.append(import_block)
    parts.append("\nALL_CHECKERS = [\n")
    parts.append(instances_block)
    parts.append("]\n")
    if post_lines:
        parts.append("".join(post_lines))

    return "".join(parts)


# ---------------------------------------------------------------------------
# Публичный API
# ---------------------------------------------------------------------------

def register_checker(
    init_path:   str,
    module_file: str,
    class_name:  Optional[str] = None,
) -> bool:
    """
    Добавить checker в __init__.py.

    Параметры:
        init_path   — путь к __init__.py
        module_file — путь к .py файлу checker'а (используется для имени модуля)
        class_name  — имя класса; если None — угадывается из module_file

    Возвращает True если файл был изменён, False если запись уже существует.
    Бросает исключение при ошибках чтения/записи.
    """
    init_path   = os.path.abspath(init_path)
    module_file = os.path.abspath(module_file)

    if class_name is None:
        class_name = extract_class_name(module_file)
        if class_name is None:
            raise ValueError(f"Cannot find class name in {module_file}")

    module = module_name_from_path(module_file)

    # Читаем
    try:
        with open(init_path, "r", encoding="utf-8") as f:
            original = f.read()
    except OSError as e:
        raise OSError(f"Cannot read {init_path}: {e}") from e

    imports, instances, pre_lines, post_lines = _parse_init(original)

    # Проверка — уже есть?
    already_imported  = any(cls == class_name for _, cls in imports)
    already_in_list   = class_name in instances

    if already_imported and already_in_list:
        return False  # ничего делать не надо

    # Добавить если нет
    if not already_imported:
        imports.append((module, class_name))
    if not already_in_list:
        instances.append(class_name)

    new_text = _render_init(imports, instances, pre_lines, post_lines)

    # Записать атомарно через временный файл
    init_dir = os.path.dirname(init_path)
    try:
        fd, tmp_path = tempfile.mkstemp(dir=init_dir, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(new_text)
            shutil.move(tmp_path, init_path)
        except Exception:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
    except OSError as e:
        raise OSError(f"Cannot write {init_path}: {e}") from e

    return True


def register_checker_from_saved_file(
    init_path: str,
    checker_py_path: str,
) -> tuple[bool, str]:
    """
    Удобная обёртка: принимает путь к сохранённому .py файлу checker'а,
    определяет имя класса автоматически, регистрирует в __init__.py.

    Возвращает (changed: bool, class_name: str).
    """
    class_name = extract_class_name(checker_py_path)
    if not class_name:
        raise ValueError(f"No BaseChecker subclass found in {checker_py_path}")

    changed = register_checker(
        init_path=init_path,
        module_file=checker_py_path,
        class_name=class_name,
    )
    return changed, class_name
