"""The package entry point into the application."""

from .app import run

if __name__ == "__main__":
    run()"""
Main entry point for running the Seer application.
"""

from geometor.seer.seer import Seer
from geometor.seer.gemini_client import GeminiClient

def main():
    """
    Initializes the Seer and GeminiClient and demonstrates generating content.
    """
    model_name = "gemini-pro"  # Replace with your desired Gemini model
    api_key = "YOUR_API_KEY" # Set your API key in the environment

    client = GeminiClient(model_name, api_key)
    seer = Seer(client)

    prompt = ["Tell me a story about a robot learning to solve ARC puzzles."]
    response = seer.run(prompt)

    print("Response from Seer:")
    print(response)

if __name__ == "__main__":
    main()
