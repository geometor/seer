# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The transformation rule is a color substitution cipher. Each color in the input grid maps to a unique color in the output grid. The geometric structure (vertical lines) and dimensions of the grid are preserved. The mapping is determined by observing the input-output pairs in the examples.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on a learned color mapping.
    The mapping is derived from observing multiple input/output examples.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Define the comprehensive color mapping based on all observed examples.
    color_map = {
        3: 4,  # Green to Yellow (Example 1)
        1: 5,  # Blue to Gray (Example 1)
        2: 6,  # Red to Magenta (Example 1, 4)
        8: 9,  # Azure to Maroon (Example 2, 3)
        5: 1,  # Gray to Blue (Example 3)
        6: 2,   # Magenta to Red (Example 3)
        9: 8,  # Maroon to Azure (Example 4)
        4: 3,  # Yellow to Green (Example 4)
    }

    # Iterate through the input grid and apply the color transformation.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_color = input_grid[i, j]
            # Use the color map to determine the output color.
            # If a color is not in the map, it remains unchanged.
            output_color = color_map.get(input_color, input_color)
            output_grid[i, j] = output_color

    return output_grid
```



Test Input Transformed Output:
![Image](008-py_05-test_output.png)
