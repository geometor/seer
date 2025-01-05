from rich import print
from geometor.seer.app import Seer


def run_demo():
    seer = Seer()
    print(f"Seer initialized")
    prompt = "Solve this simple puzzle."
    result = seer.run(prompt)
    print(f"Seer result: {result}")

if __name__ == "__main__":
    run_demo()
