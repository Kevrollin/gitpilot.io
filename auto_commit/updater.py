"""Auto-update functionality for Gitpilot."""

import subprocess
import sys
import os
from typing import Optional, Tuple
from .logger import get_logger

logger = get_logger()

# Default git repository URL - should be set to your actual repo
DEFAULT_REPO_URL = os.getenv(
    "GITPILOT_REPO_URL",
    "https://github.com/Kevrollin/gitpilot.io"
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
        if not quiet:
            logger.info(f"Updating from {repo_url}...")
        
        # Install/upgrade from git
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
        )
        
        if result.returncode == 0:
            if not quiet:
                logger.info("Update completed successfully")
            return True
        else:
            logger.error(f"Update failed: {result.stderr}")
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

