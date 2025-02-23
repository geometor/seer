import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.
    """
    input_array = np.array(input_grid)
    output_array = np.rot90(input_array, 2)  # Rotate by 90 degrees twice
    output_grid = output_array.tolist()
    return output_grid

# Example data provided in previous turns
train_set = [
    {
        "input": [[2, 2, 1], [2, 1, 2], [2, 8, 1]],
        "output": [[1, 8, 2], [2, 1, 2], [1, 2, 2]],
    },
    {
        "input": [[9, 2, 4], [2, 4, 4], [2, 9, 2]],
        "output": [[2, 9, 2], [4, 4, 2], [4, 2, 9]],
    },
    {
        "input": [[8, 8, 8], [5, 5, 8], [8, 5, 5]],
        "output": [[5, 5, 8], [8, 5, 5], [8, 8, 8]],
    },
    {
        "input": [[3, 2, 9], [9, 9, 9], [2, 3, 3]],
        "output": [[3, 3, 2], [9, 9, 9], [9, 2, 3]],
    },
]

# Function to check if two grids are equal
def grids_equal(grid1, grid2):
    return grid1 == grid2

# Test against the train set
for i, example in enumerate(train_set):
    transformed_output = transform(example["input"])
    match = grids_equal(transformed_output, example["output"])
    print(f"Example {i + 1}:")
    print(f"Transformed Output:\n{transformed_output}")
    print(f"Expected Output:\n{example['output']}")
    print(f"Match: {match}")
    print("---")
