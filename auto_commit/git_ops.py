"""Git operations handler - refactored to return values instead of printing."""

import subprocess
from typing import Optional, Tuple
from .logger import get_logger

logger = get_logger()


def run_cmd(cmd: list[str], check: bool = True) -> Tuple[str, bool]:
    """
    Run a git command safely using subprocess.
    
    Args:
        cmd: List of command and arguments (e.g., ['git', 'add', '.'])
        check: Whether to raise exception on error
        
    Returns:
        Tuple of (output: str, success: bool)
    """
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=check,
        )
        output = result.stdout.strip()
        logger.git_command(' '.join(cmd), output)
        return output, True
    except subprocess.CalledProcessError as e:
        error_msg = e.stdout.strip() if e.stdout else str(e)
        logger.error(f"Git command failed: {' '.join(cmd)} - {error_msg}")
        if check:
            raise Exception(f"Git command failed: {' '.join(cmd)}\n{error_msg}")
        return error_msg, False


def add_all() -> bool:
    """
    Stage all changes in the repository.
    
    Returns:
        True if successful, False otherwise
    """
    logger.step("Staging all changes")
    output, success = run_cmd(['git', 'add', '.'])
    if success:
        logger.step("Staging all changes", "completed")
    return success


def get_diff() -> str:
    """
    Get the cached diff (staged changes).
    
    Returns:
        Diff text as string (empty if no staged changes)
    """
    logger.step("Getting diff")
    diff_output, _ = run_cmd(['git', 'diff', '--cached'], check=False)
    logger.step("Getting diff", "completed")
    return diff_output


def commit(message: str) -> bool:
    """
    Commit staged changes with the given message.
    
    Args:
        message: Commit message
        
    Returns:
        True if successful, False otherwise
    """
    logger.step(f"Committing: {message[:50]}")
    output, success = run_cmd(['git', 'commit', '-m', message])
    if success:
        logger.step("Commit", "completed")
    return success


def push(branch: Optional[str] = None, dry_run: bool = False) -> Tuple[bool, str]:
    """
    Push commits to the current branch.
    
    Args:
        branch: Optional branch name to push to
        dry_run: If True, simulate push without actually pushing
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    if dry_run:
        logger.info("DRY RUN: Would push to remote")
        return True, "Dry run: push simulated"
    
    logger.step("Pushing to remote")
    
    # Check if remote exists
    remote_output, remote_exists = run_cmd(['git', 'remote', 'get-url', 'origin'], check=False)
    if not remote_exists:
        msg = "No remote repository configured"
        logger.warning(msg)
        return False, msg
    
    # Get current branch if not specified
    if not branch:
        branch_output, success = run_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], check=False)
        if success:
            branch = branch_output
    
    # Try to push
    output, success = run_cmd(['git', 'push'], check=False)
    if success:
        logger.step("Push", "completed")
        return True, "Changes pushed successfully"
    
    # Try with upstream setup
    if branch:
        output, success = run_cmd(['git', 'push', '-u', 'origin', branch], check=False)
        if success:
            logger.step("Push", "completed")
            return True, f"Changes pushed successfully (set upstream to origin/{branch})"
    
    error_msg = f"Could not push changes: {output}"
    logger.error(error_msg)
    return False, error_msg


def is_git_repo() -> bool:
    """
    Check if the current directory is a git repository.
    
    Returns:
        True if it's a git repo, False otherwise
    """
    _, success = run_cmd(['git', 'rev-parse', '--git-dir'], check=False)
    return success


def init_git_repo(remote_url: Optional[str] = None) -> Tuple[bool, str]:
    """
    Initialize a git repository and optionally set up remote.
    
    Args:
        remote_url: Optional git remote URL to add as 'origin'
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    logger.step("Initializing git repository")
    output, success = run_cmd(['git', 'init'])
    if not success:
        return False, "Failed to initialize git repository"
    
    logger.step("Initializing git repository", "completed")
    
    if remote_url:
        logger.step(f"Adding remote: {remote_url}")
        # Check if remote already exists
        existing_output, remote_exists = run_cmd(['git', 'remote', 'get-url', 'origin'], check=False)
        if remote_exists:
            return True, f"Remote 'origin' already exists: {existing_output}"
        
        # Add remote
        output, success = run_cmd(['git', 'remote', 'add', 'origin', remote_url], check=False)
        if success:
            logger.step("Adding remote", "completed")
            return True, "Remote origin added successfully"
        else:
            return False, f"Failed to add remote: {output}"
    
    return True, "Git repository initialized (no remote)"


def get_current_branch() -> Optional[str]:
    """Get current git branch name."""
    output, success = run_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], check=False)
    return output if success else None


def get_remote_url() -> Optional[str]:
    """Get remote origin URL."""
    output, success = run_cmd(['git', 'remote', 'get-url', 'origin'], check=False)
    return output if success else None


def checkout_branch(branch: str, create: bool = False) -> bool:
    """
    Checkout a branch.
    
    Args:
        branch: Branch name
        create: If True, create branch if it doesn't exist
        
    Returns:
        True if successful
    """
    if create:
        output, success = run_cmd(['git', 'checkout', '-b', branch], check=False)
    else:
        output, success = run_cmd(['git', 'checkout', branch], check=False)
    return success


def get_diff_summary() -> str:
    """Get a summary of changes (file names only)."""
    output, success = run_cmd(['git', 'diff', '--cached', '--name-status'], check=False)
    if success and output:
        files = output.split('\n')
        return f"{len(files)} file(s) changed"
    return "No changes"


def setup_git_repo_if_needed(prompt_callback=None) -> tuple[bool, str]:
    """
    Check if git repo exists, if not prompt user for URL and initialize.
    
    Args:
        prompt_callback: Optional callback function to get remote URL from user
        
    Returns:
        Tuple of (is_new_repo: bool, remote_url: str)
        - is_new_repo: True if repo was just initialized, False if it already existed
        - remote_url: The remote URL if provided, empty string otherwise
    """
    if is_git_repo():
        return False, ""
    
    # No repo found - get URL from callback or return empty
    remote_url = ""
    if prompt_callback:
        remote_url = prompt_callback()
    
    if remote_url:
        # Clean up the URL
        if not remote_url.startswith(('http://', 'https://', 'git@')):
            remote_url = f"https://{remote_url}"
        if remote_url.startswith(('http://', 'https://')) and not remote_url.endswith('.git'):
            remote_url = f"{remote_url}.git"
        
        # Initialize repo with remote
        success, msg = init_git_repo(remote_url)
        if success:
            return True, remote_url
    
    # Initialize repo without remote
    success, msg = init_git_repo(None)
    if success:
        return True, ""
    
    return False, ""

