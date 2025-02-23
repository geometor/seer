# 25.045.0822 • 1-3aa6fb7a • 003 example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x70283A50DCC0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x70283A50E140>

*text:*
**Natural Language Description of the Transformation:**

The transformation operates on connected components of color 8 (azure) in the input grid.

1. **Identify Connected Components:** Locate all distinct, contiguous regions of color 8. In this input, there are two such components.
2. **Process First Component:** For the first component encountered (reading order: top to bottom, left to right):
    - **Find Top-Left Cell:** Determine the cell within this component that has the minimum row index. If there are multiple cells with the same minimum row index, choose the one with the minimum column index among them. This is the "top-left" cell of the component.
    - **Change Cell to the Right:**  Identify the cell immediately to the right of the "top-left" cell. If this cell exists within the grid boundaries and its current color is 0 (white), change its color to 1 (blue).
3. **Process Second Component:** For the second component encountered (in reading order):
    - **Find Bottom-Right Cell:** Determine the cell within this component that has the maximum row index. If there are multiple cells with the same maximum row index, choose the one with the maximum column index among them. This is the "bottom-right" cell of the component.
    - **Change Cell to the Left:** Identify the cell immediately to the left of the "bottom-right" cell. If this cell exists within the grid boundaries and its current color is 0 (white), change its color to 1 (blue).
4. **Output Grid:** The grid resulting from these changes is the output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "For the first connected component of color 8, change the cell to the right of its top-left cell to color 1. For the second connected component of color 8, change the cell to the left of its bottom-right cell to color 1."
objects:
  - type: "connected component"
    color: 8
    properties:
      - "shape"
      - "position"
      - "top-left cell"
      - "bottom-right cell"
actions:
  - "identify": "connected components of color 8"
  - "find": "top-left cell of the first component"
  - "change_color": "cell to the right of the top-left cell to color 1 if it is color 0"
  - "find": "bottom-right cell of the second component"
  - "change_color": "cell to the left of the bottom-right cell to color 1 if it is color 0"
predicates:
  - "connected": "cells of the same color are adjacent"
  - "top-left": "cell with minimum row and column index in a component"
  - "bottom-right": "cell with maximum row and column index in a component"
  - "to_the_right_of": "cell is immediately to the right"
  - "to_the_left_of": "cell is immediately to the left"
  - "color_is_0": "cell color is white"
  - "color_is_1": "cell color is blue"
```

*text:*
```python
"""
For the first connected component of color 8, change the cell to the right of its top-left cell to color 1.
For the second connected component of color 8, change the cell to the left of its bottom-right cell to color 1.
"""

import copy

def find_connected_components(grid, color):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = []

    def bfs(r, c, current_component):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != color:
            return
        visited[r][c] = True
        current_component.append((r, c))
        bfs(r + 1, c, current_component)
        bfs(r - 1, c, current_component)
        bfs(r, c + 1, current_component)
        bfs(r, c - 1, current_component)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                current_component = []
                bfs(r, c, current_component)
                components.append(current_component)
    return components

def get_top_left_cell(component):
    top_left_cell = component[0]
    for r, c in component:
        if r < top_left_cell[0] or (r == top_left_cell[0] and c < top_left_cell[1]):
            top_left_cell = (r, c)
    return top_left_cell

def get_bottom_right_cell(component):
    bottom_right_cell = component[0]
    for r, c in component:
        if r > bottom_right_cell[0] or (r == bottom_right_cell[0] and c > bottom_right_cell[1]):
            bottom_right_cell = (r, c)
    return bottom_right_cell

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    components = find_connected_components(input_grid, 8)

    if not components:
        return output_grid

    # Process first component
    first_component = components[0]
    top_left_r, top_left_c = get_top_left_cell(first_component)
    right_c = top_left_c + 1
    if 0 <= right_c < cols and output_grid[top_left_r][right_c] == 0:
        output_grid[top_left_r][right_c] = 1

    if len(components) >= 2:
        # Process second component
        second_component = components[1]
        bottom_right_r, bottom_right_c = get_bottom_right_cell(second_component)
        left_c = bottom_right_c - 1
        if 0 <= left_c < cols and output_grid[bottom_right_r][left_c] == 0:
            output_grid[bottom_right_r][left_c] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x70283A50E050>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x70283A50E320>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
