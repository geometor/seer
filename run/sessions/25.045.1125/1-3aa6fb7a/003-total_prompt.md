# 25.045.1125 • 1-3aa6fb7a • 003 example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F07109D80>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F0710A200>

*text:*
**Natural Language Program:**

1. **Identify Objects:** Find all connected regions of color 8 (azure) in the input grid. We consider these regions as distinct objects.
2. **Locate Topmost Cell:** For each region of color 8, determine the cell with the smallest row index. If there are multiple cells with the same smallest row index, choose the one with the smallest column index among them. This cell is the "topmost" cell of the region.
3. **Locate Bottommost Cell:** For each region of color 8, determine the cell with the largest row index. If there are multiple cells with the same largest row index, choose the one with the smallest column index among them. This cell is the "bottommost" cell of the region.
4. **Transform Topmost Neighbor:** For each region, examine the cell immediately to the right of its "topmost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
5. **Transform Bottommost Neighbor:** For each region, examine the cell immediately to the left of its "bottommost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
6. **Output:** The grid modified after applying steps 4 and 5 for all regions of color 8 is the final output grid.

This program describes how to identify contiguous regions of color 8 as objects and then modify specific neighboring cells based on the topmost and bottommost cells within each object.

*text:*
```python
"""
Identifies connected regions of color 8 (azure) in the input grid.
For each region, finds the topmost and bottommost cells.
Changes the color of the cell to the right of the topmost cell and the cell to the left of the bottommost cell to 1 (blue), if they are 0 (white) and within grid boundaries.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
    # initialize output as a numpy array for easier manipulation
    output_grid = np.array(input_grid).copy()

    # Find regions of color 8
    regions, num_regions = label(output_grid == 8)

    for region_label in range(1, num_regions + 1):
        # Get the coordinates of cells in the current region
        region_coords = np.argwhere(regions == region_label)

        if len(region_coords) > 0:
            # Find topmost cell
            topmost_idx = np.argmin(region_coords[:, 0]) # index of min row
            topmost_cell = region_coords[topmost_idx] # (row, col) of topmost cell

            # Find bottommost cell
            bottommost_idx = np.argmax(region_coords[:, 0]) # index of max row
            bottommost_cell = region_coords[bottommost_idx] # (row, col) of bottommost cell


            # Transform Topmost Neighbor (right)
            top_row, top_col = topmost_cell
            right_col = top_col + 1
            if right_col < output_grid.shape[1] and output_grid[top_row, right_col] == 0:
                output_grid[top_row, right_col] = 1

            # Transform Bottommost Neighbor (left)
            bottom_row, bottom_col = bottommost_cell
            left_col = bottom_col - 1
            if left_col >= 0 and output_grid[bottom_row, left_col] == 0:
                output_grid[bottom_row, left_col] = 1

    return output_grid.tolist()


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F0710A110>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F0710A3E0>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
