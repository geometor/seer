# d5d6de2d • 012 • refine_coder

---
```python
"""
1.  **Identify Red Shapes and Their Holes**: Find all contiguous red (value 2) shapes in the input grid. For each red shape, locate the internal "hole," which is a contiguous region of white (value 0) pixels completely enclosed by the red shape. Holes can be of any size (1x1, 3x3, or other dimensions).

2.  **Find the Hole Center**: Calculate the center coordinates of each hole. The center is determined by finding the center row. The columns are the range of columns the hole occupies.

3.  **Create Green Line**: For each hole, replace all of the white pixels with a horizontal line of green (value 3) pixels.

4. **Remove Red**: Change all red pixels in the input to white in the output.

5.  **Preserve other parts:** If any parts of the input are not red or the "hole" inside the red, then those pixels should be value 0 in the output.
"""

import numpy as np
from scipy.ndimage import label

def find_red_shapes(grid):
    # Find all red pixels
    red_pixels = (grid == 2)
    # Label connected components
    labeled_array, num_features = label(red_pixels)
    return labeled_array, num_features

def find_hole(grid, shape_label, labeled_array):
    # Create a mask for the specific shape
    shape_mask = (labeled_array == shape_label)

    # Find the bounding box of the shape
    rows, cols = np.where(shape_mask)
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    # Extract the region within the bounding box
    region = grid[min_row:max_row+1, min_col:max_col+1]
    region_mask = shape_mask[min_row:max_row+1, min_col:max_col+1]

    # Invert the shape mask within the region to find the hole
    hole_mask = (region == 0) & ~region_mask

    if not np.any(hole_mask):
      return None, None, None

    # Find all of the hole pixels
    hole_rows, hole_cols = np.where(hole_mask)
    
    # Transform back to full grid
    hole_rows = hole_rows + min_row
    hole_cols = hole_cols + min_col

    return hole_rows, hole_cols, (min_row, max_row, min_col, max_col)

def transform(input_grid):
    # initialize output_grid as all zeros
    output_grid = np.zeros_like(input_grid)

    # Find red shapes
    labeled_array, num_features = find_red_shapes(input_grid)

    # Iterate through each red shape
    for shape_label in range(1, num_features + 1):
        # Find the hole for the current shape
        hole_rows, hole_cols, bounding_box = find_hole(input_grid, shape_label, labeled_array)
        if hole_rows is not None:
          # Replace the hole pixels with green
          for r, c in zip(hole_rows, hole_cols):
            output_grid[r,c] = 3

        # if we found a bounding box
        if bounding_box is not None:
            # change all red pixels in the input to white in the output
            min_row, max_row, min_col, max_col = bounding_box
            for r in range(min_row, max_row+1):
                for c in range(min_col, max_col+1):
                    if input_grid[r,c] == 2:
                        output_grid[r,c] = 0

    return output_grid
```
