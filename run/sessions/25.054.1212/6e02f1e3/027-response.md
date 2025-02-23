# 6e02f1e3 • 027 • refine_coder

---
```python
"""
1.  **Examine Input:** The input is a square grid (NxN).
2.  **Determine Output Size:** The output grid has the same dimensions as the input grid (NxN).
3. **Diagonal assignment:**
    - if the input grid contains different colors along either diagonal then the output grid has the color gray (5) along both the main (top-left to bottom-right) and anti-diagonal (top-right to bottom-left).
    - Otherwise, if the input grid consists of pixels of only a single color,
        - if N is odd, the output grid will consist of all gray(5).
        - if N is even, ? (we don't have any examples with even sized grids yet)
4.  **Fill Remaining Cells:** All cells *not* on the main or anti-diagonal are filled with black (0).
"""

import numpy as np

def check_diagonal_uniformity(grid, main_diag=True):
    """
    Checks if the specified diagonal has uniform color.

    Args:
        grid: The input numpy array.
        main_diag: True for main diagonal, False for anti-diagonal.

    Returns:
        True if the diagonal is uniform, False otherwise.
    """
    rows, cols = grid.shape
    first_val = None

    for r in range(rows):
        c = r if main_diag else cols - 1 - r
        if 0 <= c < cols:  # Stay within bounds, although shouldn't be needed for square grids
            if first_val is None:
                first_val = grid[r, c]
            elif grid[r, c] != first_val:
                return False
    return True

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Check diagonal uniformity
    main_diag_uniform = check_diagonal_uniformity(input_grid)
    anti_diag_uniform = check_diagonal_uniformity(input_grid, main_diag=False)

    # change output pixels based on uniformity.
    for r in range(rows):
        for c in range(cols):
            if r == c: # main diag
                if not main_diag_uniform:
                    output_grid[r,c] = 5
                elif rows % 2 != 0 and main_diag_uniform and anti_diag_uniform:
                     output_grid[r,c] = 5
            elif r + c == cols - 1: # anti diag
                if not anti_diag_uniform:
                    output_grid[r,c] = 5
                elif rows % 2 != 0 and main_diag_uniform and anti_diag_uniform:
                    output_grid[r,c] = 5

    return output_grid
```
