# 484b58aa • 018 • refine_coder

---
```python
"""
The transformation removes white (0) pixels that form contiguous 2x2 or larger squares within the input grid.
Other white pixels, which are not part of such squares, are retained.
"""

import numpy as np

def is_part_of_square(grid, row, col, min_size=2):
    """
    Checks if the pixel at (row, col) is part of a square of size min_size x min_size or larger.

    Args:
        grid: The 2D numpy array.
        row: Row index of the pixel.
        col: Column index of the pixel.
        min_size: The minimum size of the square.

    Returns:
        True if the pixel is part of a square of at least min_size, False otherwise.
    """
    if grid[row, col] != 0:
        return False

    max_size = min(grid.shape[0] - row, grid.shape[1] - col)
    for size in range(min_size, max_size + 1):
        # Check if a square of this size exists
        is_square = True
        for i in range(size):
            for j in range(size):
                if grid[row + i, col + j] != 0:
                    is_square = False
                    break
            if not is_square:
                break
        if is_square:
            return True

    return False
    

def transform(input_grid):
    """
    Transforms an input grid by removing white pixels that are part of 2x2 or larger squares.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array with white pixels within 2x2 or larger squares removed,
        maintaining the relative positions of other pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the input grid.
    for row in range(rows):
        for col in range(cols):
            # Check if pixel is white and part of a 2x2 or larger square
            if is_part_of_square(input_grid, row, col):
                output_grid[row, col] = -1  # Mark for removal

    # Create a new grid excluding the marked pixels (-1)
    rows_to_keep = []
    for r in range(output_grid.shape[0]):
      row = output_grid[r]
      new_row = row[row != -1]
      if new_row.size > 0: #prevent empty rows
        rows_to_keep.append(new_row)

    if len(rows_to_keep) > 0:
        # Find maximum row length
        max_row_length = max(len(r) for r in rows_to_keep)

        # Pad rows with -2 (or any other unique value) to create uniform shape
        padded_rows = []
        for row in rows_to_keep:
          padding_size = max_row_length - len(row)
          padded_row = np.pad(row, (0, padding_size), constant_values=-2)
          padded_rows.append(padded_row)
        
        output_grid = np.array(padded_rows)
    else:
        output_grid = np.array([])


    return output_grid
```

