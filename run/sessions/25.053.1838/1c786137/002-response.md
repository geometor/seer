# 1c786137 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify the Region of Interest:** Locate the rectangular region within the input grid. This rectangle is visually highlighted with a red interior and black border in the provided images.

2.  **Extract:** Create a new grid containing only the pixel values from within the rectangular region defined in the input grid.

3. **Reduce to Output:** the region of interest is the output.
"""

import numpy as np

def find_rectangle(grid, border_color=0, interior_color=2):
    """Finds the bounding box of a rectangle with a specific border and interior color."""
    rows, cols = grid.shape
    min_row, min_col = rows, cols
    max_row, max_col = -1, -1

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == interior_color:
                # Check for border
                is_bordered = False
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if (dr != 0 or dc != 0):  # Skip the center cell
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr, nc] == border_color:
                                    is_bordered = True
                                    break
                    if is_bordered:
                        break

                if is_bordered:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)

    return min_row, min_col, max_row, max_col



def transform(input_grid):
    """Transforms the input grid by extracting the region within a bordered rectangle."""
    # Find the bounding box of the rectangle.
    input_grid = np.array(input_grid)
    min_row, min_col, max_row, max_col = find_rectangle(input_grid)

    # Extract the region of interest.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
