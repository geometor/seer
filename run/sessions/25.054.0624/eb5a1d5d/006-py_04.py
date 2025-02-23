"""
The transformation identifies nested colored rectangles in the input grid, extracts their colors in order from outermost to innermost, and constructs a square output grid. The output grid's size is determined by the number of nested rectangles. The output is filled concentrically, starting with the outermost color and shrinking inwards, with each subsequent color filling a smaller rectangle. The innermost rectangle is represented by a single pixel.
"""

import numpy as np

def find_nested_rectangles(input_grid):
    """
    Analyzes the input grid to identify nested colored rectangles.

    Returns:
        - A list of colors, from outermost to innermost.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape
    colors = []
    current_color = grid[0, 0]
    colors.append(current_color)

    while True:
        found_new_color = False
        for r in range(rows):
            for c in range(cols):
                if grid[r, c] != current_color:
                    if grid[r,c] not in colors:
                      current_color = grid[r, c]
                      colors.append(current_color)
                      found_new_color = True
        if not found_new_color:
            break

    return colors


def transform(input_grid):
    """Transforms the input grid to the output grid based on the nested rectangles."""

    # Find the nested rectangle colors (outermost to innermost)
    colors = find_nested_rectangles(input_grid)

    # Determine output grid size
    output_size = (2 * len(colors)) - 1
    output_grid = np.full((output_size, output_size), colors[0])  # Initialize with outermost color

    # Construct output concentrically
    for i, color in enumerate(colors):
        layer_thickness = i
        for row in range(layer_thickness, output_size - layer_thickness):
            for col in range(layer_thickness, output_size - layer_thickness):
                output_grid[row, col] = color

    return output_grid.tolist()