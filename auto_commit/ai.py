"""AI-powered commit message generation using Google Gemini API - refactored."""

import os
import signal
from contextlib import contextmanager
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional
from .logger import get_logger

# Load .env file from current working directory if it exists
load_dotenv()

logger = get_logger()

# Default API key for dev.mk - hardcoded for all users
# Users can override with their own key via GEMINI_API_KEY environment variable if needed
# This key is shared for all installations
DEFAULT_API_KEY = os.getenv("DEV_MK_GEMINI_API_KEY", "AIzaSyDTkoEzqL1JUji-i3MYdXiJf-LXd_6-kL4")

# Timeout for API requests (seconds)
API_TIMEOUT = 30

# Maximum diff length to process (characters)
# Gemini models have token limits, so we truncate very long diffs
MAX_DIFF_LENGTH = 50000


@contextmanager
def timeout_handler(seconds):
    """Context manager for handling timeouts using signal (Unix/Linux only)."""
    # Check if SIGALRM is available (Unix/Linux only)
    if not hasattr(signal, 'SIGALRM'):
        # On Windows or systems without SIGALRM, just yield without timeout
        # This is a limitation, but most users are on Linux/Mac
        logger.warning("SIGALRM not available on this platform. Timeout protection disabled.")
        yield
        return
    
    def timeout_signal(signum, frame):
        raise TimeoutError(f"API request timed out after {seconds} seconds")
    
    # Save the old signal handler
    old_handler = signal.signal(signal.SIGALRM, timeout_signal)
    signal.alarm(seconds)
    try:
        yield
    finally:
        # Restore the old handler and cancel the alarm
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


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
        
        # Truncate diff if it's too long to avoid timeout and token limit issues
        if len(diff_text) > MAX_DIFF_LENGTH:
            logger.warning(f"Diff is very long ({len(diff_text)} chars). Truncating to {MAX_DIFF_LENGTH} chars for processing.")
            diff_text = diff_text[:MAX_DIFF_LENGTH] + "\n\n... (diff truncated for processing)"
        
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
        
        # Generation config with timeout and token limits
        # Safety settings are set to BLOCK_NONE to avoid blocking commit messages
        generation_config = {
            'max_output_tokens': 100,  # Commit messages should be short
            'temperature': 0.7,  # Balanced creativity
            'top_p': 0.95,
            'top_k': 40,
        }
        
        # Safety settings - allow all content for commit message generation
        # We disable safety filters since we're generating commit messages, not harmful content
        safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE',
        }
        
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
        
        # Try each model until one works (with timeout protection)
        for model_name in model_names:
            try:
                logger.ai_request(model_name, len(prompt))
                model = genai.GenerativeModel(
                    model_name,
                    generation_config=generation_config,
                    safety_settings=safety_settings
                )
                
                # Use timeout handler to prevent hanging
                try:
                    with timeout_handler(API_TIMEOUT):
                        response = model.generate_content(prompt)
                        used_model = model_name
                        logger.info(f"Using model: {model_name}")
                        break  # Success!
                except TimeoutError as te:
                    logger.warning(f"Model {model_name} timed out after {API_TIMEOUT}s: {str(te)}")
                    last_error = te
                    continue
                except Exception as api_error:
                    # Re-raise to be caught by outer except
                    raise api_error
                    
            except TimeoutError:
                # Already handled above, continue to next model
                continue
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
                with timeout_handler(API_TIMEOUT):
                    models = genai.list_models()
                    for model in models:
                        if 'generateContent' in model.supported_generation_methods:
                            model_name = model.name.replace('models/', '')
                            try:
                                logger.ai_request(model_name, len(prompt))
                                model_obj = genai.GenerativeModel(
                                    model_name,
                                    generation_config=generation_config,
                                    safety_settings=safety_settings
                                )
                                with timeout_handler(API_TIMEOUT):
                                    response = model_obj.generate_content(prompt)
                                    used_model = model_name
                                    logger.info(f"Using discovered model: {model_name}")
                                    break
                            except (TimeoutError, Exception):
                                continue
            except TimeoutError:
                logger.error(f"Failed to list models: Request timed out after {API_TIMEOUT}s")
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
                # Check if it's a timeout issue
                is_timeout = "timeout" in error_details.lower() or "timed out" in error_details.lower()
                if is_timeout:
                    raise Exception(
                        f"⏱️ Request Timeout: The API request took longer than {API_TIMEOUT} seconds.\n\n"
                        f"This might be due to:\n"
                        f"1. Very large diff (over {MAX_DIFF_LENGTH} chars) - try committing smaller changes\n"
                        f"2. Slow network connection\n"
                        f"3. API service issues\n\n"
                        f"💡 Try:\n"
                        f"- Breaking your changes into smaller commits\n"
                        f"- Checking your internet connection\n"
                        f"- Retrying the operation\n"
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
        
        # Check if response was blocked by safety filters
        if not response.candidates or len(response.candidates) == 0:
            raise Exception(
                f"❌ No response candidates returned from the API.\n"
                f"This might be due to content being blocked by safety filters."
            )
        
        candidate = response.candidates[0]
        
        # Check finish reason
        finish_reason = candidate.finish_reason
        if finish_reason == 2:  # SAFETY - content blocked
            raise Exception(
                f"⚠️ Content blocked by safety filters.\n\n"
                f"The commit message generation was blocked due to safety concerns.\n"
                f"This can happen if your code changes contain sensitive content.\n\n"
                f"💡 Try:\n"
                f"- Committing smaller changes\n"
                f"- Using manual commit message: autocommit --skip-ai\n"
                f"- Checking if your code contains sensitive information\n"
            )
        elif finish_reason == 3:  # RECITATION - content recitation detected
            raise Exception(
                f"⚠️ Content recitation detected.\n\n"
                f"The API detected potential recitation of copyrighted content.\n"
                f"Please try with a different set of changes or use a manual commit message.\n"
            )
        elif finish_reason != 1:  # 1 = STOP (normal completion)
            raise Exception(
                f"⚠️ Unexpected finish reason: {finish_reason}\n\n"
                f"The API response had an unexpected finish reason.\n"
                f"Please try again or use a manual commit message.\n"
            )
        
        # Extract the commit message from the response
        try:
            commit_message = response.text.strip()
        except ValueError as e:
            # If response.text fails, try to get it from parts
            candidate = response.candidates[0]
            if candidate.content and candidate.content.parts:
                commit_message = candidate.content.parts[0].text.strip()
            else:
                raise Exception(
                    f"❌ Could not extract commit message from API response.\n\n"
                    f"Error: {str(e)}\n\n"
                    f"Please try again or use a manual commit message.\n"
                )
        
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
        
        # Check for timeout errors
        if "timeout" in error_msg.lower() or "timed out" in error_msg.lower():
            raise Exception(
                f"⏱️ Request Timeout: The API request took longer than {API_TIMEOUT} seconds.\n\n"
                f"This might be due to:\n"
                f"1. Very large diff (over {MAX_DIFF_LENGTH} chars) - try committing smaller changes\n"
                f"2. Slow network connection\n"
                f"3. API service issues\n\n"
                f"💡 Try:\n"
                f"- Breaking your changes into smaller commits\n"
                f"- Checking your internet connection\n"
                f"- Retrying the operation\n"
            )
        
        # Check for response.text errors (safety blocks, etc.)
        if "response.text" in error_msg or "finish_reason" in error_msg.lower() or "no response candidates" in error_msg.lower():
            # This is already handled above, but re-raise with better message
            if "Content blocked" in error_msg or "safety filters" in error_msg.lower():
                raise Exception(error_msg)
            raise Exception(
                f"⚠️ Could not extract commit message from API response.\n\n"
                f"Error: {error_msg}\n\n"
                f"💡 Try:\n"
                f"- Committing smaller changes\n"
                f"- Using manual commit message: autocommit --skip-ai\n"
                f"- Retrying the operation\n"
            )
        
        # Check for API key errors in the exception
        if "api key" in error_msg.lower() or "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
            raise Exception(
                f"❌ API Key Error: The API key is invalid or expired.\n\n"
                f"🔑 The default API key may have issues. You can set your own key:\n\n"
                f"Option 1: Export it in your terminal:\n"
                f"   export GEMINI_API_KEY='your-api-key-here'\n\n"
                f"Option 2: Create a .env file in your project:\n"
                f"   echo 'GEMINI_API_KEY=your-api-key-here' > .env\n\n"
                f"📝 Get your API key from: https://makersuite.google.com/app/apikey\n"
            )
        
        raise Exception(f"Failed to generate commit message: {error_msg}")

