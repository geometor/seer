import numpy as np

# Provided input and expected output grids for all examples
examples = [
    {
        "input": np.array([[0, 0, 5], [0, 5, 0], [5, 0, 0]]),
        "expected": np.array([[3, 3, 3], [4, 4, 4], [2, 2, 2]]),
    },
    {
        "input": np.array([[0, 0, 5], [0, 0, 5], [0, 0, 5]]),
        "expected": np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
    },
    {
        "input": np.array([[5, 0, 0], [0, 5, 0], [5, 0, 0]]),
        "expected": np.array([[2, 2, 2], [4, 4, 4], [2, 2, 2]]),
    },
    {
        "input": np.array([[0, 5, 0], [0, 0, 5], [0, 5, 0]]),
        "expected": np.array([[4, 4, 4], [3, 3, 3], [4, 4, 4]]),
    },
]

# Analyze each example
for i, example in enumerate(examples):
    input_grid = example["input"]
    expected_output = example["expected"]
    print(f"Example {i+1}:")
    print(f"Input:\n{input_grid}")
    print(f"Expected Output:\n{expected_output}")

    for row in range(input_grid.shape[0]):
      for col in range(input_grid.shape[1]):
        input_val = input_grid[row,col]
        output_val = expected_output[row, col]
        print(f"  Input value {input_val} at ({row},{col}) maps to output value {output_val}")