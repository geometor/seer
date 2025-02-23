# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
This program transforms the input grid to the output grid by applying the following color mapping:
- Color 2 (red) in the input grid is changed to color 6 (magenta) in the output grid.
- Color 3 (green) in the input grid is changed to color 4 (yellow) in the output grid.
- Color 8 (azure) in the input grid is changed to color 9 (maroon) in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid by applying a color mapping.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
    
    Returns:
        numpy.ndarray: A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        2: 6,  # Red to Magenta
        3: 4,  # Green to Yellow
        8: 9   # Azure to Maroon
    }

    # Iterate over all cells in the grid using nested loops.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply color transformation based on the color map.
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid
```

