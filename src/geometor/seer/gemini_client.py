"""Client for interacting with the Google Gemini model."""

import os
from pathlib import Path
#  from google import genai
#  from google.genai import types

import google.generativeai as genai
from google.api_core import retry
from typing import List, Any, Dict, Callable


class GeminiClient:
    def __init__(self, config: dict, role: str):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

        role_config = config["roles"][role]  # Access roles dictionary
        self.model_name = role_config["model_name"]

        with open(role_config["system_context_file"], "r") as f:
            system_context = f.read().strip()
        with open(config["task_context_file"], "r") as f:
            task_context = f.read().strip()

        instructions = f"{system_context}\n\n{task_context}"

        self.model = genai.GenerativeModel(
            model_name=role_config["model_name"],
            generation_config=role_config["generation_config"],
            system_instruction=instructions,  # Corrected line
        )

    def generate_content(self, prompt: List[str], tools: List[Callable] = None) -> Any:
        try:
            if tools and tools != "code_execution":
                tool_config = {"function_calling_config": {"mode": "ANY"}}
            else:
                tool_config = None

            response = self.model.generate_content(
                prompt,
                tools=tools,
                request_options={"retry": retry.Retry()},
                tool_config=tool_config,
            )
            return response
        except Exception as e:
            # TODO: Handle exceptions as needed
            raise e

