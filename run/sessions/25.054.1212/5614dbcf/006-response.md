# 5614dbcf • 006 • refine_coder

---
```python
"""
Divide the input 9x9 grid into nine 3x3 subgrids.  For each 3x3 subgrid, determine the *most frequent non-white* color within that subgrid. If a subgrid contains only white pixels, its representative color is white.  Create a 3x3 output grid. Each cell in the output grid corresponds to a subgrid in the input grid. Populate each cell of the output grid with the representative color determined for the corresponding subgrid.
"""

import numpy as np
from collections import Counter

def get_representative_color(subgrid):
    # Flatten the subgrid and count the occurrences of each color.
    color_counts = Counter(subgrid.flatten())
    # Remove white (0) from the counts if it exists.
    if 0 in color_counts:
        del color_counts[0]
    # If there are any non-white colors, return the most frequent one.
    if color_counts:
        return color_counts.most_common(1)[0][0]
    else:
        # Otherwise, return white (0).
        return 0

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with zeros (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the input grid, dividing it into 3x3 subgrids.
    for i in range(3):
        for j in range(3):
            # Extract the 3x3 subgrid.
            subgrid = input_grid[i*3:(i+1)*3, j*3:(j+1)*3]
            # Get the representative color of the subgrid.
            representative_color = get_representative_color(subgrid)
            # Set the corresponding pixel in the output grid.
            output_grid[i, j] = representative_color

    return output_grid
```

