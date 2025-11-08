"""AI-powered commit message generation using Google Gemini API."""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file from current working directory if it exists
# This allows users to have a .env file in their project directory
load_dotenv()


def generate_commit_message(diff_text: str) -> str:
    """
    Generate a commit message from git diff using Gemini API.
    
    Args:
        diff_text: The git diff text to analyze
        
    Returns:
        A clean commit message string
        
    Raises:
        ValueError: If GEMINI_API_KEY is not set
        Exception: If API call fails
    """
    # Try to load API key from environment variable or .env file
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        error_msg = (
            "❌ GEMINI_API_KEY not found\n\n"
            "To set it up, use one of these methods:\n\n"
            "Option 1: Create a .env file in your project directory:\n"
            "   echo 'GEMINI_API_KEY=your-api-key-here' > .env\n\n"
            "Option 2: Export it as an environment variable:\n"
            "   export GEMINI_API_KEY='your-api-key-here'\n\n"
            "Option 3: Add it to ~/.bashrc or ~/.zshrc for persistence:\n"
            "   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc\n"
            "   source ~/.bashrc\n\n"
            "Get your API key from: https://makersuite.google.com/app/apikey"
        )
        raise ValueError(error_msg)
    
    try:
        genai.configure(api_key=api_key)
        
        # Prepare the prompt
        prompt = f"""Analyze the following git diff and generate a concise, professional commit message.
        
The commit message should:
- Be clear and descriptive
- Follow conventional commit format if applicable
- Be no longer than 72 characters for the subject line
- Not include explanations or meta-commentary, just the commit message itself

Git diff:
{diff_text}

Commit message:"""
        
        # Try common model names directly (faster than listing)
        # Order: try faster/cheaper models first
        model_names = [
            'gemini-1.5-flash',
            'gemini-1.5-flash-latest',
            'gemini-1.5-pro',
            'gemini-1.5-pro-latest',
            'gemini-1.0-pro',
            'gemini-1.0-pro-latest',
        ]
        
        response = None
        used_model = None
        last_error = None
        
        # Try each model until one works
        for model_name in model_names:
            try:
                print(f"   Trying model: {model_name}...", end="", flush=True)
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                used_model = model_name
                print(" ✅", flush=True)
                break  # Success!
            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                # If it's a 404/model not found, try next model
                if "404" in error_str or "not found" in error_str or "not supported" in error_str:
                    print(" ❌ (not available)", flush=True)
                    continue
                # For other errors, print and try next model
                print(f" ❌ ({str(e)[:50]}...)", flush=True)
                continue
        
        if response is None:
            # If all models failed, try listing available models as last resort
            try:
                print("   Discovering available models...", flush=True)
                models = genai.list_models()
                for model in models:
                    if 'generateContent' in model.supported_generation_methods:
                        model_name = model.name.replace('models/', '')
                        try:
                            print(f"   Trying discovered model: {model_name}...", end="", flush=True)
                            model_obj = genai.GenerativeModel(model_name)
                            response = model_obj.generate_content(prompt)
                            used_model = model_name
                            print(" ✅", flush=True)
                            break
                        except Exception:
                            print(" ❌", flush=True)
                            continue
            except Exception as list_error:
                pass  # Listing also failed
        
        if response is None:
            error_details = str(last_error) if last_error else "Unknown error"
            raise Exception(
                f"❌ Could not find an available Gemini model.\n\n"
                f"Tried models: {', '.join(model_names)}\n"
                f"Last error: {error_details[:200]}\n\n"
                f"This might be due to:\n"
                f"1. API key doesn't have access to Gemini models\n"
                f"2. API key is invalid or expired\n"
                f"3. Network/connectivity issues\n\n"
                f"Please verify your API key at: https://makersuite.google.com/app/apikey\n"
                f"And check available models at: https://ai.google.dev/models/gemini"
            )
        
        # Extract just the commit message, removing any extra formatting
        commit_message = response.text.strip()
        
        # Take only the first line if multiple lines, and clean it up
        if '\n' in commit_message:
            commit_message = commit_message.split('\n')[0].strip()
        
        # Remove quotes if present
        if commit_message.startswith('"') and commit_message.endswith('"'):
            commit_message = commit_message[1:-1]
        elif commit_message.startswith("'") and commit_message.endswith("'"):
            commit_message = commit_message[1:-1]
        
        return commit_message
        
    except Exception as e:
        error_msg = str(e)
        if "404" in error_msg or "not found" in error_msg.lower():
            raise Exception(
                f"❌ Gemini model not found. This might be due to:\n"
                f"  1. API key doesn't have access to the model\n"
                f"  2. Model name has changed\n"
                f"  3. API version issue\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please check: https://ai.google.dev/models/gemini"
            )
        raise Exception(f"❌ Failed to generate commit message: {error_msg}")

