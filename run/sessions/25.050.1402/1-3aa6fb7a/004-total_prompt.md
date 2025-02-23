# 1-3aa6fb7a • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1AF80>

**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1BF10>
**Natural Language Program:**

For each connected region of color 8 in the input grid:
1. Identify the cell within the region that has the largest row index. If there are multiple such cells, choose the one with the largest column index among them. Let's call the coordinates of this cell (R, C).
2. Check the cell directly above, at coordinates (R-1, C). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
3. If step 2 did not result in a change (either the cell above was not within bounds, not color 0, or already changed), then check the cell directly to the left, at coordinates (R, C-1). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
4. If neither step 2 nor step 3 resulted in a change, no modification is made for this region of color 8.

This process is applied independently to each connected region of color 8 in the input grid.
```python
"""
For each connected region of color 8 in the input grid:
1. Identify the cell within the region that has the largest row index. If there are multiple such cells, choose the one with the largest column index among them. Let's call the coordinates of this cell (R, C).
2. Check the cell directly above, at coordinates (R-1, C). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
3. If step 2 did not result in a change (either the cell above was not within bounds, not color 0, or already changed), then check the cell directly to the left, at coordinates (R, C-1). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
4. If neither step 2 nor step 3 resulted in a change, no modification is made for this region of color 8.

This process is applied independently to each connected region of color 8 in the input grid.
"""

import numpy as np

def find_regions(grid, color):
    """
    Finds connected regions of a specific color in the grid.
    Returns a list of regions, where each region is a list of (row, col) coordinates.
    """
    visited = set()
    regions = []

    def dfs(row, col, current_region):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_region.append((row, col))
        dfs(row + 1, col, current_region)
        dfs(row - 1, col, current_region)
        dfs(row, col + 1, current_region)
        dfs(row, col - 1, current_region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)
    return regions

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    output_grid = np.copy(input_grid)
    regions = find_regions(input_grid, 8)

    for region in regions:
        # Find the cell with the largest row index, and then largest column index.
        target_cell = max(region, key=lambda cell: (cell[0], cell[1]))
        r, c = target_cell

        # Check cell above
        if r - 1 >= 0 and output_grid[r - 1, c] == 0:
            output_grid[r - 1, c] = 1
            continue  # Move to the next region

        # Check cell to the left
        if c - 1 >= 0 and output_grid[r, c - 1] == 0:
            output_grid[r, c - 1] = 1

    return output_grid
```

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1A980>

**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1B2E0>
**Natural Language Program:**

The transformation process operates on connected regions of color 8. For each such region:

1. **Identify the Target Cell:** Locate the cell within the region that is the bottom-most (largest row index). If there are multiple cells with the same largest row index, select the one that is right-most (largest column index).

2. **Check and Modify Cell Above:** Examine the cell immediately above the target cell.
   - **Condition:** If this cell is within the grid boundaries and is currently color 0 (white).
   - **Action:** Change the color of this cell to 1 (blue).
   - **Stop:** If the color is changed in this step, no further modifications are made for this region.

3. **Check and Modify Cell to the Left (if step 2 was skipped):** If the cell above was not modified (either the condition in step 2 was not met, or there was no cell above), then examine the cell immediately to the left of the target cell.
   - **Condition:** If this cell is within the grid boundaries and is currently color 0 (white).
   - **Action:** Change the color of this cell to 1 (blue).

4. **No Modification:** If neither the cell above nor the cell to the left is modified, then no changes are made for this particular region of color 8.

This process is applied independently to each connected region of color 8 present in the input grid.
**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
