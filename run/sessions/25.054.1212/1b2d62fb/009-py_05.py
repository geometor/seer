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

for i, example in enumerate(examples):
    input_grid = example['input']
    expected_grid = example['expected']
    blue_stripe_col = find_blue_stripe_column(input_grid)
    print(f"Example {i+1}:")
    print(f"  Blue Stripe Column: {blue_stripe_col}")
