import numpy as np

# Define the examples as numpy arrays
examples = [
    {
        "input": np.array([[2, 0, 2], [0, 2, 0], [2, 0, 2]]),
        "output": np.array([[1]]),
        "red_count": 5 #Manually calculated at first to break circular dependency.
    },
    {
        "input": np.array([[2, 0, 0], [2, 0, 0], [0, 2, 0]]),
        "output": np.array([[7]]),
        "red_count": 3
    },
    {
        "input": np.array([[2, 0, 2], [2, 0, 2], [2, 0, 2]]),
        "output": np.array([[1]]),
        "red_count": 6
    },
    {
        "input": np.array([[0, 0, 0], [2, 0, 2], [0, 0, 0]]),
        "output": np.array([[1]]),
        "red_count": 2
    },
    {
        "input": np.array([[2, 2, 0], [0, 2, 2], [0, 0, 0]]),
        "output": np.array([[7]]),
        "red_count": 4
    },
    {
        "input": np.array([[2, 2, 0], [0, 2, 0], [0, 0, 0]]),
        "output": np.array([[7]]),
        "red_count": 3
    },
]

# Update metrics
for example in examples:
  red_count = np.sum(example["input"] == 2)
  example["red_count"] = red_count
  print(f"red pixels: {red_count}, output: {example['output'][0][0]}, {'Odd' if red_count % 2 != 0 else 'Even'}")
