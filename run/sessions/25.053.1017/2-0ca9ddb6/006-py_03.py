"""
The transformation adds a colored border around each non-zero pixel in the input grid. The color of the border pixels, and the relative positions, depends on the color of the original, central pixel.
"""

import numpy as np

def get_border_positions(grid, row, col, relative_positions):
    """Calculates the absolute positions of border pixels, checking bounds."""
    border_positions = []
    rows, cols = grid.shape
    for dr, dc in relative_positions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            border_positions.append((new_row, new_col))
    return border_positions

def transform(input_grid):
    """Transforms the input grid by adding colored borders around non-zero pixels."""
    # Initialize output grid with zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Define the color mapping and relative positions for borders.
    color_mapping = {
        1: (7, [(1, 0), (0, 1), (-1, 0), (0, -1)]),  # Blue -> Orange border
        2: (4, [(1, 0), (-1, 0)]),  # Red -> Yellow border
        6: (7, [(-1, 0)]),  # Magenta -> Orange border
    }

    # Iterate through each cell in the input grid
    rows, cols = input_grid.shape
    for row in range(rows):
        for col in range(cols):
            pixel_value = input_grid[row, col]

            # Copy existing pixel to output grid
            output_grid[row,col] = pixel_value

            # If the pixel is a "seed" (non-zero)
            if pixel_value != 0:
                # Get border color and relative positions from the mapping
                if pixel_value in color_mapping:
                    border_color, relative_positions = color_mapping[pixel_value]

                    # Calculate border positions and set border pixels in output
                    border_positions = get_border_positions(input_grid, row, col, relative_positions)
                    for b_row, b_col in border_positions:
                        output_grid[b_row, b_col] = border_color

    return output_grid