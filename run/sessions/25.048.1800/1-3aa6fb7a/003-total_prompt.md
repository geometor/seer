# 1-3aa6fb7a • 003 • example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F516190F70>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F5161907F0>

*text:*
**Natural Language Program:**

1. **Identify Objects:** Detect all connected regions of color 8 (azure) in the input grid. These regions are considered as distinct objects.
2. **Sort Objects:** Order the identified objects from left to right based on their horizontal position. The horizontal position of an object is determined by the minimum column index among all cells belonging to that object.
3. **Leftmost Object Action:** For the object that is leftmost in the sorted order:
    - Find its topmost cell. The topmost cell is the cell with the minimum row index among all cells of this object.
    - Locate the cell immediately to the right of this topmost cell. If this cell is within the grid boundaries, change its color to 1 (blue).
4. **Rightmost Object Action:** For the object that is rightmost in the sorted order:
    - Find its bottommost cell. The bottommost cell is the cell with the maximum row index among all cells of this object.
    - Locate the cell immediately to the left of this bottommost cell. If this cell is within the grid boundaries, change its color to 1 (blue).
5. **Output:** The grid obtained after applying these changes is the output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify connected components of color 8, sort them horizontally, and modify cells adjacent to the leftmost and rightmost components."
objects:
  - type: "connected region"
    color: 8 # azure
predicates:
  - "connected": "cells of the same color are adjacent (horizontally or vertically)"
  - "leftmost": "object with the minimum starting column index"
  - "rightmost": "object with the maximum starting column index"
  - "topmost": "cell with the minimum row index within an object"
  - "bottommost": "cell with the maximum row index within an object"
actions:
  - "identify": "detect connected regions of color 8"
  - "sort": "order objects based on their leftmost column"
  - "change_color": "modify cell color to 1 (blue)"
  - "locate_adjacent_cell": "find cell immediately to the right or left of a given cell"
steps:
  - "Identify all connected components of color 8."
  - "Sort these components based on their minimum column index (left to right)."
  - "For the leftmost component, find its topmost cell and change the color of the cell immediately to its right to 1."
  - "For the rightmost component, find its bottommost cell and change the color of the cell immediately to its left to 1."
```

*text:*
```python
"""
Identifies connected regions of color 8 (azure) in the input grid, sorts them horizontally, and changes the color of specific adjacent cells to 1 (blue).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected components of the specified color in the grid.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def sort_objects(objects):
    """
    Sorts objects based on their leftmost column.
    """
    return sorted(objects, key=lambda obj: min(col for _, col in obj))

def get_topmost_cell(object_cells):
    """Returns the topmost cell (min row index) of an object."""
    return min(object_cells, key=lambda cell: cell[0])

def get_bottommost_cell(object_cells):
    """Returns the bottommost cell (max row index) of an object."""
    return max(object_cells, key=lambda cell: cell[0])

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8
    objects = find_objects(output_grid, 8)
    
    # Sort objects from left to right
    sorted_objects = sort_objects(objects)
    
    # Process leftmost object
    if sorted_objects:
        leftmost_object = sorted_objects[0]
        topmost_cell = get_topmost_cell(leftmost_object)
        right_neighbor = (topmost_cell[0], topmost_cell[1] + 1)
        if 0 <= right_neighbor[1] < output_grid.shape[1]:
            output_grid[right_neighbor] = 1
    
    # Process rightmost object
    if len(sorted_objects) >= 1:  #Corrected the condition
        rightmost_object = sorted_objects[-1]
        bottommost_cell = get_bottommost_cell(rightmost_object)
        left_neighbor = (bottommost_cell[0], bottommost_cell[1] - 1)
        if 0 <= left_neighbor[1] < output_grid.shape[1]:
            output_grid[left_neighbor] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F51601AB00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F51601AAD0>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
