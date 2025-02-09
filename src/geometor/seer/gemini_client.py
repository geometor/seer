"""Google Gemini Model Interface for Seer

Provides a streamlined interface to Google's Gemini model, configured specifically
for the dialogue-based ARC solving approach.

Features:
    
- Structured conversation management
- Code execution capabilities
- Function calling support
- System instruction integration
- Error handling and retry logic

The client is designed to maintain consistent context while allowing for
flexible interaction patterns including code exploration and function calls.
"""

import os
from pathlib import Path
import google.generativeai as genai
from google.api_core import retry
from typing import List, Any, Dict, Callable
#  from .client import Client


class GeminiClient():
    """
    Initialize the GeminiClient with model configuration and system instructions.

    parameters
    ----------
    model_name : :class:`python:str`
        Name of the Gemini model to use.
    instructions_file : :class:`python:str`
        Path to the instructions file.
    """

    def __init__(self, model_name: str, instructions: str):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model_name = model_name

        #  script_dir = Path(__file__).parent.absolute()
        #  instructions_file = script_dir / instructions_file

        #  with open(instructions_file, "r") as f:
            #  instruction = f.read().strip()

        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=instructions,
        )

    def generate_content(self, prompt: List[str], tools: List[Callable] = None) -> Any:
        """
        Generate content from the Gemini model based on the provided prompt.

        parameters
        ----------
        prompt : list
            The prompt to send to the model.
        tools : str or list
            Optional tools or functions the model can use.
            "code_execution"

        returns
        -------
        response : GeminiResponse
            the model's response.

        """
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
