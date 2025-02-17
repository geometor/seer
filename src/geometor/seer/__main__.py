"""
Main entry point for the Seer application.

This module provides the command-line interface for running the Seer. It initializes
the Seer and GeminiClient, and demonstrates the basic workflow of generating content.
"""

from geometor.seer.seer import Seer
from geometor.seer.gemini_client import GeminiClient

def main():
    """
    Initializes the Seer and GeminiClient and demonstrates generating content.
    """
    model_name = "gemini-pro"  # Replace with your desired Gemini model
    seer = Seer()

    #  prompt = "Tell me a story about a robot learning to solve ARC puzzles."
    #  response = seer.run(prompt)

    #  print(f"Response from Seer: {response}")

if __name__ == "__main__":
    main()
