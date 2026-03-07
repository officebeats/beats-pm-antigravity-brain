"""Configuration accessors for the Antigravity Brain."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from .ui import print_warning, print_error

_config_cache: Optional[Dict[str, Any]] = None


def get_config_path() -> Path:
    """Get the path to the configuration file."""
    return Path("system/config.json")


def load_config(force: bool = False) -> Dict[str, Any]:
    """Load configuration from disk with caching."""
    global _config_cache
    if _config_cache is not None and not force:
        return _config_cache

    config_path = get_config_path()
    try:
        with config_path.open("r", encoding="utf-8") as f:
            _config_cache = json.load(f)
    except (json.JSONDecodeError, IOError) as exc:
        print_warning(f"Failed to load config file, using defaults: {exc}")
        _config_cache = {}

    return _config_cache


def save_config(config: Dict[str, Any]) -> None:
    """Persist configuration to disk."""
    config_path = get_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def set_config(key: str, value: Any) -> None:
    """Set a nested configuration value (dot notation)."""
    config = load_config()
    parts = key.split(".")
    cursor: Dict[str, Any] = config
    for part in parts[:-1]:
        cursor = cursor.setdefault(part, {})
    cursor[parts[-1]] = value
    save_config(config)


def get_config(key: str, default: Any = None) -> Any:
    """Get a nested configuration value (dot notation)."""
    config = load_config()
    parts = key.split(".")
    cursor: Any = config
    for part in parts:
        if not isinstance(cursor, dict) or part not in cursor:
            return default
        cursor = cursor[part]
    return cursor


def get_root_directory() -> str:
    """Resolve the repo root directory."""
    root = get_config("paths.root")
    if root in (None, "", "."):
        return str(Path.cwd())
    return str(Path(root).resolve())


def get_path(key: str, relative: bool = True) -> str:
    """Get a path from configuration."""
    path = get_config(f"paths.{key}")
    if not path:
        print_error(f"Path not found in config: {key}")
        return ""
    if relative:
        return path
    return str(Path(get_root_directory()) / path)


def get_required_directories() -> list:
    """Return required directory list from config."""
    return get_config("directories.required", [])


def get_extensions() -> list:
    """Return extension list from config."""
    return get_config("extensions", [])


def get_tracker_path(tracker_name: str) -> str:
    """Get configured tracker path."""
    return get_config(f"trackers.{tracker_name}", "")


def get_template_path(template_name: str) -> str:
    """Get configured template path."""
    return get_config(f"templates.{template_name}", "")
