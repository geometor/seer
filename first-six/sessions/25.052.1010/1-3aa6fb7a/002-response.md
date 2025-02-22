# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule involves adding the number "1" (blue color) at specific corners of the azure (color 8) shapes. 
Specifically, a blue cell is inserted at the top-right corner of the top 2x1 azure rectangle and at the bottom-left corner of the bottom 2x1 azure rectangle.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find and return the positions of all 2x1 rectangles of the specified color.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and c+1 < cols and grid[r + 1, c] == color:
                objects.append((r, c))
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all 2x1 rectangles of color 8 (azure)
    azure_objects = find_objects(output_grid, 8)
    
    # Check if exactly two azure objects are found to apply the rule.
    if len(azure_objects) >= 2:
        # Locate the top-right corner of the first object and insert color 1 (blue)
        top_right_corner = (azure_objects[0][0], azure_objects[0][1] + 1)
        output_grid[top_right_corner] = 1

        # Locate the bottom-left corner of the second object and insert color 1 (blue)
        # Assuming second object is always at the expected index
        bottom_left_corner = (azure_objects[1][0] + 1, azure_objects[1][1])
        output_grid[bottom_left_corner] = 1

    return output_grid
```
