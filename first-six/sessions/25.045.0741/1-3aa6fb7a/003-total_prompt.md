# 25.045.0741 • 1-3aa6fb7a • 003 example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FA68BE19510>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FA68BE198A0>

*text:*
```yaml
task_context: "The task involves transforming an input grid to an output grid. The transformation rule is based on connected components of color '8' (azure)."
objects:
  - type: "grid"
    description: "A 2D array of integers representing colors."
  - type: "connected component"
    color: 8
    description: "A group of adjacent cells of color '8', where adjacency is defined horizontally and vertically."
predicates:
  - "connected":
      description: "Cells are adjacent horizontally or vertically and have the same color."
  - "color":
      description: "The color value of a cell."
  - "top-leftmost":
      description: "The cell in a connected component with the minimum row index, and among those with the minimum column index."
actions:
  - "identify_connected_components":
      description: "Find all groups of connected cells of color '8'."
  - "find_top_leftmost_cell":
      description: "For each connected component, determine the cell with the minimum row and then minimum column index."
  - "check_cell_to_right":
      description: "Examine the cell immediately to the right of the top-leftmost cell."
  - "check_cell_below":
      description: "If the cell to the right was not modified, examine the cell immediately below the top-leftmost cell."
  - "change_color":
      description: "If a checked cell is within grid boundaries and has color '0', change its color to '1'."
transformation_rule: "For each connected component of color '8', identify its top-leftmost cell. If the cell to its right is within the grid and is '0', change it to '1'. Otherwise, if the cell below is within the grid and is '0', change it to '1'."
```

**Natural Language Program:**

The transformation process operates on connected regions of color '8' (azure) within the input grid. For each distinct connected component of '8's, the algorithm identifies a specific cell within that component: the "top-leftmost" cell. This cell is defined as the cell with the smallest row index, and in case of ties, the smallest column index among those with the smallest row index within the component.

Once the top-leftmost cell of a component is located, the algorithm first checks the cell immediately to its right. If this cell is within the grid boundaries and its color in the input grid is '0' (white), then the color of this cell is changed to '1' (blue) in the output grid.

If the cell to the right is not modified (either because it's out of bounds, or its color is not '0'), the algorithm then checks the cell immediately below the top-leftmost cell. If this cell is within the grid boundaries and its color in the input grid is '0', then the color of this cell is changed to '1' in the output grid.

If neither the cell to the right nor the cell below meet the conditions for color change, then no modification is made for that specific connected component. This process is repeated for every connected component of color '8' in the input grid to produce the final output grid.

**Python Implementation:**
```python
import numpy as np
from scipy.ndimage import label

def transform_grid(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid_np = np.copy(input_grid_np)

    labeled_grid, num_components = label(input_grid_np == 8)

    for component_index in range(1, num_components + 1):
        component_coords = np.argwhere(labeled_grid == component_index)
        min_row = np.min(component_coords[:, 0])
        topmost_cells = component_coords[component_coords[:, 0] == min_row]
        top_leftmost_cell_coord = topmost_cells[np.argmin(topmost_cells[:, 1])]
        row, col = top_leftmost_cell_coord

        # Check cell to the right
        right_col = col + 1
        if 0 <= right_col < input_grid_np.shape[1]:
            if input_grid_np[row, right_col] == 0:
                output_grid_np[row, right_col] = 1
                continue # If right is changed, do not check below

        # Check cell below
        below_row = row + 1
        if 0 <= below_row < input_grid_np.shape[0]:
            if input_grid_np[below_row, col] == 0:
                output_grid_np[below_row, col] = 1

    return output_grid_np.tolist()

# Example usage (with the input provided in the problem description)
input_grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

output_grid = transform_grid(input_grid)
print(output_grid)
```

*text:*
```python
"""
The transformation process operates on connected regions of color '8' (azure) within the input grid. For each distinct connected component of '8's, the algorithm identifies a specific cell within that component: the "top-leftmost" cell. This cell is defined as the cell with the smallest row index, and in case of ties, the smallest column index among those with the smallest row index within the component.

Once the top-leftmost cell of a component is located, the algorithm first checks the cell immediately to its right. If this cell is within the grid boundaries and its color in the input grid is '0' (white), then the color of this cell is changed to '1' (blue) in the output grid.

If the cell to the right is not modified (either because it's out of bounds, or its color is not '0'), the algorithm then checks the cell immediately below the top-leftmost cell. If this cell is within the grid boundaries and its color in the input grid is '0', then the color of this cell is changed to '1' in the output grid.

If neither the cell to the right nor the cell below meet the conditions for color change, then no modification is made for that specific connected component. This process is repeated for every connected component of color '8' in the input grid to produce the final output grid.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid_np = np.copy(input_grid_np)

    labeled_grid, num_components = label(input_grid_np == 8)

    for component_index in range(1, num_components + 1):
        component_coords = np.argwhere(labeled_grid == component_index)
        min_row = np.min(component_coords[:, 0])
        topmost_cells = component_coords[component_coords[:, 0] == min_row]
        top_leftmost_cell_coord = topmost_cells[np.argmin(topmost_cells[:, 1])]
        row, col = top_leftmost_cell_coord

        # Check cell to the right
        right_col = col + 1
        if 0 <= right_col < input_grid_np.shape[1]:
            if input_grid_np[row, right_col] == 0:
                output_grid_np[row, right_col] = 1
                continue # If right is changed, do not check below

        # Check cell below
        below_row = row + 1
        if 0 <= below_row < input_grid_np.shape[0]:
            if input_grid_np[below_row, col] == 0:
                output_grid_np[below_row, col] = 1

    return output_grid_np.tolist()


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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FA68BE192A0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FA68BE19570>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
