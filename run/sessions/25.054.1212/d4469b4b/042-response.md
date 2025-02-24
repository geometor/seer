# d4469b4b • 042 • refine_coder

---
```python
"""
Finds the smallest 3x3 grid that can contain all pixels of the
first non-background color. Create an output grid of size 3x3,
and color the output grid pixels grey (5) if the input grid
pixel is the main color, black (0) otherwise.
"""

import numpy as np

def get_object_indices(grid, color):
    """
    Find the indices of an object in a grid given its color.
    """
    return np.argwhere(grid == color)

def transform(input_grid):
    """
    Transforms the input grid according to the described rules.
    """
    # Convert input to numpy array
    input_grid_np = np.array(input_grid)

    # 1. Identify the "main color" (first non-background color)
    non_bg_colors = input_grid_np[input_grid_np != 0]
    main_color = non_bg_colors[0] if non_bg_colors.size > 0 else 0

    # 2. Find indices of the main color object
    main_indices = get_object_indices(input_grid_np, main_color)

    # 3. Determine the bounding box
    if len(main_indices) > 0:
        min_row, min_col = np.min(main_indices, axis=0)
        max_row, max_col = np.max(main_indices, axis=0)
    else:
        min_row, min_col = 0, 0
        max_row, max_col = 0, 0


    # 4. Create 3x3 output grid, initialized to black (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # 5. Populate the output grid based on relative positions, normalized to 3x3
    for r, c in main_indices:
        relative_row = r - min_row
        relative_col = c - min_col

        # Normalize to fit within 3x3
        if 0 <= relative_row < 3 and 0 <= relative_col < 3:
            output_grid[relative_row, relative_col] = 5

    return output_grid.tolist()
```
