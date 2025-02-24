import numpy as np

# define the input and output grids
examples = [
    {
        'input': np.array([
            [0, 9, 9, 1, 9, 9, 9],
            [0, 0, 9, 1, 9, 9, 0],
            [9, 0, 9, 1, 9, 9, 0],
            [0, 0, 0, 1, 9, 0, 0],
            [0, 9, 9, 1, 9, 9, 9]
        ]),
        'expected': np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0]
        ])
    },
    {
        'input': np.array([
            [0, 0, 0, 1, 9, 0, 0],
            [9, 0, 9, 1, 9, 9, 9],
            [0, 9, 9, 1, 9, 9, 9],
            [0, 0, 0, 1, 9, 9, 9],
            [0, 9, 9, 1, 9, 9, 9]
        ]),
        'expected': np.array([
            [0, 8, 8],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])
    },
    {
        'input': np.array([
            [9, 0, 0, 1, 9, 0, 9],
            [9, 0, 0, 1, 0, 9, 0],
            [9, 0, 0, 1, 9, 0, 0],
            [0, 9, 9, 1, 0, 9, 9],
            [0, 0, 9, 1, 0, 9, 0]
        ]),
        'expected': np.array([
            [0, 8, 0],
            [0, 8, 8],
            [0, 8, 8],
            [0, 8, 8],
            [0, 8, 8]
        ])
    },
   {
        'input': np.array([
            [0, 9, 9, 1, 9, 0, 9],
            [9, 0, 0, 1, 9, 0, 0],
            [9, 9, 9, 1, 9, 9, 9],
            [0, 9, 0, 1, 0, 0, 0],
            [9, 0, 0, 1, 9, 0, 0]
        ]),
        'expected': np.array([
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0],
            [8, 0, 8],
            [0, 8, 8]
        ])
    },
   {
        'input': np.array([
            [0, 9, 9, 1, 9, 0, 9],
            [9, 0, 9, 1, 9, 9, 9],
            [9, 9, 9, 1, 0, 0, 9],
            [9, 0, 0, 1, 9, 0, 0],
            [9, 9, 9, 1, 0, 0, 9]
        ]),
        'expected': np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 8, 8],
            [0, 0, 0]
        ])
    }
]

def find_blue_stripe_column(grid):
    """Finds the column index of the vertical blue stripe (color 1)."""
    for j in range(grid.shape[1]):
        if np.any(grid[:, j] == 1):
            return j
    return -1  # Return -1 if no blue stripe is found

def analyze_azure_placement(input_grid, expected_grid, blue_stripe_col):
    """Analyzes the placement of azure pixels in relation to the blue stripe."""
    azure_positions = []
    for i in range(expected_grid.shape[0]):
        for j in range(expected_grid.shape[1]):
            if expected_grid[i, j] == 8:
                azure_positions.append((i, j))

    print(f"  Azure Pixel Positions: {azure_positions}")

    # Calculate relative positions
    relative_positions = []
    input_height = input_grid.shape[0]
    input_width  = input_grid.shape[1]

    for row, col in azure_positions:
        rel_row = row - (input_height -1 )/2
        rel_col = col - (blue_stripe_col- (input_width-1)/2) + .5
        relative_positions.append((rel_row,rel_col))

    print(f"  Relative Positions (row, col) to center: {relative_positions}")

for i, example in enumerate(examples):
    input_grid = example['input']
    expected_grid = example['expected']
    blue_stripe_col = find_blue_stripe_column(input_grid)
    print(f"Example {i+1}:")
    print(f"  Blue Stripe Column: {blue_stripe_col}")
    analyze_azure_placement(input_grid, expected_grid, blue_stripe_col)