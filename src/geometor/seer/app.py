"""
run the main app
"""
from .seer import Seer


def run() -> None:
    reply = Seer().run()
    print(reply)
