"""Setup configuration for auto-commit-assistant package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Get version from package
try:
    from auto_commit import __version__
    version = __version__
except ImportError:
    version = "0.1.0"

setup(
    name="auto-commit-assistant",
    version=version,
    author="Gitpilot",
    description="Automatically stage, analyze, commit, and push Git changes using AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "autocommit=cli:main",
        ],
    },
)

