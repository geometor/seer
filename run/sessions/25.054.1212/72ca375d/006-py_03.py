"""
1.  Determine the Target Color: Examine the *output* grid. The target color is usually the most prominent or perhaps the *only* color present in the output. Handle the edge case of an empty output grid, returning an empty grid as the result.
2.  Locate Bounding Box in Input: Within the *input* grid, find the smallest rectangular region (bounding box) that contains all pixels of the target color identified in Step 1. If the target color is not found, return an empty grid.
3.  Extract the Region:** Create a new grid containing only the pixels within the bounding box found in the input grid. This extracted region is the transformed output.
"""

import numpy as np

def find_bounding_box(grid, target_color):
    """
    Finds the bounding box of a target color in a grid.
    Returns (min_row, min_col, max_row, max_col)
    """
    rows, cols = np.where(grid == target_color)
    if len(rows) == 0:
        return None  # Target color not found
    min_row, min_col = np.min(rows), np.min(cols)
    max_row, max_col = np.max(rows), np.max(cols)
    return min_row, min_col, max_row, max_col

def get_target_color(output_grid):
    """
    Determines the target color from the output grid.
    Assumes a non-empty output grid.  Handles edge cases and invalid inputs.
    """
    output_grid = np.array(output_grid)
    if output_grid.size == 0: # Handle empty output grid case.
       return None

    unique_colors = np.unique(output_grid)
    if len(unique_colors) == 1:
        return unique_colors[0]
    # fallback for when not a single color
    return unique_colors[0]

def transform(input_grid, output_grid):
    """
    Extracts a rectangular region of a specific color from the input grid.
    """
    input_grid = np.array(input_grid)  # Ensure input is a NumPy array.
    output_grid = np.array(output_grid)

    # Determine the target color from the output grid.
    target_color = get_target_color(output_grid)
    if target_color is None:
        return [[]]

    # Find the bounding box of the target color in the input grid.
    bounding_box = find_bounding_box(input_grid, target_color)
    if bounding_box is None:
        return [[]] # Return empty grid if target color not found in input.

    min_row, min_col, max_row, max_col = bounding_box

    # Extract the region.
    extracted_region = input_grid[min_row:max_row+1, min_col:max_col+1]

    return extracted_region.tolist()