"""Console UI helpers for consistent output formatting."""

def _print(prefix: str, message: str) -> None:
    print(f"{prefix} {message}")


def print_cyan(message: str) -> None:
    _print("\033[96m", message)


def print_green(message: str) -> None:
    _print("\033[92m", message)


def print_yellow(message: str) -> None:
    _print("\033[93m", message)


def print_gray(message: str) -> None:
    _print("\033[90m", message)


def print_success(message: str) -> None:
    _print("✅", message)


def print_warning(message: str) -> None:
    _print("⚠️", message)


def print_error(message: str) -> None:
    _print("❌", message)
