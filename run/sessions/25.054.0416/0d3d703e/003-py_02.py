import numpy as np

# Data from the provided examples
examples = [
    {
        "input": np.array([[3, 1, 2], [3, 1, 2], [3, 1, 2]]),
        "expected": np.array([[4, 5, 6], [4, 5, 6], [4, 5, 6]]),
    },
    {
        "input": np.array([[2, 3, 8], [2, 3, 8], [2, 3, 8]]),
        "expected": np.array([[6, 4, 9], [6, 4, 9], [6, 4, 9]]),
    },
    {
        "input": np.array([[5, 8, 6], [5, 8, 6], [5, 8, 6]]),
        "expected": np.array([[1, 9, 2], [1, 9, 2], [1, 9, 2]]),
    },
    {
        "input": np.array([[9, 4, 2], [9, 4, 2], [9, 4, 2]]),
        "expected": np.array([[8, 3, 6], [8, 3, 6], [8, 3, 6]]),
    },
]

# Create a mapping dictionary
value_mapping = {}

# Populate the mapping dictionary
for example in examples:
    for i in range(example["input"].shape[0]):
        for j in range(example["input"].shape[1]):
            input_val = example["input"][i, j]
            expected_val = example["expected"][i, j]
            if input_val not in value_mapping:
                value_mapping[input_val] = set()
            value_mapping[input_val].add(expected_val)

# Print the mapping, sorted by input value
print("Input-Output Value Mapping:")
for input_val in sorted(value_mapping.keys()):
    print(f"  {input_val}: {sorted(list(value_mapping[input_val]))}")
