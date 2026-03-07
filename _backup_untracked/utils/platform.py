"""Platform helpers for environment detection."""

import platform
import subprocess
import tempfile


def get_system() -> str:
    return platform.system()


def is_windows() -> bool:
    return get_system() == "Windows"


def is_macos() -> bool:
    return get_system() == "Darwin"


def is_linux() -> bool:
    return get_system() == "Linux"


def get_shell_flag() -> bool:
    return is_windows()


def get_python_executable() -> str:
    return "python"


def get_npm_executable() -> str:
    return "npm"


def get_home_directory() -> str:
    import os
    return os.path.expanduser("~")


def get_temp_directory() -> str:
    return tempfile.gettempdir()


def command_exists(command: str) -> bool:
    try:
        subprocess.run(
            [command, "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            shell=get_shell_flag(),
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
