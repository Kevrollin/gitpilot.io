"""AI-powered commit message generation using Google Gemini API - refactored."""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional
from .logger import get_logger

# Load .env file from current working directory if it exists
load_dotenv()

logger = get_logger()

# Default API key for dev.mk - shared key with rate limits
# Users can override with their own key via GEMINI_API_KEY environment variable
# WARNING: This is a shared key. For production use, get your own key from:
# https://makersuite.google.com/app/apikey
DEFAULT_API_KEY = os.getenv("DEV_MK_GEMINI_API_KEY", "AIzaSyDlRRsBadF_FmGwyhNeZqYubEVEeACDrrUs")


def generate_commit_message(diff_text: str, callback=None) -> str:
    """
    Generate a commit message from git diff using Gemini API.
    
    Args:
        diff_text: The git diff text to analyze
        callback: Optional callback function for progress updates
        
    Returns:
        A clean commit message string
        
    Raises:
        ValueError: If GEMINI_API_KEY is not set
        Exception: If API call fails
    """
    # Try to load API key in order of priority:
    # 1. User's own key (GEMINI_API_KEY)
    # 2. Default shared key (DEV_MK_GEMINI_API_KEY)
    api_key = os.getenv("GEMINI_API_KEY") or DEFAULT_API_KEY
    
    using_default_key = not os.getenv("GEMINI_API_KEY") and DEFAULT_API_KEY
    
    if not api_key:
        error_msg = (
            "GEMINI_API_KEY not found\n\n"
            "To set it up, use one of these methods:\n\n"
            "Option 1: Create a .env file in your project directory:\n"
            "   echo 'GEMINI_API_KEY=your-api-key-here' > .env\n\n"
            "Option 2: Export it as an environment variable:\n"
            "   export GEMINI_API_KEY='your-api-key-here'\n\n"
            "Option 3: Add it to ~/.bashrc or ~/.zshrc for persistence:\n"
            "   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc\n"
            "   source ~/.bashrc\n\n"
            "Get your API key from: https://makersuite.google.com/app/apikey\n\n"
            "Note: For unlimited usage, get your own API key. The default key has rate limits."
        )
        raise ValueError(error_msg)
    
    if using_default_key:
        logger.warning("Using default shared API key. For unlimited usage, set your own GEMINI_API_KEY")
    
    try:
        genai.configure(api_key=api_key)
        logger.info("Configured Gemini API")
        
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
        
        # Try each model until one works (silently in background)
        for model_name in model_names:
            try:
                logger.ai_request(model_name, len(prompt))
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                used_model = model_name
                logger.info(f"Using model: {model_name}")
                break  # Success!
            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                # If it's a 404/model not found, try next model
                if "404" in error_str or "not found" in error_str or "not supported" in error_str:
                    logger.debug(f"Model {model_name} not available: {error_str[:100]}")
                    continue
                # For other errors, log and try next model
                logger.warning(f"Error with model {model_name}: {str(e)[:100]}")
                continue
        
        if response is None:
            # If all models failed, try listing available models as last resort
            try:
                logger.debug("Discovering available models...")
                models = genai.list_models()
                for model in models:
                    if 'generateContent' in model.supported_generation_methods:
                        model_name = model.name.replace('models/', '')
                        try:
                            logger.ai_request(model_name, len(prompt))
                            model_obj = genai.GenerativeModel(model_name)
                            response = model_obj.generate_content(prompt)
                            used_model = model_name
                            logger.info(f"Using discovered model: {model_name}")
                            break
                        except Exception:
                            continue
            except Exception as list_error:
                logger.error(f"Failed to list models: {str(list_error)}")
        
        if response is None:
            error_details = str(last_error) if last_error else "Unknown error"
            logger.error(f"Could not find available Gemini model: {error_details}")
            
            # Check if it's an API key issue
            is_api_key_error = "api key" in error_details.lower() or "API_KEY_INVALID" in error_details or "invalid" in error_details.lower()
            
            if is_api_key_error:
                raise Exception(
                    f"❌ API Key Error: The API key is invalid or expired.\n\n"
                    f"🔑 To fix this, set your own Gemini API key:\n\n"
                    f"Option 1 (Recommended): Export it in your terminal:\n"
                    f"   export GEMINI_API_KEY='your-api-key-here'\n\n"
                    f"Option 2: Create a .env file in your project:\n"
                    f"   echo 'GEMINI_API_KEY=your-api-key-here' > .env\n\n"
                    f"Option 3: Add to your shell config (~/.bashrc or ~/.zshrc):\n"
                    f"   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc\n"
                    f"   source ~/.bashrc\n\n"
                    f"📝 Get your API key from: https://makersuite.google.com/app/apikey\n\n"
                    f"💡 The default shared key may have expired. Setting your own key ensures unlimited usage.\n"
                )
            else:
            raise Exception(
                f"Could not find an available Gemini model.\n\n"
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
        
        logger.ai_response(commit_message)
        return commit_message
        
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Failed to generate commit message: {error_msg}")
        
        # If error already contains helpful instructions, re-raise as-is
        if "❌ API Key Error" in error_msg or "To fix this, set your own" in error_msg:
            raise Exception(error_msg)
        
        if "404" in error_msg or "not found" in error_msg.lower():
            raise Exception(
                f"Gemini model not found. This might be due to:\n"
                f"  1. API key doesn't have access to the model\n"
                f"  2. Model name has changed\n"
                f"  3. API version issue\n\n"
                f"Error details: {error_msg}\n\n"
                f"Please check: https://ai.google.dev/models/gemini"
            )
        
        # Check for API key errors in the exception
        if "api key" in error_msg.lower() or "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
            raise Exception(
                f"❌ API Key Error: The API key is invalid or expired.\n\n"
                f"🔑 To fix this, set your own Gemini API key:\n\n"
                f"Option 1 (Recommended): Export it in your terminal:\n"
                f"   export GEMINI_API_KEY='your-api-key-here'\n\n"
                f"Option 2: Create a .env file in your project:\n"
                f"   echo 'GEMINI_API_KEY=your-api-key-here' > .env\n\n"
                f"Option 3: Add to your shell config (~/.bashrc or ~/.zshrc):\n"
                f"   echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc\n"
                f"   source ~/.bashrc\n\n"
                f"📝 Get your API key from: https://makersuite.google.com/app/apikey\n\n"
                f"💡 The default shared key may have expired. Setting your own key ensures unlimited usage.\n"
            )
        
        raise Exception(f"Failed to generate commit message: {error_msg}")

