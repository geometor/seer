"""
The transformation rule is as follows:
1. Identify a contiguous shape of gray (5) pixels in the input grid.
2. Outline the shape by replacing the outermost layer of gray pixels with azure (8) pixels.
3. Fill the interior of the outlined shape with red (2) pixels.
4. Preserve the white (0) background.
"""

import numpy as np

def find_shape(grid, color):
    # Find all pixels of the specified color
    shape_pixels = np.argwhere(grid == color)
    
    if shape_pixels.size == 0:
        return []

    # Assuming all shape pixels form one contiguous block, can return directly
    return shape_pixels.tolist()

def is_outermost(grid, row, col, shape_color):
    """
    Checks if a pixel at (row, col) is on the outermost layer of the shape.
    A pixel is outermost if it's part of the shape and has at least one 
    neighbor (up, down, left, right) that is not part of the shape.
    """
    rows, cols = grid.shape
    if grid[row, col] != shape_color:
        return False

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr, nc] != shape_color:
                return True
        else:
            # Consider edges as "outermost"
            return True
    return False

def transform(input_grid):
    # Initialize output_grid with the same dimensions and background as the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the shape (gray pixels)
    shape_pixels = find_shape(input_grid, 5)

    # Outline and fill the shape
    for row, col in shape_pixels:
        if is_outermost(input_grid, row, col, 5):
            output_grid[row, col] = 8  # Azure for outline
        else:
            output_grid[row, col] = 2  # Red for fill

    return output_grid