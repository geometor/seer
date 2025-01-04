"""
run the main app
"""
from .seer import Seer


def run() -> None:
    seer = Seer()
    reply = seer.run()
    print(reply)
