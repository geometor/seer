# 484b58aa • 017 • refine_coder

---
```python
"""
Identify pixels of a specific color (magenta or red in the provided examples) and change them to black (0). If the grid is already all black, or contains a mix of colors 1-9, leave it unchanged.
"""

import numpy as np

def transform(input_grid):
    # Convert to numpy array for easier manipulation
    output_grid = np.array(input_grid)
    input_grid_flat = output_grid.flatten()

    # Check if the grid is all black
    if np.all(input_grid_flat == 0):
        return output_grid.tolist()  # Return unchanged

    # check for a mix of colors 1-9
    unique_colors = np.unique(input_grid_flat)
    if len(unique_colors) > 1 and np.all(unique_colors != 0):
        # if all the colors present in the unique colors are within 1-9
        if np.all((unique_colors >= 1) & (unique_colors <=9)):
            return output_grid.tolist()

    # Identify magenta (6) pixels and change them to black (0)
    output_grid[output_grid == 6] = 0

    # Identify red (2) pixels and change them to black (0)
    output_grid[output_grid == 2] = 0

    return output_grid.tolist()
```
