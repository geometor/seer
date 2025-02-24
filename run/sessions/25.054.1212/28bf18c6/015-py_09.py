import numpy as np
from collections import Counter

def analyze_grid(grid):
    """Analyzes a single grid and returns its dimensions and color counts."""
    grid_array = np.array(grid)
    height, width = grid_array.shape
    color_counts = Counter(grid_array.flatten())
    return {
        "height": height,
        "width": width,
        "color_counts": color_counts,
    }

def analyze_example(input_grid, output_grid):
    """Analyzes an input-output pair."""
    input_analysis = analyze_grid(input_grid)
    output_analysis = analyze_grid(output_grid)
    return {
        "input": input_analysis,
        "output": output_analysis,
    }


# Example data (replace with your actual data)
examples = [
    (
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 8, 0, 0, 0, 0, 0],
         [0, 0, 8, 0, 0, 0, 0, 0],
         [0, 8, 8, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]],
        [[8, 8, 0, 8, 8, 0],
         [0, 8, 0, 0, 8, 0],
         [8, 8, 8, 8, 8, 8]]
    ),
    (
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 2, 2, 2, 0, 0, 0],
         [0, 0, 2, 2, 0, 0, 0, 0]],
        [[0, 2, 0, 0, 2, 0],
         [2, 2, 2, 2, 2, 2],
         [2, 2, 0, 2, 2, 0]]
    ),
    (
        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]],
        [[0, 1, 1, 0, 1, 1],
         [1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0]]
    )
]

analysis_results = [analyze_example(inp, out) for inp, out in examples]
print(analysis_results)