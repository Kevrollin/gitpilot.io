"""Main orchestration logic for auto-commit workflow."""

import sys
from .git_handler import add_all, get_diff, commit, push, setup_git_repo_if_needed
from .ai_commit import generate_commit_message


def run_auto_commit() -> None:
    """
    Orchestrate the auto-commit workflow:
    1. Check if git repo exists, setup if needed
    2. If new repo: stage all files, generate AI commit message, make initial commit, push
    3. If existing repo: stage changes, check for changes, generate AI commit message, commit and push
    """
    try:
        # Step 0: Check if git repo exists, prompt for URL if needed
        is_new_repo, remote_url = setup_git_repo_if_needed()
        
        if is_new_repo:
            # Handle initial commit for new repository
            print("\n📦 Preparing initial commit...")
            
            # Stage all files
            add_all()
            
            # Get the diff of all staged files
            print("🔍 Analyzing files...")
            diff_text = get_diff()
            
            if not diff_text or diff_text.strip() == "":
                print("✅ No files to commit.")
                sys.exit(0)
            
            # Generate AI commit message for initial commit
            print("🤖 Generating initial commit message with AI...")
            commit_message = generate_commit_message(diff_text)
            print(f"📝 Generated message: {commit_message}")
            
            # Make initial commit message
            commit(commit_message)
            
            # Push if remote was provided
            if remote_url:
                push()
                print("\n🎉 Initial commit created and pushed successfully!")
            else:
                print("\n🎉 Initial commit created successfully!")
                print("ℹ️  No remote repository configured. Add one with: git remote add origin <url>")
            
        else:
            # Handle regular commits for existing repository
            # Step 1: Stage all changes
            add_all()
            
            # Step 2: Get the diff
            print("🔍 Analyzing changes...")
            diff_text = get_diff()
            
            # Step 3: Check if there are any changes
            if not diff_text or diff_text.strip() == "":
                print("✅ No changes to commit.")
                sys.exit(0)
            
            # Step 4: Generate commit message using AI
            print("🤖 Generating commit message with AI...")
            commit_message = generate_commit_message(diff_text)
            print(f"📝 Generated message: {commit_message}")
            
            # Step 5: Commit and push
            commit(commit_message)
            push()
            
            print("\n🎉 Congratulations! Auto-commit completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

