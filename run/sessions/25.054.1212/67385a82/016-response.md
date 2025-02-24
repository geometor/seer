# 67385a82 • 016 • refine_coder

---
```python
"""
1.  **Find Green Pixels:** Identify all pixels with a value of 3 (green).

2.  **Top Row Transformation:** For any green pixel in the top row (row 0):
    * Check the color of the pixel directly below.
        * If the pixel directly below is azure, change it to white (0).
        * If the pixel directly below is NOT azure, change it to azure (8).
        
3.  **Bottom-Left Transformation:** If a green pixel is in the bottom-left corner (last row, column 0), change its color to azure (8).

4. **All Other Pixels:** All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find green pixels
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Green pixel found
                # Top Row Transformation
                if r == 0:
                    if r + 1 < rows: #ensure we are within the grid
                        if output_grid[r+1,c] == 8:
                            output_grid[r+1, c] = 0  # Change to white
                        else:
                            output_grid[r+1, c] = 8  # Change to azure
                # Bottom-Left Transformation
                elif r == rows - 1 and c == 0:
                    output_grid[r, c] = 8  # Change to azure

    return output_grid
```

