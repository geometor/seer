"""
The transformation extracts the smallest rectangular subgrid that contains all non-zero pixels from the input grid.  It effectively "crops" the input grid, removing all surrounding rows and columns that contain *only* black (0) pixels. The colors and relative positions of the non-zero pixels are preserved.

1.  **Identify Non-Zero Pixels:** Locate all pixels within the input grid that have a value other than 0.
2.  **Find Bounding Box:** Determine the minimum and maximum row indices, and the minimum and maximum column indices, that encompass all non-zero pixels.  This defines a rectangular region.
3.  **Extract Subgrid:** Create a new grid consisting only of the rows and columns within the bounding box identified in step 2. Copy the pixel values from the corresponding locations in the input grid to the new grid.
4. Return the extracted subgrid
"""

import numpy as np
from typing import List, Tuple

def _find_bounding_box(grid: np.ndarray) -> Tuple[int, int, int, int]:
    """Finds the bounding box of non-zero pixels."""
    rows, cols = grid.shape
    min_row, min_col = rows, cols
    max_row, max_col = -1, -1

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r)
                max_col = max(max_col, c)

    if max_row == -1:  # Handle the case where the grid is all zeros
      return 0,0,-1,-1
    return min_row, min_col, max_row + 1, max_col + 1

def transform(input_grid: List[List[int]]) -> List[List[int]]:
    """Extracts the smallest subgrid containing all non-zero pixels."""
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the bounding box
    top, left, bottom, right = _find_bounding_box(input_grid)

    # Extract the subgrid.
    if bottom == -1:
        output_grid = []
    else:
        output_grid = input_grid[top:bottom, left:right].tolist()

    return output_grid