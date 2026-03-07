"""Subprocess utilities with Antigravity helpers."""

from __future__ import annotations

import os
import subprocess
import urllib.request
from typing import List, Optional, Sequence, Union

from .platform import get_shell_flag
from .ui import print_cyan, print_green, print_error


Command = Union[str, Sequence[str]]


def run_command(
    command: Command,
    capture_output: bool = False,
    check: bool = False,
    shell: bool = False,
    cwd: Optional[str] = None,
) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        capture_output=capture_output,
        check=check,
        shell=shell,
        cwd=cwd,
    )


def run_command_silent(command: Command, cwd: Optional[str] = None) -> bool:
    try:
        run_command(command, capture_output=True, check=True, cwd=cwd)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False


def check_command_exists(command: str) -> bool:
    try:
        run_command([command, "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False


def run_python_script(path: str) -> bool:
    try:
        run_command(["python", path], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_extension_installed(ext_id: str) -> bool:
    try:
        result = run_command(
            ["antigravity", "--list-extensions"],
            capture_output=True,
            check=True,
        )
        output = result.stdout.decode("utf-8", errors="replace")
        return ext_id in output
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False


def install_extension(ext_id: str, ext_name: str, ext_url: Optional[str] = None) -> bool:
    """Install an Antigravity extension from URL or gallery."""
    try:
        if ext_url:
            filename = "extension.vsix"
            urllib.request.urlretrieve(ext_url, filename)
            print_green(f"  [+] Installing {ext_name}...")
            run_command(
                ["antigravity", "--install-extension", filename],
                capture_output=True,
                check=True,
                shell=get_shell_flag(),
            )
            os.remove(filename)
            print_green(f"  [✓] {ext_name} installed successfully.")
            return True

        print_green(f"  [+] Installing {ext_name}...")
        run_command(
            ["antigravity", "--install-extension", ext_id],
            capture_output=True,
            check=True,
            shell=get_shell_flag(),
        )
        print_green(f"  [✓] {ext_name} installed successfully.")
        return True
    except Exception as exc:
        print_error(f"  [!] Failed to install {ext_name}: {exc}")
        return False
