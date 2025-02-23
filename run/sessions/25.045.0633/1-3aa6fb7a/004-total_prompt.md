# 25.045.0633 • 1-3aa6fb7a • 004 example_2 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7EECCC10D570>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7EECCC10D900>

*text:*
**Natural Language Description of Transformation:**

For each connected region of color 8 in the input grid:
1. Identify the topmost-leftmost cell of the region. This is the cell with the minimum row index, and among cells with the same minimum row index, the minimum column index.
2. Attempt to change the color of the cell immediately to the right of this topmost-leftmost cell to color 1, but only if:
    a. The cell to the right is within the grid boundaries.
    b. The cell to the right is currently color 0 in the input grid.
    c. The cell to the right is not part of the same connected region of color 8.
3. If the change in step 2 is not possible (because condition a, b, or c is not met), then attempt to change the color of the cell immediately below the topmost-leftmost cell to color 1, but only if:
    a. The cell below is within the grid boundaries.
    b. The cell below is currently color 0 in the input grid.
    c. The cell below is not part of the same connected region of color 8.

**Python Implementation:**

```python
import numpy as np
from scipy.ndimage import label

def transform_grid(input_grid):
    grid = np.array(input_grid)
    output_grid = np.copy(grid)
    labeled_grid, num_labels = label(grid == 8)

    for label_id in range(1, num_labels + 1):
        component_indices = np.argwhere(labeled_grid == label_id)
        min_row = np.min(component_indices[:, 0])
        topmost_cells = component_indices[component_indices[:, 0] == min_row]
        topleft_cell_row, topleft_cell_col = topmost_cells[np.argmin(topmost_cells[:, 1])]

        # Try to change cell to the right
        cell_right_col = topleft_cell_col + 1
        if (0 <= topleft_cell_row < grid.shape[0] and
            0 <= cell_right_col < grid.shape[1]):
            if grid[topleft_cell_row, cell_right_col] == 0 and labeled_grid[topleft_cell_row, cell_right_col] != label_id:
                output_grid[topleft_cell_row, cell_right_col] = 1
                continue # If right cell is changed, move to next component

        # If right cell cannot be changed, try cell below
        cell_below_row = topleft_cell_row + 1
        if (0 <= cell_below_row < grid.shape[0] and
            0 <= topleft_cell_col < grid.shape[1]):
            if grid[cell_below_row, topleft_cell_col] == 0 and labeled_grid[cell_below_row, topleft_cell_col] != label_id:
                output_grid[cell_below_row, topleft_cell_col] = 1
                continue # If below cell is changed, move to next component

    return output_grid.tolist()

# Example usage with input from problem description
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
print("Output Grid:")
for row in output_grid:
    print(row)
```

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle"
transformation_description: "For each connected region of color 8, identify the topmost-leftmost cell. Change the color of the cell immediately to its right to 1 if possible (within bounds, color 0, not part of the same region). If not possible, try to change the cell immediately below in the same conditions."
transformation_rule_objects:
  - object: "connected region of color 8"
    properties:
      - "topmost-leftmost cell"
transformation_rule_actions:
  - action: "change color"
    target_object: "cell immediately to the right of the topmost-leftmost cell"
    target_color: 1
    conditions:
      - "within grid boundaries"
      - "original color is 0"
      - "not part of the same connected region of color 8"
  - action: "change color"
    target_object: "cell immediately below the topmost-leftmost cell"
    target_color: 1
    conditions:
      - "within grid boundaries"
      - "original color is 0"
      - "not part of the same connected region of color 8"
    fallback_for: "right cell change failure"
```

*text:*
```python
"""
For each connected region of color 8 in the input grid:
1. Identify the topmost-leftmost cell of the region. This is the cell with the minimum row index, and among cells with the same minimum row index, the minimum column index.
2. Attempt to change the color of the cell immediately to the right of this topmost-leftmost cell to color 1, but only if:
    a. The cell to the right is within the grid boundaries.
    b. The cell to the right is currently color 0 in the input grid.
    c. The cell to the right is not part of the same connected region of color 8.
3. If the change in step 2 is not possible (because condition a, b, or c is not met), then attempt to change the color of the cell immediately below the topmost-leftmost cell to color 1, but only if:
    a. The cell below is within the grid boundaries.
    b. The cell below is currently color 0 in the input grid.
    c. The cell below is not part of the same connected region of color 8.
"""

import numpy as np
from scipy.ndimage import label

input_grid = [
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

def transform(input):
    # Convert input list to numpy array for easier manipulation
    grid = np.array(input)
    output_grid = np.copy(grid)
    # Label connected regions of color 8
    labeled_grid, num_labels = label(grid == 8)

    # Iterate through each connected region
    for label_id in range(1, num_labels + 1):
        # Get indices of cells belonging to the current region
        component_indices = np.argwhere(labeled_grid == label_id)
        # Find the topmost row index
        min_row = np.min(component_indices[:, 0])
        # Find all cells in the topmost row
        topmost_cells = component_indices[component_indices[:, 0] == min_row]
        # Find the topmost-leftmost cell (minimum column index among topmost cells)
        topleft_cell_row, topleft_cell_col = topmost_cells[np.argmin(topmost_cells[:, 1])]

        # Try to change cell to the right
        cell_right_col = topleft_cell_col + 1
        if (0 <= topleft_cell_row < grid.shape[0] and
            0 <= cell_right_col < grid.shape[1]): # Check grid boundaries
            if grid[topleft_cell_row, cell_right_col] == 0 and labeled_grid[topleft_cell_row, cell_right_col] != label_id: # Check color and not part of same region
                output_grid[topleft_cell_row, cell_right_col] = 1
                continue # If right cell is changed, move to next component

        # If right cell cannot be changed, try cell below
        cell_below_row = topleft_cell_row + 1
        if (0 <= cell_below_row < grid.shape[0] and
            0 <= topleft_cell_col < grid.shape[1]): # Check grid boundaries
            if grid[cell_below_row, topleft_cell_col] == 0 and labeled_grid[cell_below_row, topleft_cell_col] != label_id: # Check color and not part of same region
                output_grid[cell_below_row, topleft_cell_col] = 1
                continue # If below cell is changed, move to next component

    return output_grid.tolist()


if __name__ == '__main__':

    output = transform(input_grid)

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7EECCC10DAE0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7EECCC10D2A0>

*text:*
**Natural Language Description of Transformation:**

For each connected region of color 8 in the input grid:
1. Identify the topmost-leftmost cell of the region. This is the cell with the minimum row index, and among cells with the same minimum row index, the minimum column index.
2. Attempt to change the color of the cell immediately to the **right** of this topmost-leftmost cell to color 1, but only if:
    a. The cell to the right is within the grid boundaries.
    b. The cell to the right is currently color 0 in the input grid.
    c. The cell to the right is not part of the same connected region of color 8.
3. If the change in step 2 is not possible (because condition a, b, or c is not met), then attempt to change the color of the cell immediately **below** the topmost-leftmost cell to color 1, but only if:
    a. The cell below is within the grid boundaries.
    b. The cell below is currently color 0 in the input grid.
    c. The cell below is not part of the same connected region of color 8.
4. If the change in step 3 is not possible, then attempt to change the color of the cell immediately to the **left** of the topmost-leftmost cell to color 1, but only if:
    a. The cell to the left is within the grid boundaries.
    b. The cell to the left is currently color 0 in the input grid.
    c. The cell to the left is not part of the same connected region of color 8.
5. If the change in step 4 is not possible, then attempt to change the color of the cell immediately **above** the topmost-leftmost cell to color 1, but only if:
    a. The cell above is within the grid boundaries.
    b. The cell above is currently color 0 in the input grid.
    c. The cell above is not part of the same connected region of color 8.
6. If none of the above changes are possible, no change is made for this region.

**Python Implementation:**

```python
import numpy as np
from scipy.ndimage import label

def transform(input):
    grid = np.array(input)
    output_grid = np.copy(grid)
    labeled_grid, num_labels = label(grid == 8)

    for label_id in range(1, num_labels + 1):
        component_indices = np.argwhere(labeled_grid == label_id)
        min_row = np.min(component_indices[:, 0])
        topmost_cells = component_indices[component_indices[:, 0] == min_row]
        topleft_cell_row, topleft_cell_col = topmost_cells[np.argmin(topmost_cells[:, 1])]

        # Try to change cell to the right
        cell_r_row, cell_r_col = topleft_cell_row, topleft_cell_col + 1
        if (0 <= cell_r_row < grid.shape[0] and 0 <= cell_r_col < grid.shape[1] and
            grid[cell_r_row, cell_r_col] == 0 and labeled_grid[cell_r_row, cell_r_col] != label_id):
            output_grid[cell_r_row, cell_r_col] = 1
            continue

        # Try to change cell below
        cell_b_row, cell_b_col = topleft_cell_row + 1, topleft_cell_col
        if (0 <= cell_b_row < grid.shape[0] and 0 <= cell_b_col < grid.shape[1] and
            grid[cell_b_row, cell_b_col] == 0 and labeled_grid[cell_b_row, cell_b_col] != label_id):
            output_grid[cell_b_row, cell_b_col] = 1
            continue

        # Try to change cell to the left
        cell_l_row, cell_l_col = topleft_cell_row, topleft_cell_col - 1
        if (0 <= cell_l_row < grid.shape[0] and 0 <= cell_l_col < grid.shape[1] and
            grid[cell_l_row, cell_l_col] == 0 and labeled_grid[cell_l_row, cell_l_col] != label_id):
            output_grid[cell_l_row, cell_l_col] = 1
            continue

        # Try to change cell above
        cell_a_row, cell_a_col = topleft_cell_row - 1, topleft_cell_col
        if (0 <= cell_a_row < grid.shape[0] and 0 <= cell_a_col < grid.shape[1] and
            grid[cell_a_row, cell_a_col] == 0 and labeled_grid[cell_a_row, cell_a_col] != label_id):
            output_grid[cell_a_row, cell_a_col] = 1
            continue

    return output_grid.tolist()
```
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- The primary function should be named `transform`, which takes the input grid (represented as a Python list of lists) and returns the transformed output grid (also a Python list of lists).
- Include a docstring at the top of the module that contains the natural language description of the transformation rule.
- Use comments to describe the workflow.
- All major math, science and analysis libraries are available to you.
- Include an `if __name__ == '__main__':` block that:
    - Defines the input grid.
    - Defines the expected output grid.
    - Calls the `transform` function with the input grid.
    - Asserts that the transformed output matches the expected output. Print a clear message indicating success or failure.

- if your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Skeleton Template**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

input = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

expected_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

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
