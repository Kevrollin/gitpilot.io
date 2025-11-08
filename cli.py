"""CLI entry point for autocommit command with argument parsing."""

import argparse
import sys
from auto_commit.main import run_auto_commit
from auto_commit.updater import update_from_git, check_for_updates, get_repo_url, get_installed_version
from auto_commit.ui import show_info, show_success, show_error, show_warning, set_theme
from auto_commit import __version__


def main():
    """Parse CLI arguments and run auto-commit workflow."""
    parser = argparse.ArgumentParser(
        description="Gitpilot - AI-Powered Auto Commit Assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  autocommit                    # Interactive mode with AI-generated commits
  autocommit --yes              # Auto-accept AI messages
  autocommit --dry-run          # Simulate without committing/pushing
  autocommit --skip-ai          # Skip AI, enter manual commit message
  autocommit --branch feature   # Commit to specific branch
  autocommit --quiet --log log.txt  # Quiet mode with logging
  autocommit --theme minimal    # Use minimal theme

For more information, visit: https://github.com/your-repo/gitpilot
        """,
    )
    
    parser.add_argument(
        "--yes",
        "-y",
        action="store_true",
        help="Auto-accept AI-generated commit messages without preview",
    )
    
    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="Simulate all operations without committing or pushing",
    )
    
    parser.add_argument(
        "--skip-ai",
        "-s",
        action="store_true",
        help="Skip AI generation and prompt for manual commit message",
    )
    
    parser.add_argument(
        "--branch",
        "-b",
        type=str,
        metavar="NAME",
        help="Branch name to commit to (will create if doesn't exist)",
    )
    
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress non-essential output (useful for scripting)",
    )
    
    parser.add_argument(
        "--log",
        "-l",
        type=str,
        metavar="FILE",
        help="Log all operations to specified file",
    )
    
    parser.add_argument(
        "--theme",
        "-t",
        type=str,
        choices=["hacker", "minimal", "developer"],
        default="minimal",
        help="UI theme: minimal (default), hacker, or developer",
    )
    
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"Gitpilot {__version__}",
    )
    
    parser.add_argument(
        "--update",
        "-u",
        action="store_true",
        help="Update Gitpilot to the latest version from repository",
    )
    
    parser.add_argument(
        "--check-updates",
        action="store_true",
        help="Check if updates are available",
    )
    
    # Parse arguments - this will handle --help and --version automatically
    args = parser.parse_args()
    
    # Handle update commands first
    if args.update:
        set_theme(args.theme)
        show_info("Checking for updates...")
        repo_url = get_repo_url()
        show_info(f"Repository: {repo_url}")
        show_info(f"Current version: {get_installed_version()}")
        
        if update_from_git(repo_url, quiet=args.quiet):
            show_success("Update completed! Please restart your terminal.")
            sys.exit(0)
        else:
            show_error("Update failed. Check logs for details.")
            sys.exit(1)
    
    if args.check_updates:
        set_theme(args.theme)
        show_info(f"Current version: {get_installed_version()}")
        has_updates, latest = check_for_updates()
        if has_updates:
            show_warning(f"Updates available (latest: {latest})")
            show_info("Run 'autocommit --update' to update")
        else:
            show_success("You're running the latest version")
        sys.exit(0)
    
    # Run the workflow (only if we get here, --help and --version have been handled)
    exit_code = run_auto_commit(
        dry_run=args.dry_run,
        skip_ai=args.skip_ai,
        yes=args.yes,
        branch=args.branch,
        quiet=args.quiet,
        log_file=args.log,
        theme=args.theme,
    )
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
