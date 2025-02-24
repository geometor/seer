# 67385a82 • 012 • refine_coder

---
```python
"""
Identifies horizontal runs of contiguous green pixels. If a run has length 2 or more,
change all pixels in that run to azure. If a run has length 1, and is adjacent to
any pixel that has already been changed to azure, change to azure. Adjacency is checked
iteratively until no more changes can be made.
"""

import numpy as np

def get_runs(grid):
    """Helper function to extract horizontal runs of green pixels."""
    runs = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for r in range(rows):
        start_col = -1
        for c in range(cols):
            if grid[r][c] == 3:
                if start_col == -1:
                    start_col = c
            elif start_col != -1:
                runs.append((r, start_col, c - 1))
                start_col = -1
        if start_col != -1:  # Handle runs that extend to the end of the row
            runs.append((r, start_col, cols - 1))
    return runs

def transform(input_grid):
    """
    Transforms the input grid by changing horizontally contiguous green pixels to azure based on run length and adjacency.
    """
    output_grid = [row[:] for row in input_grid]  # Create a copy
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # 1. Identify and Measure Horizontal Runs
    runs = get_runs(output_grid)


    # 2. Change pixels based on run length (>= 2)
    for r, start_c, end_c in runs:
        if end_c - start_c + 1 >= 2:
            for c in range(start_c, end_c + 1):
                output_grid[r][c] = 8

    # 3. Iteratively apply adjacency rule for single-pixel runs.
    while True:
        changed = False
        runs = get_runs(output_grid) # get runs from output_grid
        for r, start_c, end_c in runs:
            if end_c - start_c + 1 == 1:
                if start_c > 0 and output_grid[r][start_c - 1] == 8:
                    output_grid[r][start_c] = 8
                    changed = True
                elif end_c < cols - 1 and output_grid[r][end_c + 1] == 8:
                    output_grid[r][end_c] = 8
                    changed = True
        if not changed:
            break  # Exit loop if no changes were made in this iteration

    return output_grid
```
