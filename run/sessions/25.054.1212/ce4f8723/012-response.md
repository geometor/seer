# ce4f8723 • 012 • refine_coder

---
```python
"""
Extracts the top-left 4x4 region of the input grid and recolors it: blue (1) becomes green (3), and white (0) remains white (0). The output is always 4x4.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize the output grid as a 4x4 array filled with zeros.
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through the top-left 4x4 region of the input grid.
    for i in range(4):
        for j in range(4):
            # Extract the corresponding cell value.
            cell_value = input_grid[i][j]

            # Apply the color mapping rules.
            if cell_value == 1:  # Blue
                output_grid[i][j] = 3  # Green
            elif cell_value == 0: #white
                output_grid[i][j] = 0 #white
            #No other colors are changed.

    return output_grid
```

