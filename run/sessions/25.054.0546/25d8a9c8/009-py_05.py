import numpy as np
from collections import Counter

def analyze_examples(examples):
    """Analyzes input-output pairs to determine color mappings and errors."""

    all_input_colors = Counter()
    all_output_colors = Counter()
    color_mappings = {}
    error_details = []
    pixel_diffs = {}


    for idx, (input_grid, expected_output) in enumerate(examples):

        input_grid = np.array(input_grid)
        expected_output = np.array(expected_output)

        all_input_colors.update(input_grid.flatten())
        all_output_colors.update(expected_output.flatten())

        # Determine color mappings
        for color in np.unique(input_grid):
            corresponding_output_colors = expected_output[input_grid == color]
            if len(np.unique(corresponding_output_colors)) == 1:
                color_mappings[color] = corresponding_output_colors[0]
            else:
                # Handle cases where a single input color maps to multiple output colors
                color_mappings[color] = tuple(np.unique(corresponding_output_colors))  # Store as a tuple

        # pixels that don't match
        diff = input_grid != expected_output
        if diff.any():
            # record which colors where incorrect
            pixel_diffs[f'{idx}'] = diff.sum()

            rows, cols = np.where(diff)
            incorrect_pixels = []
            for r, c in zip(rows, cols):
                incorrect_pixels.append(
                    {
                        "row": int(r),
                        "col": int(c),
                        "input_color": int(input_grid[r, c]),
                        "expected_color": int(expected_output[r, c]),
                    }
                )
            error_details.append(
                {"example_index": idx, "incorrect_pixels": incorrect_pixels}
            )


    print("Color Mapping Report:")
    for in_color, out_color in color_mappings.items():
        print(f"  Input Color: {in_color} -> Output Color: {out_color}")
    print("\nError Report:")
    for error in error_details:
        print(f"Example {error['example_index'] + 1}:")
        for pixel_error in error["incorrect_pixels"]:
            print(
                f"  Row: {pixel_error['row']}, Col: {pixel_error['col']}, "
                f"Input: {pixel_error['input_color']}, Expected: {pixel_error['expected_color']}"
            )
    print(f'\n\nPixel Diff Report {pixel_diffs}')

# Example data (replace with actual data loading)
examples = [
    (
        [[4, 4, 4], [2, 3, 2], [2, 3, 3]],
        [[4, 4, 4], [2, 0, 2], [2, 0, 0]],
    ),  # Example 1 - corrected output
    (
        [[7, 3, 3], [6, 6, 6], [3, 7, 7]],
        [[0, 0, 0], [5, 5, 5], [0, 0, 0]],
    ),  # Example 2
    (
       [[2, 9, 2], [4, 4, 4], [9, 9, 9]],
       [[2, 9, 2], [4, 4, 4], [9, 9, 9]]
    ),  # Example 3 corrected output
    (
       [[2, 2, 4], [2, 2, 4], [1, 1, 1]],
       [[2, 2, 4], [2, 2, 4], [1, 1, 1]]
    ),  # Example 4 corrected output
]

analyze_examples(examples)
