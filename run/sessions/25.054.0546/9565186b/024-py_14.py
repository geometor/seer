"""
1.  **Identify all colors** present in the input grid.
2.  **Check for Uniform Rows:** Examine each row of the input grid. If a row is found where all pixels have the *same* color, designate that color as the "retained color". If multiple rows have this property, use the color in the higher row.
3.  **Create Output Grid:** Create a new grid with the same dimensions as the input grid, initially filled with gray (color value 5).
4.  **Populate Output Grid:** Iterate through each pixel of the input grid. If a pixel's color matches the "retained color", set the corresponding pixel in the output grid to the "retained color". Otherwise, leave the output pixel as gray (5).
5. If no row is uniform, keep the entire output grid as gray.
"""

import numpy as np

def get_retained_color(grid):
    """Helper function to find the color of the first uniform row."""
    for row in grid:
        if np.all(row == row[0]):
            return row[0]
    return None  # No uniform row found

def transform(input_grid):
    # Create output grid filled with gray (5)
    output_grid = np.full(input_grid.shape, 5, dtype=int)

    # Find the retained color (color of the first uniform row)
    retained_color = get_retained_color(input_grid)

    # If a retained color is found, populate the output grid
    if retained_color is not None:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                if input_grid[i, j] == retained_color:
                    output_grid[i, j] = retained_color

    return output_grid