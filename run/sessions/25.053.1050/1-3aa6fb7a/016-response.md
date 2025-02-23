# 1-3aa6fb7a • 016 • refine_coder

---
```python
"""
1.  **Identify:** Locate all white (0) and azure (8) pixels within the input grid.
2.  **Iterate:** For each white pixel, examine its entire row.
3.  **Condition:** A white pixel changes to blue (1) if, and *only* if, there are azure pixels present both to its left and to its right anywhere on the *same* row. Note, it does not have to be the *immediate* neighbor, just *somewhere* to the left and right on that row.
4.  **Output:** The modified grid constitutes the output, where qualifying white pixels have been replaced by blue pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is white
            if output_grid[r, c] == 0:
                # Check for azure neighbors to the left and right on the same row
                left_azure = False
                right_azure = False

                # Check left side
                for i in range(c):
                    if output_grid[r, i] == 8:
                        left_azure = True
                        break

                # Check right side
                for i in range(c + 1, cols):
                    if output_grid[r, i] == 8:
                        right_azure = True
                        break

                # Check if both conditions are met
                if left_azure and right_azure:
                    output_grid[r, c] = 1  # Change white to blue

    return output_grid
```

