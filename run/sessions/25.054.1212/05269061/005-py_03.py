import numpy as np
from typing import List, Tuple

def analyze_example(input_grid: List[List[int]], expected_output: List[List[int]]) -> dict:
    """Analyzes a single example and provides metrics."""

    input_array = np.array(input_grid)
    expected_output_array = np.array(expected_output)

    # Basic size checks
    input_shape = input_array.shape
    output_shape = expected_output_array.shape
    size_correct = input_shape == output_shape

    # Color palette analysis (focus on non-zero pixels)
    input_colors = set(np.unique(input_array[input_array != 0]))
    output_colors = set(np.unique(expected_output_array[expected_output_array != 0]))
    color_palette_correct = input_colors == output_colors

    # Pixel counts (focus on non-zero pixels)
    input_counts = {color: np.sum(input_array == color) for color in input_colors}
    output_counts = {color: np.sum(expected_output_array == color) for color in output_colors}
    correct_pixel_counts = input_counts == output_counts

    return {
        "input_shape": input_shape,
        "output_shape": output_shape,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "input_colors": input_colors,
        "output_colors": output_colors,
        "input_counts": input_counts,
        "output_counts": output_counts
    }

# Example data (replace with actual examples from the task)
examples = [
    (
        [[2, 8, 3, 0, 0, 0, 0],
         [8, 3, 0, 0, 0, 0, 0],
         [3, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]],
        [[2, 8, 3, 2, 8, 3, 2],
         [8, 3, 2, 8, 3, 2, 8],
         [3, 2, 8, 3, 2, 8, 3],
         [2, 8, 3, 2, 8, 3, 2],
         [8, 3, 2, 8, 3, 2, 8],
         [3, 2, 8, 3, 2, 8, 3],
         [2, 8, 3, 2, 8, 3, 2]]
    ),
     (
        [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 2],
         [0, 0, 0, 0, 1, 2, 4],
         [0, 0, 0, 1, 2, 4, 0],
         [0, 0, 1, 2, 4, 0, 0]],
        [[2, 4, 1, 2, 4, 1, 2],
         [4, 1, 2, 4, 1, 2, 4],
         [1, 2, 4, 1, 2, 4, 1],
         [2, 4, 1, 2, 4, 1, 2],
         [4, 1, 2, 4, 1, 2, 4],
         [1, 2, 4, 1, 2, 4, 1],
         [2, 4, 1, 2, 4, 1, 2]]
    ),
    (
        [[0, 0, 0, 0, 8, 3, 0],
         [0, 0, 0, 8, 3, 0, 0],
         [0, 0, 8, 3, 0, 0, 0],
         [0, 8, 3, 0, 0, 0, 4],
         [8, 3, 0, 0, 0, 4, 0],
         [3, 0, 0, 0, 4, 0, 0],
         [0, 0, 0, 4, 0, 0, 0]],
        [[4, 8, 3, 4, 8, 3, 4],
         [8, 3, 4, 8, 3, 4, 8],
         [3, 4, 8, 3, 4, 8, 3],
         [4, 8, 3, 4, 8, 3, 4],
         [8, 3, 4, 8, 3, 4, 8],
         [3, 4, 8, 3, 4, 8, 3],
         [4, 8, 3, 4, 8, 3, 4]]
    )
]

# Analyze each example
results = [analyze_example(input_grid, expected_output) for input_grid, expected_output in examples]

# Print results
for i, result in enumerate(results):
    print(f"Example {i+1}:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print("-" * 20)