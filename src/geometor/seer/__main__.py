"""
Main entry point for running the Seer application.
"""

from geometor.seer.seer import Seer
from geometor.seer.gemini_client import GeminiClient

def main():
    """
    Initializes the Seer and GeminiClient and demonstrates generating content.
    """
    model_name = "gemini-pro"  # Replace with your desired Gemini model
    client = GeminiClient(model_name)
    seer = Seer(client)

    prompt = "Tell me a story about a robot learning to solve ARC puzzles."
    response = seer.run(prompt)

    print(f"Response from Seer: {response}")

if __name__ == "__main__":
    main()
"""The package entry point into the application."""

from .app import run

if __name__ == "__main__":
    run()
