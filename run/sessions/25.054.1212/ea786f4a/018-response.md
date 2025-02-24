# ea786f4a • 018 • refine_coder

---
```python
"""
1.  **Locate the Center:** Find the single white pixel (value 0) in the input grid. This pixel defines the center of a cross shape.

2.  **Identify the most frequent color:** Determine the color that appears most frequently within the input grid, excluding white (0).

3.  **Transform into Cross:**
    *   Change the color of the center pixel to the most frequent color.
    *   Change the most frequent color to white(0) on all pixels that form cross shape.
    *    The cross shape is created by extending the center pixel's row and column to the edges of the grid.

4. **No change:** If there isn't a white pixel, then return the original grid.
"""

import numpy as np
from collections import Counter

def find_center(grid):
    # Find the coordinates of the white pixel (value 0).
    rows, cols = np.where(grid == 0)
    if len(rows) > 0:  # Check if a white pixel was found
       return rows[0], cols[0]
    return None

def most_frequent_color(grid):
    # Flatten the grid and use Counter to find the most common color, excluding 0
    flat_grid = grid.flatten()
    color_counts = Counter(flat_grid)
    if 0 in color_counts:
        del color_counts[0]  # Remove 0 from counts

    if len(color_counts) == 0:
        return None # if not other colors found

    most_common = color_counts.most_common(1)
    return most_common[0][0]

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    #find center
    center = find_center(input_grid)
    if center is None: #if no center of this type, return
        return output_grid
    center_row, center_col = center

    #get most frequent color
    freq_color = most_frequent_color(input_grid)
    if freq_color is None:
        return output_grid

    #change the 0 cell
    output_grid[center_row, center_col] = freq_color

    # Iterate through the grid and invert colors based on cross shape
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            if output_grid[row,col] == freq_color:
                if row == center_row or col == center_col:
                    output_grid[row, col] = 0

    return output_grid
```
