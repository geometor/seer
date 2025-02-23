# 4-0d3d703e • 004 • refine_code - CODE

---
```python
"""
The transformation rule can be described by the following process. For each colored cell  `c` located at coordinate (x,y):

1.  **Identify the original color value:** Determine the integer value (0-9) of the cell in the input grid.
2.  **Apply a color-specific transformation**:
    *   If the original color is 1, the output color is 5 (+4).
    *   If the original color is 2, the output color is 6 (+4).
    *   If the original color is 3, the output color is 4 (+1).
    *   If the original color is 4, the output color is 3 (-1).
    *   If the original color is 5, the output color is 1 (-4).
    *   If the original color is 6, the output color is 2 (-4).
    *   If the original color is 8, the output color is 9 (+1).
    *   If the original color is 9, the output color is 8 (-1).
3. **Write the new value** Assign the corresponding transformed value to the same location (x, y) in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on a color-specific rule.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Define the transformation rules as a dictionary.
    transformation_rules = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8
    }

    # Iterate through each cell in the grid.
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            # Get the original color of the cell.
            original_color = input_grid[x, y]
            # Apply the transformation rule if it exists for the original color.
            if original_color in transformation_rules:
                output_grid[x, y] = transformation_rules[original_color]

    return output_grid
```

