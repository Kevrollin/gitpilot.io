"""CLI entry point for autocommit command with argument parsing."""

import argparse
import sys
from auto_commit.main import run_auto_commit


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
        default="hacker",
        help="UI theme: hacker (default), minimal, or developer",
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Gitpilot 0.1.0",
    )
    
    # Parse arguments - this will handle --help and --version automatically
    args = parser.parse_args()
    
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
