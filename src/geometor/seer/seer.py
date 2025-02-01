"""
seer
"""

class Seer:
    """
    The Seer class.
    """
    def __init__(self, client):
        self.client = client

    def run(self, prompt):
        return self.client.generate_content(prompt)
