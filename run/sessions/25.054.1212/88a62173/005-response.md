# 88a62173 • 005 • refine_coder

---
```python
"""
1. Identify Selection Region: Consider the 3x3 subgrid at the top-left corner of the input grid.
2. Discard Black Pixels: Remove any black (value 0) pixels.
3. Extract: Extract the 2x2 subgrid at the top-left corner of the reduced selection.
4. Output: The resulting 2x2 grid is the output.
"""

import numpy as np

def get_top_left_3x3(grid):
    """Extracts the top-left 3x3 subgrid."""
    return grid[:3, :3]

def remove_black_pixels(grid):
    """
    Replaces black pixels (0) with a placeholder (-1) to indicate their
    original positions, but keeps track of non-black pixels.
    """
    rows, cols = grid.shape
    result = np.full((rows, cols), -1) # Initialize with -1 (representing empty)
    for i in range(rows):
        for j in range(cols):
          if grid[i,j] != 0:
            result[i,j] = grid[i,j]
    return result

def extract_top_left_2x2(grid):
    """Extracts the top-left 2x2 subgrid."""
    return grid[:2, :2]
  
def replace_neg_one_with_zero(grid):
    """Replaces -1 values in the grid with 0."""
    rows, cols = grid.shape
    result = np.copy(grid)
    for i in range(rows):
      for j in range(cols):
          if result[i, j] == -1:
              result[i,j] = 0
    return result

def transform(input_grid):
    """Transforms the input grid according to the identified rule."""

    # Convert the input grid to a NumPy array for easier manipulation.
    input_grid = np.array(input_grid)

    # 1. Identify Selection Region: Get the top-left 3x3 subgrid.
    selection_region = get_top_left_3x3(input_grid)

    # 2. Discard Black Pixels, keep track of their absence
    modified_selection = remove_black_pixels(selection_region)

    # 3. Extract the top-left 2x2 subgrid.
    output_grid = extract_top_left_2x2(modified_selection)

    # restore -1 to 0.
    output_grid = replace_neg_one_with_zero(output_grid)

    return output_grid.tolist()
```

