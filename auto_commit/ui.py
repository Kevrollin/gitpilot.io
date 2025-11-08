"""Rich-based interactive terminal UI for auto-commit assistant."""

import sys
from datetime import datetime
from typing import Optional, Literal
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text
from rich import box
import subprocess
import os

# Initialize console
console = Console()

# Theme colors
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
        "primary": "blue",
        "secondary": "white",
        "accent": "bright_blue",
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

# Current theme (default: hacker)
_current_theme = "hacker"


def set_theme(theme: Literal["hacker", "minimal", "developer"] = "hacker") -> None:
    """Set the UI theme."""
    global _current_theme
    if theme in THEMES:
        _current_theme = theme
    else:
        _current_theme = "hacker"


def get_color(color_type: str) -> str:
    """Get color from current theme."""
    return THEMES[_current_theme].get(color_type, "white")


def show_banner() -> None:
    """Display hacker/dev-inspired ASCII banner."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    banner_text = Text()
    banner_text.append("╔═══════════════════════════════════════════════════════╗\n", style=get_color("primary"))
    banner_text.append("║                                                       ║\n", style=get_color("primary"))
    banner_text.append("║", style=get_color("primary"))
    banner_text.append("          GITPILOT - AUTO COMMIT ASSISTANT", style=f"bold {get_color('accent')}")
    banner_text.append("          ║\n", style=get_color("primary"))
    banner_text.append("║", style=get_color("primary"))
    banner_text.append("              AI-Powered Git Automation", style=get_color("secondary"))
    banner_text.append("              ║\n", style=get_color("primary"))
    banner_text.append("║                                                       ║\n", style=get_color("primary"))
    banner_text.append("╚═══════════════════════════════════════════════════════╝\n", style=get_color("primary"))
    banner_text.append(f"  🚀 Initialized at {timestamp}\n", style=get_color("info"))
    
    console.print(banner_text)


def show_step(step_number: int, total_steps: int, step_name: str, status: str = "pending") -> None:
    """Display a step in the workflow."""
    status_icons = {
        "pending": "⏳",
        "running": "⚙️",
        "success": "✅",
        "error": "❌",
        "skipped": "⏭️",
    }
    
    icon = status_icons.get(status, "⏳")
    color = {
        "pending": get_color("info"),
        "running": get_color("accent"),
        "success": get_color("success"),
        "error": get_color("error"),
        "skipped": get_color("warning"),
    }.get(status, get_color("info"))
    
    step_text = f"[{step_number}/{total_steps}] {icon} {step_name}"
    console.print(f"  {step_text}", style=color)


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
                SpinnerColumn(spinner_name="dots", style=get_color("accent")),
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


def show_progress_bar(message: str, total: int = 100):
    """Create a progress bar context manager."""
    return Progress(
        TextColumn(f"[{get_color('info')}]{message}[/{get_color('info')}]"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    )


def show_panel(content: str, title: str = "", border_style: Optional[str] = None) -> None:
    """Display content in a Rich panel."""
    if not border_style:
        border_style = get_color("primary")
    
    panel = Panel(
        content,
        title=title,
        border_style=border_style,
        box=box.ROUNDED,
        padding=(1, 2),
    )
    console.print(panel)


def show_commit_preview(commit_message: str, diff_summary: str = "") -> str:
    """
    Show commit message preview and allow user interaction.
    
    Returns:
        Final commit message (user may edit or accept)
    """
    # Create preview panel
    preview_content = f"[{get_color('accent')}]{commit_message}[/{get_color('accent')}]"
    if diff_summary:
        preview_content += f"\n\n[{get_color('info')}]Changes: {diff_summary}[/{get_color('info')}]"
    
    show_panel(
        preview_content,
        title="[bold]🤖 AI-Generated Commit Message[/bold]",
        border_style=get_color("accent"),
    )
    
    # Show options
    console.print(f"\n[{get_color('info')}]Options:[/{get_color('info')}]")
    console.print(f"  [{get_color('success')}]1.[/{get_color('success')}] Accept and continue")
    console.print(f"  [{get_color('accent')}]2.[/{get_color('accent')}] Edit message inline")
    console.print(f"  [{get_color('accent')}]3.[/{get_color('accent')}] Edit in editor ($EDITOR)")
    console.print(f"  [{get_color('warning')}]4.[/{get_color('warning')}] Enter manual message")
    console.print(f"  [{get_color('error')}]5.[/{get_color('error')}] Cancel")
    
    while True:
        choice = Prompt.ask(
            f"\n[{get_color('primary')}]Your choice[/{get_color('primary')}]",
            choices=["1", "2", "3", "4", "5"],
            default="1",
        )
        
        if choice == "1":
            # Accept and continue
            return commit_message
        elif choice == "2":
            # Edit message inline
            edited = Prompt.ask(
                f"[{get_color('accent')}]Edit commit message[/{get_color('accent')}]",
                default=commit_message,
            )
            return edited.strip()
        elif choice == "3":
            # Edit in editor
            try:
                edited = edit_with_editor(commit_message)
                return edited.strip() if edited else commit_message
            except Exception as e:
                console.print(f"[{get_color('error')}]Failed to open editor: {e}[/{get_color('error')}]")
                console.print(f"[{get_color('warning')}]Falling back to inline editing...[/{get_color('warning')}]")
                edited = Prompt.ask(
                    f"[{get_color('accent')}]Edit commit message[/{get_color('accent')}]",
                    default=commit_message,
                )
                return edited.strip()
        elif choice == "4":
            # Manual message
            manual = Prompt.ask(
                f"[{get_color('warning')}]Enter commit message[/{get_color('warning')}]",
            )
            return manual.strip()
        else:
            # Cancel
            console.print(f"\n[{get_color('error')}]Operation cancelled[/{get_color('error')}]")
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
    console.print(f"[{get_color('success')}]✅ {message}[/{get_color('success')}]")


def show_error(message: str) -> None:
    """Display error message."""
    console.print(f"[{get_color('error')}]❌ {message}[/{get_color('error')}]")


def show_warning(message: str) -> None:
    """Display warning message."""
    console.print(f"[{get_color('warning')}]⚠️  {message}[/{get_color('warning')}]")


def show_info(message: str) -> None:
    """Display info message."""
    console.print(f"[{get_color('info')}]ℹ️  {message}[/{get_color('info')}]")


def show_table(headers: list[str], rows: list[list[str]], title: str = "") -> None:
    """Display a Rich table."""
    table = Table(title=title, show_header=True, header_style=get_color("accent"))
    
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
    """Show workflow summary table."""
    table = Table(title="Workflow Summary", show_header=True, header_style=get_color("accent"))
    table.add_column("Step", style=get_color("secondary"))
    table.add_column("Status", style=get_color("secondary"))
    table.add_column("Details", style=get_color("secondary"))
    
    for step in steps:
        status_color = {
            "success": get_color("success"),
            "error": get_color("error"),
            "skipped": get_color("warning"),
        }.get(step.get("status", "pending"), get_color("info"))
        
        table.add_row(
            step.get("name", ""),
            f"[{status_color}]{step.get('status', 'pending')}[/{status_color}]",
            step.get("details", ""),
        )
    
    console.print(table)

