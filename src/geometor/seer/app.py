"""
run the main app
"""
from .seer import Seer
from .client import Client


def run() -> None:
    seer = Seer()
    reply = seer.run()
    print(reply)
