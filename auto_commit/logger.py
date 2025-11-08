"""Logging module for auto-commit assistant."""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


class AutoCommitLogger:
    """Logger for auto-commit operations."""
    
    def __init__(self, log_file: Optional[str] = None, verbose: bool = True):
        """
        Initialize logger.
        
        Args:
            log_file: Optional path to log file
            verbose: Whether to log to console
        """
        self.logger = logging.getLogger("autocommit")
        self.logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_formatter = logging.Formatter(
            '%(levelname)s - %(message)s'
        )
        
        # File handler
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        # Console handler (only if verbose)
        if verbose:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)
    
    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(message)
    
    def step(self, step_name: str, status: str = "started") -> None:
        """Log a workflow step."""
        self.info(f"STEP: {step_name} - {status}")
    
    def git_command(self, command: str, output: str = "") -> None:
        """Log git command execution."""
        self.debug(f"GIT: {command}")
        if output:
            self.debug(f"GIT OUTPUT: {output[:200]}...")  # Limit output length
    
    def ai_request(self, model: str, prompt_length: int) -> None:
        """Log AI request."""
        self.info(f"AI: Requesting from model {model} (prompt length: {prompt_length})")
    
    def ai_response(self, message: str) -> None:
        """Log AI response."""
        self.info(f"AI: Generated commit message: {message}")


# Global logger instance
_logger_instance: Optional[AutoCommitLogger] = None


def get_logger() -> AutoCommitLogger:
    """Get global logger instance."""
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = AutoCommitLogger()
    return _logger_instance


def init_logger(log_file: Optional[str] = None, verbose: bool = True) -> AutoCommitLogger:
    """Initialize global logger."""
    global _logger_instance
    _logger_instance = AutoCommitLogger(log_file, verbose)
    return _logger_instance

