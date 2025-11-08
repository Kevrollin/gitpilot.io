# Changelog

All notable changes to Gitpilot will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Auto-update functionality with `--update` and `--check-updates` flags
- Simplified UI with minimal output and footer display
- Installation via pipx support (recommended for Linux)
- GitHub Actions workflow for automated releases
- Release script for easy version management

### Changed
- Simplified commit preview interface
- Reduced verbose output in UI
- Improved installation documentation for externally-managed environments
- Updated installation methods to handle modern Linux distributions

### Fixed
- Installation issues on Ubuntu 22.04+ and Debian 12+
- Externally-managed-environment errors
- PATH configuration for user installations

## [0.1.0] - 2024-01-XX

### Added
- Initial release
- AI-powered commit message generation using Google Gemini API
- Automatic git staging, committing, and pushing
- Interactive commit message preview and editing
- Rich terminal UI with multiple themes
- CLI flags for automation (--yes, --dry-run, --skip-ai, etc.)
- Branch switching support
- Logging functionality
- Support for new repository initialization

### Features
- Beautiful terminal interface with spinners and progress bars
- Multiple UI themes (hacker, minimal, developer)
- File logging for debugging
- Graceful error handling
- Cross-platform support (Linux, macOS)

