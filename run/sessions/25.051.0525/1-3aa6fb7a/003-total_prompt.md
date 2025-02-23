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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 rectangles
        positions:
          - top_left: [1,1]
          - top_left: [3,4]
      - color: 0 (white)
        shape: background
        positions:
          - all cells not occupied by color 8
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 rectangles
        positions:
          - top_left: [1,1]
          - top_left: [3,4]
      - color: 1 (blue)
        shape: single cells
        positions:
          - top_left: [1,2]
          - top_left: [4,4]
      - color: 0 (white)
        shape: background
        positions:
          - all cells not occupied by color 8 or 1
```

**Natural Language Program:**

1.  **Identify Objects:** In the input grid, we have two distinct objects of color 8 (azure). These objects are 2x1 rectangles. One is located at the top-left corner (1, 1), and the second at position (3,4).

2.  **Detect Changes**: Comparing the input and output, we can see that a color 1 (blue) cell has been added to the right of the top rectangle (at [1,2]). We can see that the other color 1 (blue) cell is added to the left of the bottom rectangle (at [4,4]).

3. **Transformation Rule:**
    -   For the top azure rectangle, add a blue cell to the immediate right of the rectangle.
    -   For the bottom azure rectangle, add a blue cell to the immediate left of the rectangle.

**Summary**

The program identifies each 2x1 azure rectangle. For the topmost rectangle, add a blue cell to the immediate right. For the bottommost rectangle, add a blue cell to the immediate left.

```python
"""
The program identifies each 2x1 azure rectangle. For the topmost rectangle, add a blue cell to the immediate right. For the bottommost rectangle, add a blue cell to the immediate left.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
    objects = []
    visited = set()

    def is_valid(pos):
        return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]

    def dfs(pos, current_object):
        if not is_valid(pos) or grid[pos] != color or pos in visited:
            return
        visited.add(pos)
        current_object.append(pos)
        neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                     (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        for neighbor in neighbors:
            dfs(neighbor, current_object)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color and (i, j) not in visited:
                current_object = []
                dfs((i, j), current_object)
                objects.append(current_object)
    return objects

def is_2x1_rectangle(obj, grid):
   # checks that shape is a 2x1 rectangle
    if len(obj) != 2:
        return False
    coords = np.array(obj)
    min_row, min_col = np.min(coords, axis=0)
    max_row, max_col = np.max(coords, axis=0)

    return (max_row - min_row == 1 and max_col - min_col == 0) or \
           (max_row - min_row == 0 and max_col - min_col == 1)

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Filter for 2x1 rectangles
    rectangles_2x1 = [obj for obj in azure_objects if is_2x1_rectangle(obj, input_grid)]
    
    # Sort rectangles based on their top-left corner's row, then column
    rectangles_2x1.sort(key=lambda obj: (min(r for r, _ in obj), min(c for _, c in obj)))
    
    # Process the rectangles
    if len(rectangles_2x1) >= 1:
        # Top rectangle: Add a blue cell to the immediate right
        top_rect = rectangles_2x1[0]
        top_rect_coords = np.array(top_rect)
        top_right_coord = (top_rect_coords[0,0], np.max(top_rect_coords[:, 1]) + 1)

        
        if 0 <= top_right_coord[0] < output_grid.shape[0] and 0 <= top_right_coord[1] < output_grid.shape[1]:
            output_grid[top_right_coord] = 1

    if len(rectangles_2x1) >= 2:

        # Bottom rectangle, add a blue cell immediately to the left.
        bottom_rect = rectangles_2x1[1]
        bottom_rect_coords = np.array(bottom_rect)

        bottom_left_coord = (bottom_rect_coords[0,0], np.min(bottom_rect_coords[:, 1]) - 1)

        if 0 <= bottom_left_coord[0] < output_grid.shape[0] and 0<= bottom_left_coord[1] < output_grid.shape[1]:
            output_grid[bottom_left_coord] = 1

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

![Image](002-example_2_input.png)


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

![Image](002-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
