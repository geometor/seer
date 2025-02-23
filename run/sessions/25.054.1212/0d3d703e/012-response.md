# 0d3d703e • 012 • refine_coder

---
```python
"""
The program implements a color substitution cipher. It transforms an input grid of colored pixels into an output grid of the same dimensions by applying the following transformation to each pixel:

1.  **Maintain Grid Structure**: The output grid has the same shape (height and width) as the input grid.

2.  **Color Substitution:** Each pixel's color in the input grid is replaced with a different color in the output grid according to the following mapping:
    *   Red (2) becomes Magenta (6)
    *   Green (3) becomes Yellow (4)
    *   Azure (8) becomes Maroon (9)
    *   Blue (1) becomes Grey(5)
    *  Yellow(4) becomes Green(3)
    *   Grey (5) becomes Blue(1)
    *  Magenta(6) becomes Red(2)
    * Maroon(9) becomes Azure(8)
    * White (0) and Orange(7) are unused, and if present, will be unchanged.

3.  **Iteration:** The transformation is applied to each pixel in the input grid independently.

In simpler terms: The program takes a grid of colored pixels and changes the color of each pixel according to a specific, predefined color-swapping rule, while keeping the overall grid structure the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by applying a color substitution cipher.
    """
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # define the complete color mapping
    color_map = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8
    }

    # iterate through the grid and apply the color mapping
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid
```

