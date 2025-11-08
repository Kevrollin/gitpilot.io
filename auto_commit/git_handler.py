"""Git operations handler using subprocess."""

import subprocess


def run_cmd(cmd: list[str]) -> str:
    """
    Run a git command safely using subprocess.
    
    Args:
        cmd: List of command and arguments (e.g., ['git', 'add', '.'])
        
    Returns:
        Command output as string
        
    Raises:
        Exception: If command fails
    """
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_msg = e.stdout.strip() if e.stdout else str(e)
        raise Exception(f" Git command failed: {' '.join(cmd)}\n{error_msg}")


def add_all() -> None:
    """Stage all changes in the repository."""
    print("📦 Staging all changes...")
    run_cmd(['git', 'add', '.'])
    print("✅ All changes staged")


def get_diff() -> str:
    """
    Get the cached diff (staged changes).
    
    Returns:
        Diff text as string (empty if no staged changes)
    """
    diff_output = run_cmd(['git', 'diff', '--cached'])
    return diff_output


def commit(message: str) -> None:
    """
    Commit staged changes with the given message.
    
    Args:
        message: Commit message
    """
    print(f"💾 Committing changes: {message[:50]}...")
    run_cmd(['git', 'commit', '-m', message])
    print("✅ Changes committed successfully")


def push() -> None:
    """Push commits to the current branch."""
    print("🚀 Pushing to remote...")
    
    # Check if remote exists
    try:
        remote = run_cmd(['git', 'remote', 'get-url', 'origin'])
    except Exception:
        # No remote configured
        print("⚠️  No remote repository configured. Skipping push.")
        print("ℹ️  You can add a remote later with: git remote add origin <url>")
        return
    
    # Try to push - handle upstream setup if needed
    try:
        # First, try normal push
        run_cmd(['git', 'push'])
        print("✅ Changes pushed successfully")
    except Exception:
        # Push failed, might need to set upstream
        try:
            branch = run_cmd(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
            # Try pushing with upstream setup
            run_cmd(['git', 'push', '-u', 'origin', branch])
            print(f"✅ Changes pushed successfully (set upstream to origin/{branch})")
        except Exception as e:
            error_msg = str(e)
            if "fatal:" in error_msg.lower():
                print(f"⚠️  Could not push changes: {error_msg}")
                print("ℹ️  You may need to authenticate or set up the remote repository.")
            else:
                print(f"⚠️  Warning: Could not push changes: {error_msg}")


def is_git_repo() -> bool:
    """
    Check if the current directory is a git repository.
    
    Returns:
        True if it's a git repo, False otherwise
    """
    try:
        run_cmd(['git', 'rev-parse', '--git-dir'])
        return True
    except Exception:
        return False


def init_git_repo(remote_url: str = None) -> None:
    """
    Initialize a git repository and optionally set up remote.
    
    Args:
        remote_url: Optional git remote URL to add as 'origin'
    """
    print("🔧 Initializing git repository...")
    run_cmd(['git', 'init'])
    print("✅ Git repository initialized")
    
    if remote_url:
        print(f"🔗 Adding remote origin: {remote_url}")
        try:
            # Check if remote already exists
            try:
                existing_remote = run_cmd(['git', 'remote', 'get-url', 'origin'])
                print(f"⚠️  Remote 'origin' already exists: {existing_remote}")
                response = input("Do you want to update it? (y/n): ").strip().lower()
                if response == 'y':
                    run_cmd(['git', 'remote', 'set-url', 'origin', remote_url])
                    print("✅ Remote origin updated")
                else:
                    print("ℹ️  Keeping existing remote")
            except Exception:
                # Remote doesn't exist, add it
                run_cmd(['git', 'remote', 'add', 'origin', remote_url])
                print("✅ Remote origin added")
        except Exception as e:
            print(f"⚠️  Warning: Could not add remote: {str(e)}")
            print("ℹ️  You can add it manually later with: git remote add origin <url>")


def setup_git_repo_if_needed() -> tuple[bool, str]:
    """
    Check if git repo exists, if not prompt user for URL and initialize.
    
    Returns:
        Tuple of (is_new_repo: bool, remote_url: str)
        - is_new_repo: True if repo was just initialized, False if it already existed
        - remote_url: The remote URL if provided, empty string otherwise
    """
    if not is_git_repo():
        print("⚠️  No git repository found in the current directory.")
        print("📝 Please provide a git repository URL to associate with this folder.")
        print("   (You can also press Enter to skip and initialize without a remote)")
        
        remote_url = input("\n🔗 Git repository URL (or press Enter to skip): ").strip()
        
        if remote_url:
            # Clean up the URL - ensure it has proper format
            if not remote_url.startswith(('http://', 'https://', 'git@')):
                # Assume it's an https URL if no protocol
                remote_url = f"https://{remote_url}"
            # Ensure .git extension for https/http URLs (SSH URLs already have it)
            if remote_url.startswith(('http://', 'https://')) and not remote_url.endswith('.git'):
                remote_url = f"{remote_url}.git"
        
        init_git_repo(remote_url if remote_url else None)
        
        # Return True to indicate this is a new repo, and the remote URL
        return (True, remote_url if remote_url else "")
    else:
        # Repo already exists
        return (False, "")

