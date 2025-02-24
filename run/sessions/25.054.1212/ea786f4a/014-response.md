# ea786f4a • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify the Center:** Locate the single white pixel (value 0) in the input grid. This is the center of the transformation.

2.  **Invert Colors in cross pattern:** all pixels that are the same color as the most frequent color get flipped to 0 if they are the same Manhattan distance in the x or y direction from the center. All instances of 0 are also changed to the most frequent color.
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
    # Flatten the grid and use Counter to find the most common color
    flat_grid = grid.flatten()
    color_counts = Counter(flat_grid)
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

    #change the 0 cell
    output_grid[center_row, center_col] = freq_color

    # Iterate through the grid and invert colors based on Manhattan distance
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            if output_grid[row,col] == freq_color:
                if row == center_row or col == center_col:
                    output_grid[row, col] = 0

    return output_grid
```
