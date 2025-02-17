# 25.045.0644 • 1-3aa6fb7a • 004 example_2 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7E32A281D630>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7E32A281D9C0>

*text:*
**Natural Language Program:**

1. **Identify '8'-objects:** Find all connected regions of cells with color '8' in the input grid. We can consider these as distinct objects.
2. **Locate Top-Left Cell:** For each '8'-object, determine its "top-left most" cell. This is the cell within the object with the smallest row index, and among those with the smallest row index, the smallest column index.
3. **Sequential Modification:**
    - For the *first* '8'-object identified:  Examine the cell immediately to the right of its top-left cell. If this cell is within the grid boundaries and its color is '0', change its color to '1'.
    - For the *second* '8'-object identified: Examine the cell immediately below its top-left cell. If this cell is within the grid boundaries and its color is '0', change its color to '1'.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle"
transformation_rule: "Modify cells adjacent to connected '8' regions."
objects:
  - type: "connected region"
    color: 8
    properties:
      - "connectivity"
      - "top-left most cell"
actions:
  - action_type: "change_color"
    target_object: "cell adjacent to '8'-object's top-left cell"
    new_color: 1
    conditions:
      - "target cell is within grid boundaries"
      - "target cell's original color is 0"
transformation_steps:
  - "Identify connected regions of color '8'."
  - "For each region, find the top-left most cell."
  - "For the first region, change the cell to the right of its top-left cell to '1' if possible."
  - "For the second region, change the cell below its top-left cell to '1' if possible."
```

*text:*
```python
"""
Identifies connected regions of color '8' and modifies cells adjacent to their top-left cells.
For the first '8'-object, changes the cell to its right to '1'.
For the second '8'-object, changes the cell below it to '1'.
Modifications are only applied if the target cell is within grid boundaries and is '0'.
"""

import numpy as np

def transform(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid = np.copy(input_grid_np)
    rows, cols = input_grid_np.shape
    visited = np.zeros_like(input_grid_np, dtype=bool)
    components = []

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
        return neighbors

    def find_connected_component(r, c):
        component = []
        q = [(r, c)]
        visited[r, c] = True
        while q:
            row, col = q.pop(0)
            component.append((row, col))
            for nr, nc in get_neighbors(row, col):
                if input_grid_np[nr, nc] == 8 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    q.append((nr, nc))
        return component

    for r in range(rows):
        for c in range(cols):
            if input_grid_np[r, c] == 8 and not visited[r, c]:
                components.append(find_connected_component(r, c))

    for i, component in enumerate(components[:2]): # Process only the first two components
        top_left_cell = None
        min_row = float('inf')
        min_col = float('inf')
        for r, c in component:
            if r < min_row:
                min_row = r
                min_col = c
                top_left_cell = (r, c)
            elif r == min_row and c < min_col:
                min_col = c
                top_left_cell = (r, c)

        if top_left_cell:
            tl_r, tl_c = top_left_cell
            if i == 0: # First component: modify cell to the right
                target_r, target_c = tl_r, tl_c + 1
                if 0 <= target_r < rows and 0 <= target_c < cols and output_grid[target_r, target_c] == 0:
                    output_grid[target_r, target_c] = 1
            elif i == 1: # Second component: modify cell below
                target_r, target_c = tl_r + 1, tl_c
                if 0 <= target_r < rows and 0 <= target_c < cols and output_grid[target_r, target_c] == 0:
                    output_grid[target_r, target_c] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7E32A281DBA0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7E32A281D390>

*text:*
**Natural Language Program:**

1. **Identify '8'-objects:** Find all connected regions of cells with color '8' in the input grid. Consider each connected region as a distinct object.
2. **Order Objects:** Order the identified '8'-objects based on their discovery order during a typical connected component finding algorithm (e.g., top-to-bottom, left-to-right scan).
3. **Iterate through '8'-objects:** For each '8'-object in the determined order:
    a. **Find Top-Left Cell:** Locate the top-left most cell within the current '8'-object.
    b. **Cycle Directions:** Use a cyclic sequence of directions: right, down, left, up.
    c. **Attempt Modification with Directions:** For each direction in the cycle, starting with right for the first object, down for the second, left for the third, up for the fourth, and then repeating the cycle:
        - Check the cell immediately adjacent to the top-left cell in the current direction.
        - If this adjacent cell is within the grid boundaries and its current color is '0', change its color to '1'.
        - Once a cell is successfully changed to '1', stop attempting further directions for the current '8'-object and proceed to the next '8'-object in the sequence.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle"
transformation_rule: "Modify cells adjacent to connected '8' regions in a cyclic direction pattern."
objects:
  - type: "connected region"
    color: 8
    properties:
      - "connectivity"
      - "top-left most cell"
      - "discovery order"
actions:
  - action_type: "change_color"
    target_object: "cell adjacent to '8'-object's top-left cell"
    new_color: 1
    conditions:
      - "target cell is within grid boundaries"
      - "target cell's original color is 0"
transformation_steps:
  - "Identify and order connected regions of color '8'."
  - "For each region, find the top-left most cell."
  - "Apply cyclic directions (right, down, left, up) based on the region's order."
  - "For each direction, check the adjacent cell; if valid and color '0', change to '1' and proceed to the next region."
```
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- Follow the template below
- If your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Transform Template:**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

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
