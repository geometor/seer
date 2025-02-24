def get_dimensions(grid):
    return len(grid), len(grid[0]) if grid else 0

# Example Data (from the prompt)
examples = [
    {
        "input": [
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 0, 0, 0],
            [3, 0, 0, 3],
            [0, 0, 0, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 0, 1],
        ],
        "expected_output": [
            [2, 2, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
        ],
    },
    {
        "input": [
            [3, 3, 3, 3],
            [0, 3, 3, 0],
            [0, 0, 3, 3],
            [3, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 1],
        ],
        "expected_output": [
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 2, 2, 0],
        ],
    },
    {
        "input": [
            [0, 3, 3, 0],
            [0, 3, 0, 3],
            [0, 0, 3, 0],
            [3, 3, 3, 3],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
        ],
        "expected_output": [
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 2],
            [0, 0, 0, 0],
        ],
    },
    {
        "input": [
            [3, 3, 3, 3],
            [3, 0, 0, 0],
            [3, 0, 3, 3],
            [3, 3, 0, 3],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1],
        ],
        "expected_output": [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0],
        ],
    },
]

# Analyze each example
for i, example in enumerate(examples):
  input_dims = get_dimensions(example["input"])
  expected_output_dims = get_dimensions(example["expected_output"])
  actual_output = transform(example["input"])
  actual_output_dims = get_dimensions(actual_output)

  print(f"Example {i+1}:")
  print(f"  Input Dimensions: {input_dims}")
  print(f"  Expected Output Dimensions: {expected_output_dims}")
  print(f"  Actual Output Dimensions: {actual_output_dims}")
  print(f"  Dimensions Match: {expected_output_dims == actual_output_dims}")