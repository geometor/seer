# 1-3aa6fb7a • 006 • example_2 - CODE

---
```python
"""
The program involves keeping every existing azure (8) object unchanged and adding a blue pixel (1) at the interior angle of each azure "L"-shaped object.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds the coordinates of the interior corner of L-shaped objects of the specified color.
    """
    coords = []
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if grid[i, j] == color:
                # Check for L-shape (2x2 block with one missing corner)
                if grid[i+1, j] == color and grid[i, j+1] == color and grid[i+1, j+1] != color:
                    coords.append((i+1, j+1))
                elif grid[i+1, j] == color and grid[i, j+1] != color and grid[i+1, j+1] == color:
                    coords.append((i+1, j))
                elif grid[i+1, j] != color and grid[i, j+1] == color and grid[i+1, j+1] == color:
                    coords.append((i, j+1))
    return coords

def transform(input_grid):
    """
    Transforms the input grid by adding a blue (1) pixel inside the corner of each azure (8) L-shaped object.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input
    
    # Find the coordinates of the corners of L-shaped azure objects
    l_shape_corners = find_l_shapes(output_grid, 8)

    # Add a blue pixel (1) at the corner of each L-shaped object
    for corner in l_shape_corners:
        output_grid[corner] = 1

    return output_grid
```

