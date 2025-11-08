"""Main orchestration logic for auto-commit workflow with Rich UI."""

import sys
from typing import Optional
from .git_ops import (
    is_git_repo, init_git_repo, add_all, get_diff, commit, push,
    get_current_branch, checkout_branch, get_diff_summary
)
from .ai import generate_commit_message
from .ui import (
    show_banner, show_step, show_spinner, show_panel, show_commit_preview,
    show_success, show_error, show_warning, show_info, confirm, prompt_input,
    show_summary, edit_with_editor, set_theme
)
from .logger import init_logger, get_logger


class AutoCommitWorkflow:
    """Main workflow orchestrator for auto-commit."""
    
    def __init__(
        self,
        dry_run: bool = False,
        skip_ai: bool = False,
        yes: bool = False,
        branch: Optional[str] = None,
        quiet: bool = False,
        log_file: Optional[str] = None,
        theme: str = "hacker",
    ):
        """
        Initialize workflow.
        
        Args:
            dry_run: Simulate operations without committing/pushing
            skip_ai: Skip AI generation, prompt for manual message
            yes: Auto-accept AI-generated messages
            branch: Branch name to commit to
            quiet: Suppress non-essential output
            log_file: Path to log file
            theme: UI theme (hacker, minimal, developer)
        """
        self.dry_run = dry_run
        self.skip_ai = skip_ai
        self.yes = yes
        self.branch = branch
        self.quiet = quiet
        self.log_file = log_file
        self.theme = theme
        
        # Initialize logger
        init_logger(log_file, verbose=not quiet)
        self.logger = get_logger()
        
        # Set theme
        set_theme(theme)
        
        # Workflow steps tracking
        self.steps = []
    
    def _add_step(self, name: str, status: str, details: str = ""):
        """Track workflow step."""
        self.steps.append({
            "name": name,
            "status": status,
            "details": details,
        })
        self.logger.step(name, status)
    
    def run(self) -> int:
        """
        Run the auto-commit workflow.
        
        Returns:
            Exit code (0 for success, 1 for error)
        """
        try:
            # Show banner (skip for help/version which are handled by argparse)
            if not self.quiet:
                show_banner()
            
            self.logger.info("Starting auto-commit workflow")
            
            # Step 0: Setup git repo if needed
            is_new_repo, remote_url = self._setup_repo()
            
            # Switch to branch if specified
            if self.branch:
                self._switch_branch()
            
            # Stage changes
            if not self._stage_changes():
                return 0  # No changes to commit
            
            # Get diff
            diff_text = self._get_diff()
            if not diff_text or diff_text.strip() == "":
                if not self.quiet:
                    show_info("No changes to commit")
                return 0
            
            # Generate commit message
            commit_message = self._generate_commit_message(diff_text)
            if not commit_message:
                return 1  # User cancelled or error
            
            # Preview and confirm commit message
            final_message = self._preview_commit_message(commit_message, diff_text)
            if not final_message:
                return 1  # User cancelled
            
            # Commit
            if not self._commit_changes(final_message):
                return 1
            
            # Push
            if not self.dry_run:
                self._push_changes()
            else:
                if not self.quiet:
                    show_info("Dry run: Skipping push")
            
            # Show summary
            if not self.quiet:
                self._show_summary()
            
            self.logger.info("Workflow completed successfully")
            return 0
            
        except KeyboardInterrupt:
            if not self.quiet:
                show_warning("Operation cancelled by user")
            self.logger.warning("Operation cancelled by user")
            return 1
        except Exception as e:
            if not self.quiet:
                show_error(str(e))
            self.logger.error(f"Workflow error: {str(e)}")
            return 1
    
    def _setup_repo(self) -> tuple[bool, str]:
        """Setup git repository if needed."""
        if not self.quiet:
            show_step("Checking git repository", "running")
        
        if is_git_repo():
            if not self.quiet:
                show_step("Git repository found", "success")
            self._add_step("Git Repo Check", "success", "Repository exists")
            return False, ""
        
        # No repo found - prompt for URL
        if not self.quiet:
            show_step("Git repository not found", "pending")
            show_warning("No git repository found in the current directory")
            show_info("Please provide a git repository URL to associate with this folder")
            show_info("(You can also press Enter to skip and initialize without a remote)")
        
        remote_url = prompt_input("Git repository URL (or press Enter to skip)", "")
        
        if remote_url:
            # Clean up the URL
            if not remote_url.startswith(('http://', 'https://', 'git@')):
                remote_url = f"https://{remote_url}"
            if remote_url.startswith(('http://', 'https://')) and not remote_url.endswith('.git'):
                remote_url = f"{remote_url}.git"
        
        # Initialize repo
        if not self.quiet:
            with show_spinner("Initializing git repository"):
                success, msg = init_git_repo(remote_url if remote_url else None)
        else:
            success, msg = init_git_repo(remote_url if remote_url else None)
        
        if success:
            if not self.quiet:
                show_step("Git repository initialized", "success")
            self._add_step("Git Repo Setup", "success", msg)
            return True, remote_url if remote_url else ""
        else:
            if not self.quiet:
                show_step("Git repository setup failed", "error")
            self._add_step("Git Repo Setup", "error", msg)
            raise Exception(msg)
    
    def _switch_branch(self) -> None:
        """Switch to specified branch."""
        if not self.branch:
            return
        
        current_branch = get_current_branch()
        if current_branch == self.branch:
            if not self.quiet:
                show_info(f"Already on branch: {self.branch}")
            return
        
        if not self.quiet:
            with show_spinner(f"Switching to branch: {self.branch}"):
                success = checkout_branch(self.branch, create=True)
        else:
            success = checkout_branch(self.branch, create=True)
        
        if success:
            if not self.quiet:
                show_success(f"Switched to branch: {self.branch}")
            self._add_step("Branch Switch", "success", f"Switched to {self.branch}")
        else:
            if not self.quiet:
                show_warning(f"Could not switch to branch: {self.branch}")
            self._add_step("Branch Switch", "error", f"Failed to switch to {self.branch}")
    
    def _stage_changes(self) -> bool:
        """Stage all changes."""
        if not self.quiet:
            show_step("Staging changes", "running")
        
        if self.dry_run:
            if not self.quiet:
                show_info("Dry run: Would stage all changes")
            self._add_step("Stage Changes", "success", "Dry run: simulated")
            return True
        
        if not self.quiet:
            with show_spinner("Staging all changes"):
                success = add_all()
        else:
            success = add_all()
        
        if success:
            if not self.quiet:
                show_step("Changes staged", "success")
            self._add_step("Stage Changes", "success", "All changes staged")
            return True
        else:
            if not self.quiet:
                show_step("Staging failed", "error")
            self._add_step("Stage Changes", "error", "Failed to stage changes")
            return False
    
    def _get_diff(self) -> str:
        """Get diff of staged changes."""
        if not self.quiet:
            show_step("Analyzing changes", "running")
        
        if not self.quiet:
            with show_spinner("Analyzing git diff"):
                diff_text = get_diff()
        else:
            diff_text = get_diff()
        
        if not self.quiet:
            show_step("Changes analyzed", "success")
        
        self._add_step("Analyze Changes", "success", f"Diff length: {len(diff_text)} chars")
        return diff_text
    
    def _generate_commit_message(self, diff_text: str) -> Optional[str]:
        """Generate commit message using AI or prompt user."""
        if not self.quiet:
            show_step("Generating commit message", "running")
        
        if self.skip_ai:
            # Skip AI, prompt for manual message
            if not self.quiet:
                show_info("Skipping AI generation")
                commit_message = prompt_input("Enter commit message")
            else:
                commit_message = input("Enter commit message: ")
            
            if commit_message:
                self._add_step("Generate Message", "success", "Manual message entered")
                return commit_message.strip()
            return None
        
        # Generate with AI (silently in background, no callback)
        try:
            if not self.quiet:
                with show_spinner("Generating commit message with AI"):
                    commit_message = generate_commit_message(diff_text, None)
            else:
                commit_message = generate_commit_message(diff_text, None)
            
            if not self.quiet:
                show_step("Commit message generated", "success")
            
            self._add_step("Generate Message", "success", f"AI generated: {commit_message[:50]}")
            return commit_message
            
        except Exception as e:
            if not self.quiet:
                show_step("AI generation failed", "error")
                show_error(f"Failed to generate commit message: {str(e)}")
            self._add_step("Generate Message", "error", str(e))
            
            # Fallback to manual input
            if not self.quiet:
                show_info("Falling back to manual input")
                commit_message = prompt_input("Enter commit message manually")
            else:
                commit_message = input("Enter commit message manually: ")
            
            if commit_message:
                return commit_message.strip()
            return None
    
    def _preview_commit_message(self, commit_message: str, diff_text: str) -> Optional[str]:
        """Preview and allow user to edit commit message."""
        if self.yes or self.dry_run:
            # Auto-accept
            if not self.quiet:
                show_info(f"Auto-accepting commit message: {commit_message}")
            return commit_message
        
        if self.quiet:
            # In quiet mode, just return the message
            return commit_message
        
        # Show preview with options
        diff_summary = get_diff_summary()
        final_message = show_commit_preview(commit_message, diff_summary)
        
        if not self.quiet:
            show_step("Commit message confirmed", "success")
        
        return final_message
    
    def _commit_changes(self, message: str) -> bool:
        """Commit staged changes."""
        if not self.quiet:
            show_step("Committing changes", "running")
        
        if self.dry_run:
            if not self.quiet:
                show_info(f"Dry run: Would commit with message: {message}")
            self._add_step("Commit", "success", "Dry run: simulated")
            return True
        
        if not self.quiet:
            with show_spinner(f"Committing: {message[:50]}..."):
                success = commit(message)
        else:
            success = commit(message)
        
        if success:
            if not self.quiet:
                show_step("Changes committed", "success")
            self._add_step("Commit", "success", message)
            return True
        else:
            if not self.quiet:
                show_step("Commit failed", "error")
            self._add_step("Commit", "error", "Failed to commit")
            return False
    
    def _push_changes(self) -> bool:
        """Push commits to remote."""
        if not self.quiet:
            show_step("Pushing to remote", "running")
        
        current_branch = get_current_branch()
        if not self.quiet:
            with show_spinner("Pushing to remote"):
                success, msg = push(self.branch or current_branch, dry_run=self.dry_run)
        else:
            success, msg = push(self.branch or current_branch, dry_run=self.dry_run)
        
        if success:
            if not self.quiet:
                show_step("Changes pushed", "success")
            self._add_step("Push", "success", msg)
            return True
        else:
            if not self.quiet:
                show_step("Push failed or skipped", "skipped")
                show_warning(msg)
            self._add_step("Push", "skipped", msg)
            return False
    
    def _show_summary(self) -> None:
        """Show workflow summary."""
        if not self.quiet:
            show_summary(self.steps)
            show_success("Auto-commit completed successfully!")


def run_auto_commit(
    dry_run: bool = False,
    skip_ai: bool = False,
    yes: bool = False,
    branch: Optional[str] = None,
    quiet: bool = False,
    log_file: Optional[str] = None,
    theme: str = "hacker",
) -> int:
    """
    Run the auto-commit workflow.
    
    Args:
        dry_run: Simulate operations without committing/pushing
        skip_ai: Skip AI generation, prompt for manual message
        yes: Auto-accept AI-generated messages
        branch: Branch name to commit to
        quiet: Suppress non-essential output
        log_file: Path to log file
        theme: UI theme (hacker, minimal, developer)
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    workflow = AutoCommitWorkflow(
        dry_run=dry_run,
        skip_ai=skip_ai,
        yes=yes,
        branch=branch,
        quiet=quiet,
        log_file=log_file,
        theme=theme,
    )
    return workflow.run()
