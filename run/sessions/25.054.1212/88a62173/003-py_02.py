import numpy as np

def get_grid_properties(grid):
    grid = np.array(grid)
    height, width = grid.shape
    unique_colors = np.unique(grid)
    color_counts = {color: np.count_nonzero(grid == color) for color in unique_colors}
    top_left_2x2 = grid[0:2, 0:2].tolist()

    return {
        "height": height,
        "width": width,
        "unique_colors": unique_colors.tolist(),
        "color_counts": color_counts,
        "top_left_2x2": top_left_2x2,
    }

# Example Inputs and Outputs (from the prompt)
examples = [
    {
        "input": [
            [0, 2, 0, 0, 2],
            [2, 2, 0, 2, 2],
            [0, 0, 0, 0, 0],
            [0, 2, 0, 2, 2],
            [2, 2, 0, 2, 0]
        ],
        "output": [
            [2, 2],
            [2, 0]
        ]
    },
    {
        "input": [
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 0, 0, 1]
        ],
        "output": [
            [1, 0],
            [0, 1]
        ]
    },
    {
        "input": [
            [8, 8, 0, 0, 8],
            [8, 0, 0, 8, 0],
            [0, 0, 0, 0, 0],
            [8, 8, 0, 8, 8],
            [8, 0, 0, 8, 0]
        ],
        "output": [
            [8, 8],
            [8, 0]
        ]
    }
]

# Analyze each example
for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    input_props = get_grid_properties(example["input"])
    output_props = get_grid_properties(example["output"])
    print("Input Properties:", input_props)
    print("Output Properties:", output_props)
    print("-" * 20)
