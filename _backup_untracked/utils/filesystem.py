"""Filesystem helpers with atomic writes for Antigravity."""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Optional, Union

from .ui import print_error


def ensure_directory(path: Union[str, Path]) -> bool:
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except OSError as exc:
        print_error(f"Failed to create directory {path}: {exc}")
        return False


def ensure_file_directory(path: Union[str, Path]) -> bool:
    return ensure_directory(Path(path).parent)


def file_exists(path: Union[str, Path]) -> bool:
    return Path(path).is_file()


def directory_exists(path: Union[str, Path]) -> bool:
    return Path(path).is_dir()


def read_file(path: Union[str, Path], encoding: str = "utf-8") -> Optional[str]:
    try:
        return Path(path).read_text(encoding=encoding)
    except (IOError, UnicodeDecodeError) as exc:
        print_error(f"Failed to read file {path}: {exc}")
        return None


def write_file(path: Union[str, Path], content: str, encoding: str = "utf-8") -> bool:
    try:
        p = Path(path)
        ensure_file_directory(p)
        p.write_text(content, encoding=encoding)
        return True
    except IOError as exc:
        print_error(f"Failed to write file {path}: {exc}")
        return False


def append_file(path: Union[str, Path], content: str, encoding: str = "utf-8") -> bool:
    try:
        with Path(path).open("a", encoding=encoding) as f:
            f.write(content)
        return True
    except IOError as exc:
        print_error(f"Failed to append to file {path}: {exc}")
        return False


def atomic_write(path: Union[str, Path], content: str, encoding: str = "utf-8") -> bool:
    """Write content atomically by writing to a temp file and renaming."""
    try:
        target = Path(path)
        ensure_file_directory(target)
        temp_path = target.with_suffix(target.suffix + ".tmp")
        temp_path.write_text(content, encoding=encoding)
        os.replace(str(temp_path), str(target))
        return True
    except OSError as exc:
        print_error(f"Failed to atomic write {path}: {exc}")
        return False


def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> bool:
    try:
        ensure_file_directory(dst)
        shutil.copy2(str(src), str(dst))
        return True
    except OSError as exc:
        print_error(f"Failed to copy file {src} -> {dst}: {exc}")
        return False


def get_relative_path(path: Union[str, Path], start: Union[str, Path]) -> str:
    p = Path(path)
    s = Path(start)
    try:
        return str(p.relative_to(s))
    except ValueError:
        return str(p)


def get_absolute_path(path: Union[str, Path]) -> str:
    return str(Path(path).resolve())


def get_directory(path: Union[str, Path]) -> str:
    return str(Path(path).parent)
