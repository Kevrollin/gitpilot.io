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
        
        # First, try to list available models to find a working one
        available_model = None
        try:
            # List available models
            models = genai.list_models()
            for model in models:
                # Look for models that support generateContent
                if 'generateContent' in model.supported_generation_methods:
                    model_name = model.name.replace('models/', '')
                    # Prefer flash models (faster and cheaper)
                    if 'flash' in model_name.lower():
                        available_model = model_name
                        break
                    # Otherwise use the first available model
                    if available_model is None:
                        available_model = model_name
        except Exception as e:
            # If listing models fails, fall back to trying common names
            pass
        
        # If no model found from listing, try common model names
        if available_model is None:
            model_names = [
                'gemini-1.5-flash',
                'gemini-1.5-pro',
                'gemini-1.0-pro-latest',
                'gemini-1.0-pro',
                'gemini-pro',
            ]
            
            # Try each model name
            for model_name in model_names:
                try:
                    model = genai.GenerativeModel(model_name)
                    # Try a simple test generation to verify it works
                    test_response = model.generate_content("test")
                    available_model = model_name
                    break
                except Exception:
                    continue
        
        if available_model is None:
            raise Exception(
                "❌ Could not find an available Gemini model.\n\n"
                "This might be due to:\n"
                "1. API key doesn't have access to Gemini models\n"
                "2. API key is invalid or expired\n"
                "3. Network/connectivity issues\n\n"
                "Please verify your API key at: https://makersuite.google.com/app/apikey\n"
                "And check available models at: https://ai.google.dev/models/gemini"
            )
        
        # Use the available model
        model = genai.GenerativeModel(available_model)
        
        prompt = f"""Analyze the following git diff and generate a concise, professional commit message.
        
The commit message should:
- Be clear and descriptive
- Follow conventional commit format if applicable
- Be no longer than 72 characters for the subject line
- Not include explanations or meta-commentary, just the commit message itself

Git diff:
{diff_text}

Commit message:"""
        
        response = model.generate_content(prompt)
        
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

