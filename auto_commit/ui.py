"""Minimal terminal-style UI for auto-commit assistant."""

import sys
import os
import subprocess
from datetime import datetime
from typing import Optional, Literal
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text
from rich import box

# Initialize console
console = Console()

# Minimal theme colors
THEMES = {
    "hacker": {
        "primary": "bright_green",
        "secondary": "cyan",
        "accent": "bright_yellow",
        "error": "bright_red",
        "success": "bright_green",
        "warning": "bright_yellow",
        "info": "cyan",
    },
    "minimal": {
        "primary": "white",
        "secondary": "bright_white",
        "accent": "blue",
        "error": "red",
        "success": "green",
        "warning": "yellow",
        "info": "bright_blue",
    },
    "developer": {
        "primary": "bright_cyan",
        "secondary": "white",
        "accent": "bright_magenta",
        "error": "bright_red",
        "success": "bright_green",
        "warning": "bright_yellow",
        "info": "bright_blue",
    },
}

# Current theme (default: minimal)
_current_theme = "minimal"


def set_theme(theme: Literal["hacker", "minimal", "developer"] = "minimal") -> None:
    """Set the UI theme."""
    global _current_theme
    if theme in THEMES:
        _current_theme = theme
    else:
        _current_theme = "minimal"


def get_color(color_type: str) -> str:
    """Get color from current theme."""
    return THEMES[_current_theme].get(color_type, "white")


def show_banner() -> None:
    """Display minimal terminal banner."""
    console.print(f"[{get_color('accent')}]dev.mk[/{get_color('accent')}] by Kelvin Mukaria\n")


def show_step(step_name: str, status: str = "running", details: str = "") -> None:
    """
    Display a process step in terminal style.
    
    Status formats:
    - running: [*] Process name
    - success: [OK] Process name
    - error: [FAIL] Process name
    - skipped: [SKIP] Process name
    """
    status_markers = {
        "running": "[*]",
        "success": "[OK]",
        "error": "[FAIL]",
        "skipped": "[SKIP]",
        "pending": "[...]",
    }
    
    marker = status_markers.get(status, "[*]")
    
    color_map = {
        "running": get_color("info"),
        "success": get_color("success"),
        "error": get_color("error"),
        "skipped": get_color("warning"),
        "pending": get_color("info"),
    }
    
    color = color_map.get(status, get_color("info"))
    
    # Only show step name, skip details for minimal output
    console.print(f"{marker} [{color}]{step_name}[/{color}]")


def show_spinner(message: str):
    """
    Context manager for showing a spinner during operations.
    
    Usage:
        with show_spinner("Loading..."):
            # Do work here
            pass
    """
    class SpinnerContext:
        def __init__(self, msg: str):
            self.msg = msg
            self.progress = None
        
        def __enter__(self):
            self.progress = Progress(
                SpinnerColumn(spinner_name="dots", style=get_color("info")),
                TextColumn(f"[{get_color('info')}]{self.msg}[/{get_color('info')}]"),
                console=console,
                transient=True,
            )
            self.progress.start()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.progress:
                self.progress.stop()
            return False
    
    return SpinnerContext(message)


def show_panel(content: str, title: str = "", border_style: Optional[str] = None) -> None:
    """Display content in a minimal panel."""
    if not border_style:
        border_style = get_color("primary")
    
    panel = Panel(
        content,
        title=title,
        border_style=border_style,
        box=box.SIMPLE,
        padding=(1, 2),
    )
    console.print(panel)


def show_commit_preview(commit_message: str, diff_summary: str = "") -> str:
    """
    Show commit message preview and allow user interaction.
    
    Returns:
        Final commit message (user may edit or accept)
    """
    # Minimal preview - just show the message
    console.print(f"\n[{get_color('accent')}]{commit_message}[/{get_color('accent')}]")
    
    # Simplified options
        choice = Prompt.ask(
        f"[{get_color('info')}](1) Accept  (2) Edit  (3) Manual  (4) Cancel[/{get_color('info')}]",
        choices=["1", "2", "3", "4"],
            default="1",
        )
        
        if choice == "1":
            return commit_message
        elif choice == "2":
            edited = Prompt.ask(
            f"[{get_color('accent')}]Edit:[/{get_color('accent')}]",
                default=commit_message,
            )
            return edited.strip()
        elif choice == "3":
            manual = Prompt.ask(
            f"[{get_color('warning')}]Message:[/{get_color('warning')}]",
            )
            return manual.strip()
        else:
        console.print(f"[{get_color('error')}]Cancelled[/{get_color('error')}]")
            sys.exit(0)


def edit_with_editor(content: str) -> str:
    """Open content in editor and return edited version."""
    editor = os.getenv("EDITOR", "nano")
    
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(content)
        temp_path = f.name
    
    try:
        subprocess.run([editor, temp_path], check=True)
        with open(temp_path, "r") as f:
            edited = f.read().strip()
        return edited
    except Exception as e:
        console.print(f"[{get_color('error')}]Failed to open editor: {e}[/{get_color('error')}]")
        return content
    finally:
        os.unlink(temp_path)


def show_success(message: str) -> None:
    """Display success message."""
    console.print(f"[{get_color('success')}][OK] {message}[/{get_color('success')}]")


def show_error(message: str) -> None:
    """Display error message."""
    console.print(f"[{get_color('error')}][FAIL] {message}[/{get_color('error')}]")


def show_warning(message: str) -> None:
    """Display warning message."""
    console.print(f"[{get_color('warning')}][WARN] {message}[/{get_color('warning')}]")


def show_info(message: str) -> None:
    """Display info message."""
    console.print(f"[{get_color('info')}][INFO] {message}[/{get_color('info')}]")


def show_table(headers: list[str], rows: list[list[str]], title: str = "") -> None:
    """Display a minimal table."""
    table = Table(title=title, show_header=True, header_style=get_color("accent"), box=box.SIMPLE)
    
    for header in headers:
        table.add_column(header, style=get_color("secondary"))
    
    for row in rows:
        table.add_row(*row)
    
    console.print(table)


def confirm(message: str, default: bool = True) -> bool:
    """Show confirmation prompt."""
    return Confirm.ask(
        f"[{get_color('warning')}]{message}[/{get_color('warning')}]",
        default=default,
    )


def prompt_input(message: str, default: Optional[str] = None) -> str:
    """Show input prompt."""
    return Prompt.ask(
        f"[{get_color('primary')}]{message}[/{get_color('primary')}]",
        default=default or "",
    )


def show_summary(steps: list[dict]) -> None:
    """Show minimal workflow summary."""
    # Skip detailed summary table for minimal UI
    pass


def show_footer(success: bool = True, message: str = "") -> None:
    """Display footer before closing."""
    if success:
        status_text = f"[{get_color('success')}]✓ Done[/{get_color('success')}]"
    else:
        status_text = f"[{get_color('error')}]✗ Failed[/{get_color('error')}]"
    
    footer = f"\n{status_text}"
    if message:
        footer += f" - {message}"
    
    console.print(footer)
