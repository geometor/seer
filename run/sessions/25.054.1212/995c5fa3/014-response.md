# 995c5fa3 • 014 • example_3 • investigate_coder

---
```python
"""
1. **Scan the Input:** Examine the input grid and identify the columns that contain white (0) pixels.
2. **Column-to-Row Mapping:**  For each identified column containing white, map it to a corresponding row in the output grid:
    - The first column with a white pixel corresponds to output row 1.
    - The second column with a white pixel corresponds to output row 2.
    - The third column with a white pixel corresponds to output row 3.
3. **Assign Colors:** Assign a specific color to each output row based on a predefined mapping:
    - Row 1: Azure (8)
    - Row 2: Red (2)
    - Row 3: Yellow (4)
4. **Create Output:** Construct a 3x3 output grid. Fill all cells in each row of output with mapped color.
"""

import numpy as np

def get_white_columns(grid):
    # Find columns containing white (0) pixels
    white_columns = []
    for x in range(grid.shape[1]):
        if 0 in grid[:, x]:
            white_columns.append(x)
    return white_columns

def transform(input_grid):
    # Initialize output grid as 3x3 numpy array
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the columns containing white pixels
    white_cols = get_white_columns(input_grid)

    # Define the color mapping
    color_map = {
        0: 8,  # First white column -> Row 1: Azure (8)
        1: 2,  # Second white column -> Row 2: Red (2)
        2: 4   # Third white column -> Row 3: Yellow (4)
    }

    # Map white columns to output rows and colors
    for i, col in enumerate(white_cols):
        if i < 3: # important - stop after finding at most 3 columns
            output_grid[i, :] = color_map[i]

    return output_grid
```
