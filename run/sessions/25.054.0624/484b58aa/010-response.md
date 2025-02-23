# 484b58aa • 010 • refine_coder

---
```python
"""
1. Iterate through each pixel of the input grid.
2. If the pixel is white (0):
    *   Check if it's on the edge of the grid. If so, keep it.
    *   Check its immediate neighbors (up, down, left, right, diagonals).
        *   If any neighbor is outside the grid bounds, keep the white pixel.
        *   If all neighboring pixels that exist (are within bounds) are also white, remove the white pixel.
        *   If neighboring pixels have mixed colors (or are all 0), keep it (handles edges of holes and boundaries correctly).
3. Copy all non-white pixels directly to the output grid in the same position.

"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by removing specific white pixels."""

    rows, cols = input_grid.shape
    output_grid = np.copy(input_grid)  # Start with a copy

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:  # If the pixel is white
                # Check if it's on the edge
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    continue  # Keep edge white pixels

                neighbors = []
                # Check neighbors (including diagonals)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue  # Skip the pixel itself
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            neighbors.append(input_grid[nr, nc])

                # If all neighbors are white (or empty), remove the pixel.
                if all(neighbor == 0 for neighbor in neighbors):
                    output_grid[r,c] = -1  # Mark for removal
                elif len(set(neighbors)) <= 1 and 0 not in neighbors:
                    # All neighbors are same color, but none are white.  keep the pixel.
                    pass # keep the original value
                elif 0 in neighbors and len(set(neighbors)) > 1:
                    #Mixed colors.
                    pass #keep
                elif not neighbors:
                    output_grid[r, c] = 0 #keep solitary pixels

    rows, cols = output_grid.shape
    final_grid = []
    for r in range(rows):
      row = []
      for c in range(cols):
        if output_grid[r,c] != -1:
          row.append(output_grid[r,c])
      if row:
        final_grid.append(row)

    final_grid = np.array(final_grid)

    return final_grid
```

