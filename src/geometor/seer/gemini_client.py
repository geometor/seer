"""Client for interacting with the Google Gemini model."""

import os
from pathlib import Path

import google.generativeai as genai
import google.generativeai as genai
from google.api_core import retry
from typing import List, Any, Dict, Callable, Union

# Import the new Config class and potential error
from geometor.seer.config import Config, ConfigError


class GeminiClient:
    # Change type hint for config from dict to Config
    def __init__(self, config: Config, role: str):
        """
        Initializes the GeminiClient using a Config object.

        Args:
            config: The loaded Config object.
            role: The name of the role this client represents (e.g., 'dreamer', 'coder').

        Raises:
            ConfigError: If required configuration for the role is missing.
            ValueError: If the GEMINI_API_KEY environment variable is not set.
            RuntimeError: If the GenerativeModel fails to initialize.
        """
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            # More specific error for missing API key
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        genai.configure(api_key=api_key)

        # Access role-specific configuration from the Config object
        role_config = config.roles.get(role)
        if not role_config or not isinstance(role_config, dict):
            raise ConfigError(f"Configuration for role '{role}' not found or invalid in config.")

        self.model_name = role_config.get("model_name")
        if not self.model_name:
            raise ConfigError(f"Missing 'model_name' for role '{role}' in configuration.")

        # Access the pre-loaded system context content for the specific role
        role_system_context = role_config.get("system_context_content", "") # Default to empty string
        if not role_system_context:
            print(f"Warning: Role-specific 'system_context_content' not found or empty for role '{role}'.")

        # Access the pre-loaded general task context content from the Config object
        general_task_context = config.task_context # Access via property, defaults to ""
        if not general_task_context:
             print(f"Warning: General 'task_context_content' not found or empty in config.")

        # Combine role-specific system context and general task context
        # Add a separator for clarity if both exist
        combined_system_instruction = role_system_context
        if role_system_context and general_task_context:
            combined_system_instruction += "\n\n---\n\n" # Add a separator
        combined_system_instruction += general_task_context

        # Access generation_config
        generation_config = role_config.get("generation_config")
        if not generation_config:
            # Provide default or raise error if required
            print(f"Warning: 'generation_config' not found for role '{role}'. Using default generation settings.")
            generation_config = None # Let the library use its defaults
            # raise ConfigError(f"Missing 'generation_config' for role '{role}' in configuration.")


        # Task context is generally handled by the Seer when building the prompt,
        # not usually part of the core system instruction for the model itself.
        # We don't need to access config.task_context here.

        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=generation_config, # Pass the loaded generation config
                system_instruction=combined_system_instruction, # Pass the combined context
                # safety_settings=... # Add safety_settings from config if defined
            )
        except Exception as e:
            # Catch potential errors during model initialization
            raise RuntimeError(f"Failed to initialize GenerativeModel for role '{role}': {e}") from e


    # No changes needed in generate_content itself, as it receives the full prompt
    # from the caller (Seer), which should incorporate task context if needed.
    def generate_content(self, prompt: List[Any], tools: Union[List[Callable], str, None] = None) -> Any:
        """
        Generates content using the configured Gemini model.

        Args:
            prompt: The list of content parts forming the prompt (can include text, images).
            tools: Optional list of functions or the string "code_execution".

        Returns:
            The response object from the Gemini API.

        Raises:
            Exception: Propagates exceptions from the API call.
        """
        try:
            tool_config = None
            actual_tools = None

            if tools == "code_execution":
                # Enable the code execution tool
                # Note: The exact way to enable this might change. Refer to latest genai docs.
                # This assumes a basic enablement.
                # If using specific retrievers, configure Tool.from_retrieval_basis accordingly.
                # For simple execution, just enabling might be enough via model config or here.
                # Let's try enabling it directly if the API supports it this way.
                # If not, model initialization or a Tool object might be needed.
                # For now, let's assume passing the string might be handled internally
                # or we prepare a basic Tool object.
                # Creating a basic ExecutableCode tool part:
                # actual_tools = [genai.Tool(executable_code=genai.ExecutableCode())]
                # Or rely on the model's built-in capability if configured.
                # Let's pass the string and see if the API handles it, common in some versions.
                actual_tools = tools # Pass the string directly for now

            elif isinstance(tools, list) and tools:
                # Assume it's a list of functions for function calling
                actual_tools = tools # Pass the list directly
                tool_config = {"function_calling_config": {"mode": "ANY"}}
            # else: tools is None or an empty list, no tools/tool_config needed


            response = self.model.generate_content(
                prompt,
                tools=actual_tools, # Pass the prepared tools list/object or string
                request_options={"retry": retry.Retry()},
                tool_config=tool_config, # Pass the generated tool_config
            )
            return response
        except Exception as e:
            # TODO: Consider more specific error logging/handling here
            print(f"Error during Gemini API call for role '{self.model_name}': {e}") # Basic logging
            # Consider logging the prompt length/type for debugging
            # print(f"Prompt details: {len(prompt)} parts, types: {[type(p) for p in prompt]}")
            raise # Re-raise the exception for the caller to handle

