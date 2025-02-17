# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation rule is to locate the empty cell at the inner center of each azure (color 8) L-shaped object and fill those positions with a single blue (color 1) cell. All other cells remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds the coordinates of cells that form an L-shape of the specified color.
    Returns a list of tuples, each containing the coordinates of the three cells forming the L and the inner empty cell.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for L-shape (normal and rotated/inverted)
            if grid[r, c] == color:
                # Check for normal L
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append(((r, c), (r + 1, c), (r, c + 1), (r+1, c+1)))
                # Check for rotated L (90 degrees clockwise)
                if grid[r, c+1] == color and grid[r+1,c+1] == color:
                    l_shapes.append(((r, c), (r, c+1), (r+1,c+1), (r+1,c)))
                
            if grid[r+1,c+1] == color:    
                #Check for rotated L (180 degrees clockwise)
                if grid[r,c+1] == color and grid[r+1,c] == color:
                    l_shapes.append(((r+1,c+1),(r, c+1), (r+1,c),(r,c)))

                # Check for inverted L (270 degrees clockwise)
                if grid[r+1,c] == color and grid[r,c] == color:
                    l_shapes.append(((r+1, c), (r,c), (r+1,c+1),(r,c+1)))

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule: fill the inner center of each azure (color 8) L-shape with a blue (color 1) cell.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    # Fill the inner center of each L-shape with color 1
    for l_shape in l_shapes:
        inner_center = l_shape[3]
        output_grid[inner_center] = 1

    return output_grid
```
