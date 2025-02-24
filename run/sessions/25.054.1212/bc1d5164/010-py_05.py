"""
1.  **Identify the outermost bounding pixels:** Find the non-background colored pixels that form the edges of a conceptual rectangle within the input grid. Consider all non-zero colors.
2.  **Determine Output Dimensions:** Calculate the rectangle size from these bounding pixels:
    - The width and height will be based on the number of pixels from leftmost to rightmost and topmost to bottommost.
    - if width or height < 3, create 3x3 subgrid.
3.  **Extract Subgrid:** Create a new grid of the appropriate size
    - Copy the content from the top-left corner of the detected rectangle
"""

import numpy as np

def find_bounding_pixels(input_grid):
    """Finds the outermost non-background pixels."""
    rows, cols = input_grid.shape
    non_bg_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_bg_pixels.append((r, c))
    return non_bg_pixels

def extract_subgrid(input_grid, bounding_pixels):
    """Extracts the subgrid based on bounding pixels."""
    if not bounding_pixels:
        return np.zeros((3, 3), dtype=int).tolist()  # Return 3x3 of background if no bounding pixels

    min_row = min(r for r, c in bounding_pixels)
    max_row = max(r for r, c in bounding_pixels)
    min_col = min(c for r, c in bounding_pixels)
    max_col = max(c for r, c in bounding_pixels)

    height = max_row - min_row + 1
    width = max_col - min_col + 1
    
    if height < 3 or width < 3:
      output_grid = input_grid[min_row:min_row + 3, min_col:min_col+3].copy()
      return output_grid
    
    
    return output_grid.tolist()

def transform(input_grid):
    """Transforms the input grid to the output grid."""
    input_grid = np.array(input_grid)

    # Find the bounding pixels (non-background)
    bounding_pixels = find_bounding_pixels(input_grid)

    # Extract the subgrid based on the bounding rectangle.
    output_grid = extract_subgrid(input_grid, bounding_pixels)
    
    #handle edge case:
    if output_grid is None:
      return np.zeros((3,3), dtype=int).tolist()

    return output_grid