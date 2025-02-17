# 25.045.0652 • 1-3aa6fb7a • 003 example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x753240211690>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x753240211A20>

*text:*
**Natural Language Program:**

The task is to modify the grid based on connected regions of color '8' (azure).
First, identify all distinct connected components of cells containing the value '8'. Connectivity is defined by adjacency (horizontally or vertically).
For each connected component of '8's:
  1. Find the topmost-leftmost cell within this component. This is the cell with the minimum row index, and among those with the same minimum row index, the minimum column index. Let's call this cell the 'anchor' cell.
  2. Check the cell immediately to the right of the 'anchor' cell. If this cell is within the grid boundaries and its value is '0' (white), change its value to '1' (blue).
  3. Check the cell immediately below the 'anchor' cell. If this cell is within the grid boundaries and its value is '0' (white), change its value to '1' (blue).

This process is applied independently to each connected component of '8's in the input grid to produce the output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "For each connected component of color '8', identify the topmost-leftmost cell. Change the value of the cell immediately to its right to '1' if it's '0', and change the value of the cell immediately below it to '1' if it's '0'."
objects:
  - type: "connected component"
    color: 8
    properties:
      - "topmost-leftmost cell"
actions:
  - "identify connected components of color '8'"
  - "find topmost-leftmost cell in each component"
  - "check cell to the right and below the topmost-leftmost cell"
  - "if cell is '0', change to '1'"
```

*text:*
```python
"""
For each connected component of color '8', identify the topmost-leftmost cell.
Change the value of the cell immediately to its right to '1' if it's '0',
and change the value of the cell immediately below it to '1' if it's '0'.
"""

import collections

def get_connected_components(grid, color):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                component = []
                q = collections.deque([(r, c)])
                visited[r][c] = True
                while q:
                    row, col = q.popleft()
                    component.append((row, col))
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == color and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                components.append(component)
    return components

def get_topmost_leftmost_cell(component):
    topmost_row = float('inf')
    leftmost_col = float('inf')
    anchor_cell = None
    for r, c in component:
        if r < topmost_row:
            topmost_row = r
            leftmost_col = c
            anchor_cell = (r, c)
        elif r == topmost_row and c < leftmost_col:
            leftmost_col = c
            anchor_cell = (r, c)
    return anchor_cell

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [row[:] for row in input_grid] # Create a copy

    components = get_connected_components(input_grid, 8)
    for component in components:
        anchor_cell = get_topmost_leftmost_cell(component)
        if anchor_cell:
            r, c = anchor_cell
            # Check right
            if c + 1 < cols and output_grid[r][c + 1] == 0:
                output_grid[r][c + 1] = 1
            # Check below
            if r + 1 < rows and output_grid[r + 1][c] == 0:
                output_grid[r + 1][c] = 1
    return output_grid


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

<PIL.Image.Image image mode=RGB size=448x448 at 0x753240211C00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7532402120E0>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
