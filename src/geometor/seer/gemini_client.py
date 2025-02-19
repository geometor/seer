"""Client for interacting with the Google Gemini model."""

import os
from pathlib import Path
import google.generativeai as genai
from google.api_core import retry
from typing import List, Any, Dict, Callable


class GeminiClient:
    def __init__(self, config: dict, instructions: str):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        #  self.model_name = model_name
        self.model_name = config["model_name"]

        self.model = genai.GenerativeModel(
            model_name=config["model_name"],
            generation_config=config["generation_config"],
            system_instruction=instructions,
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
