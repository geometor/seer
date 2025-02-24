# a740d043 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule is to "crop" the input grid by removing the outer "frame" of the dominant color, and outputting the remaining internal region.
"""

import numpy as np

def find_internal_region(grid):
    """Finds the bounding box of the non-dominant color region."""
    rows, cols = grid.shape
    
    # Find dominant color (most frequent color on the border)
    border_pixels = np.concatenate([
        grid[0, :], grid[-1, :], grid[:, 0], grid[:, -1]
    ])
    unique, counts = np.unique(border_pixels, return_counts=True)
    dominant_color = unique[np.argmax(counts)]

    # Find rows and cols that contain non-dominant colors
    non_dominant_rows = []
    non_dominant_cols = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != dominant_color:
                non_dominant_rows.append(r)
                non_dominant_cols.append(c)
    
    if not non_dominant_rows: # Handle the edge case of a uniform grid
        return (0, 0, rows-1, cols-1)

    min_row, max_row = min(non_dominant_rows), max(non_dominant_rows)
    min_col, max_col = min(non_dominant_cols), max(non_dominant_cols)
    
    return (min_row, max_row, min_col, max_col)

def transform(input_grid):
    """
    Extracts the internal region of the input grid by removing the border of the dominant color.
    """
    # Convert input_grid to numpy array
    grid = np.array(input_grid)

    # Find the bounding box of the internal region
    min_row, max_row, min_col, max_col = find_internal_region(grid)

    # Extract the internal region
    output_grid = grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
