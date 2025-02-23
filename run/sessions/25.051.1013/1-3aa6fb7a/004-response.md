# 1-3aa6fb7a • 004 • refine_code - CODE

---
```python
"""
The program identifies all azure (8) colored "L"-shaped objects within the input grid. An "L"-shaped object is defined as a 2x2 block of azure pixels with exactly one of the four corners missing. For each identified "L" shape, the program adds a single blue pixel (1) at the interior corner of the "L". The interior corner is defined as the cell within the 2x2 bounding box of the "L" that is *not* occupied by an azure pixel. All other aspects of the input grid remain unchanged.
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
            # Create a 2x2 block to check for L-shapes
            block = grid[i:i+2, j:j+2]
            
            # Count the number of pixels of the specified color in the block
            count = np.sum(block == color)

            # If exactly 3 pixels are of the specified color, it's an L-shape
            if count == 3:
                # Find the coordinates of the missing corner (the interior corner)
                for x in range(2):
                    for y in range(2):
                        if block[x, y] != color:
                            coords.append((i + x, j + y))
    return coords

def transform(input_grid):
    """
    Transforms the input grid by adding a blue (1) pixel inside the corner of each azure (8) L-shaped object.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input

    # Find the coordinates of the interior corners of L-shaped azure objects
    l_shape_corners = find_l_shapes(output_grid, 8)

    # Add a blue pixel (1) at the interior corner of each L-shaped object
    for corner in l_shape_corners:
        output_grid[corner] = 1

    return output_grid
```

