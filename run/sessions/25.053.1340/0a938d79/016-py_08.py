"""
Identify the rows in the input grid where each distinct, non-zero color first appears.
Copy these *entire* rows.
Create an output grid where the pattern is a repeating sequence of these identified rows. The sequence restarts from the beginning after the last identified row is placed.
"""

import numpy as np

def find_first_color_rows(input_grid):
    """Finds the row index and content where each distinct color first appears."""
    input_grid = np.array(input_grid)
    color_rows = []
    colors_found = []
    rows, _ = input_grid.shape
    for r in range(rows):
        for c in range(input_grid.shape[1]):
            color = input_grid[r, c]
            if color != 0 and color not in colors_found:
                color_rows.append((r, input_grid[r, :].copy()))  # Store row index and the entire row
                colors_found.append(color)
                break  # Move to the next row after finding the first new color
    return color_rows

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find the row indices and content where each distinct color first appears.
    color_rows = find_first_color_rows(input_grid)
    num_color_rows = len(color_rows)

    # Build the output grid by repeating the sequence of identified rows.
    for i in range(rows):
        row_index, row_content = color_rows[i % num_color_rows]
        output_grid[i, :] = row_content

    return output_grid.tolist()