"""Utility package for Beats PM Antigravity Kit."""

from .filesystem import (
    ensure_directory,
    ensure_file_directory,
    file_exists,
    directory_exists,
    read_file,
    write_file,
    append_file,
    atomic_write,
    copy_file,
    get_relative_path,
    get_absolute_path,
    get_directory,
)
from .config import (
    get_config,
    get_config_path,
    load_config,
    save_config,
    set_config,
    get_path,
    get_required_directories,
    get_extensions,
    get_tracker_path,
    get_template_path,
    get_root_directory,
)
from .subprocess_helper import (
    run_command,
    run_command_silent,
    check_command_exists,
    run_python_script,
    check_extension_installed,
    install_extension,
)
from .platform import (
    get_system,
    get_python_executable,
    get_npm_executable,
    get_shell_flag,
    get_home_directory,
    get_temp_directory,
)
from .ui import (
    print_cyan,
    print_green,
    print_yellow,
    print_gray,
    print_success,
    print_warning,
    print_error,
)
