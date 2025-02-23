# 4-0d3d703e • 006 • example_3 - CODE

---
```python
"""
1.  **Color Substitution:** Replace every instance of color 5 (gray) with color 1 (blue), color 8 (azure) with color 9 (maroon), and color 6 (magenta) with color 2 (red). The dimensions and structure remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        5: 1,  # gray to blue
        8: 9,  # azure to maroon
        6: 2   # magenta to red
    }

    # Iterate through the input grid and apply the color substitution.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid
```

