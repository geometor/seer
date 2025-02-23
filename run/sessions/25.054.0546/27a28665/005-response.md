# 27a28665 • 005 • refine_coder

---
```python
"""
1.  **Input:** A square grid of pixels (integers 0-9).
2.  **Ignore:** Pixels with a value of 0 (white).
3.  **Extract:**  The main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left).
4. **Compare:** Check if non-white values of main and anti diagonals are the same.
5.  **Count:**
     If non-white values are on both diagonals AND they're the same, the counter is set to 1.
     If the non-white values are different, and are present on either diagonal, set counter to 2.
     If there are no non-white values, set the counter to 0.

6.  **Output:** A 1x1 grid containing the final count.
"""

import numpy as np

def _extract_diagonals(grid):
    """Extracts the main and anti-diagonals of a square grid."""
    rows, cols = grid.shape
    main_diag = [grid[i, i] for i in range(rows)]
    anti_diag = [grid[i, cols - 1 - i] for i in range(rows)]
    return main_diag, anti_diag

def _compare_diagonals(main_diag, anti_diag):
    """Compares the non-white elements of two diagonals."""
    main_diag_non_white = [x for x in main_diag if x != 0]
    anti_diag_non_white = [x for x in anti_diag if x != 0]

    if len(main_diag_non_white) == 0 and len(anti_diag_non_white) == 0:
        return "neither"
    elif main_diag_non_white == anti_diag_non_white:
        return "equal"
    elif len(main_diag_non_white) > 0 and len(anti_diag_non_white) >0:
      return "different"    
    elif len(main_diag_non_white) > 0:
        return "main_only"
    else:
        return "anti_only"

def transform(input_grid):
    # initialize output_grid
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    output_grid = [[0]] #initialize to 0

    # Only process if input is a square
    if rows == cols:
        main_diag, anti_diag = _extract_diagonals(input_array)
        comparison_result = _compare_diagonals(main_diag, anti_diag)

        if comparison_result == "equal":
            output_grid[0][0] = 1
        elif comparison_result == "different" or comparison_result == "main_only" or comparison_result == "anti_only":
            output_grid[0][0] = 2
        #else it remains zero

    return output_grid
```
