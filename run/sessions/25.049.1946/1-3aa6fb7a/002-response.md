# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule identifies azure (color 8) L-shaped objects (made of three cells) and, based on their position on the input grid, paint with color blue (value 1) the cell to the right of the upper part of each "L" object.

1.  **Identify Objects:** Locate all azure (8) colored objects that are composed of three cells forming an "L" shape.
2.  **Find Target:** For each identified L-shaped object, locate the cell immediately to the right of the top-most cell that constructs the shape "L".
3. **Change color:** Change the color value of this target cell to blue (1).
4. **Keep initial object** Keep the identified L-shaped objects.
"""

import numpy as np

def find_l_shapes(grid, color=8):
    """Finds L-shaped objects of a specified color in the grid."""
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for L-shape in all four orientations
            if grid[r, c] == color and grid[r + 1, c] == color and grid[r, c + 1] == color:
                l_shapes.append(((r, c), "top_left"))
            elif grid[r, c] == color and grid[r + 1, c] == color and grid[r + 1, c + 1] == color:
                l_shapes.append(((r, c), "bottom_left"))
            elif grid[r, c] == color and grid[r, c + 1] == color and grid[r + 1, c + 1] == color:
                l_shapes.append(((r, c), "top_right"))
            elif grid[r + 1, c] == color and grid[r, c + 1] == color and grid[r + 1, c + 1] == color:
                l_shapes.append(((r, c), "bottom_right"))

    return l_shapes
def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find L-shapes
    l_shapes = find_l_shapes(output_grid)

    # change pixels to blue to the right based on the top of the "L"
    for (r, c), orientation in l_shapes:
        if orientation == "top_left":
            if c + 2 < cols:
                output_grid[r,c+2] = 1

        if orientation == "top_right":
            if c + 2 < cols:
                output_grid[r,c+2] = 1

        if orientation == "bottom_left":
            if c+1 < cols and r > 0:

                output_grid[r-1,c+1]=1

        if orientation == "bottom_right":
             if c+1 < cols and r-1 > 0 :
                output_grid[r,c]=1


    return output_grid
```
