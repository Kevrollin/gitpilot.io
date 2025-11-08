"""Auto-update functionality for dev.mk."""

import subprocess
import sys
import os
from typing import Optional, Tuple
from .logger import get_logger

logger = get_logger()

# Default git repository URL - should be set to your actual repo
DEFAULT_REPO_URL = os.getenv(
    "GITPILOT_REPO_URL",
    "https://github.com/Kevrollin/gitpilot.io.git"
)


def get_installed_version() -> str:
    """Get the currently installed version."""
    try:
        from . import __version__
        return __version__
    except ImportError:
        return "unknown"


def get_repo_url() -> str:
    """Get the git repository URL for updates."""
    return DEFAULT_REPO_URL


def check_for_updates(repo_url: Optional[str] = None) -> Tuple[bool, str]:
    """
    Check if updates are available from the git repository.
    
    Returns:
        Tuple of (has_updates: bool, latest_version: str)
    """
    if repo_url is None:
        repo_url = get_repo_url()
    
    try:
        # Check remote for latest commit
        result = subprocess.run(
            ["git", "ls-remote", repo_url, "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        
        if result.returncode != 0:
            logger.warning(f"Failed to check for updates: {result.stderr}")
            return False, get_installed_version()
        
        # Extract commit hash
        latest_commit = result.stdout.split()[0] if result.stdout.strip() else None
        
        if not latest_commit:
            return False, get_installed_version()
        
        # For now, we'll consider it updated if we can reach the repo
        # In a full implementation, you'd compare commit hashes or tags
        return True, latest_commit[:8]
        
    except subprocess.TimeoutExpired:
        logger.warning("Update check timed out")
        return False, get_installed_version()
    except Exception as e:
        logger.warning(f"Error checking for updates: {str(e)}")
        return False, get_installed_version()


def is_installed_with_pipx() -> bool:
    """Check if the package is installed via pipx."""
    try:
        # Check if running in a pipx environment
        # pipx installs packages in isolated venvs
        venv_path = getattr(sys, 'real_prefix', None) or (getattr(sys, 'base_prefix', None) if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix else None)
        if venv_path:
            # Check if this looks like a pipx environment
            venv_str = str(venv_path)
            if 'pipx' in venv_str or '.local/pipx' in venv_str or '.pipx' in venv_str:
                return True
        
        # Alternative: check if pipx command exists and package is listed
        result = subprocess.run(
            ["pipx", "list"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and "auto-commit-assistant" in result.stdout:
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        pass
    return False


def update_from_git(repo_url: Optional[str] = None, quiet: bool = False) -> bool:
    """
    Update the package by reinstalling from git repository.
    
    Args:
        repo_url: Git repository URL (defaults to DEFAULT_REPO_URL)
        quiet: Suppress output
        
    Returns:
        True if update was successful, False otherwise
    """
    if repo_url is None:
        repo_url = get_repo_url()
    
    try:
        # Check if installed with pipx
        if is_installed_with_pipx():
            if not quiet:
                logger.info("Detected pipx installation. Using pipx to update...")
            
            # Use pipx to upgrade
            result = subprocess.run(
                ["pipx", "upgrade", "auto-commit-assistant"],
                capture_output=True,
                text=True,
                timeout=300,
            )
            
            if result.returncode == 0:
                if not quiet:
                    logger.info("Update completed successfully with pipx")
                return True
            else:
                # If pipx upgrade fails, try reinstalling
                if not quiet:
                    logger.info("pipx upgrade failed, trying reinstall...")
                
                result = subprocess.run(
                    ["pipx", "reinstall", "--force", f"git+{repo_url}"],
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                
                if result.returncode == 0:
                    if not quiet:
                        logger.info("Reinstall completed successfully")
                    return True
                else:
                    logger.error(f"pipx update failed: {result.stderr}")
                    if not quiet:
                        logger.error("Try manually: pipx upgrade auto-commit-assistant")
                    return False
        
        # Regular pip installation
        if not quiet:
            logger.info(f"Updating from {repo_url}...")
        
        # Try with --user flag first (avoids permission issues)
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--user",
                "--upgrade",
                "--force-reinstall",
                f"git+{repo_url}",
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )
        
        if result.returncode == 0:
            if not quiet:
                logger.info("Update completed successfully")
            return True
        else:
            # Try without --user flag
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    "--force-reinstall",
                    f"git+{repo_url}",
                ],
                capture_output=True,
                text=True,
                timeout=300,
            )
            
            if result.returncode == 0:
                if not quiet:
                    logger.info("Update completed successfully")
                return True
            else:
                logger.error(f"Update failed: {result.stderr}")
                return False
            
    except subprocess.TimeoutExpired:
        logger.error("Update timed out")
        return False
    except Exception as e:
        logger.error(f"Error during update: {str(e)}")
        return False


def install_from_git(repo_url: Optional[str] = None, quiet: bool = False) -> bool:
    """
    Install the package from git repository.
    
    Args:
        repo_url: Git repository URL (defaults to DEFAULT_REPO_URL)
        quiet: Suppress output
        
    Returns:
        True if installation was successful, False otherwise
    """
    if repo_url is None:
        repo_url = get_repo_url()
    
    try:
        if not quiet:
            logger.info(f"Installing from {repo_url}...")
        
        # Install from git
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                f"git+{repo_url}",
            ],
            capture_output=True,
            text=True,
        )
        
        if result.returncode == 0:
            if not quiet:
                logger.info("Installation completed successfully")
            return True
        else:
            logger.error(f"Installation failed: {result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"Error during installation: {str(e)}")
        return False

