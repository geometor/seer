# 1-3aa6fb7a • 007 • example_2 - NLP

---
Okay, let's analyze the transformation from the input to the output grid in this second example.

**YAML Description**

```yaml
observations:
  input:
    objects:
      - color: 8 (azure)
        shape: Three separate objects. Two 2x1 vertical rectangles and a 1x2 horizontal rectangle.
        positions:
          - (0,4) and (0,5) # row, column indexing starting from 0
          - (1,5) and (2,5)
          - (2,2) and (3,2)
          - (3,2) and (3,3)
          - (5,4) and (6,4)
          - (6,4) and (6,5)
    grid_size: (7, 7)
  output:
    objects:
      - color: 8 (azure)
        shape: Three separate objects. Two 2x1 vertical rectangles and a 1x2 horizontal rectangle.
        positions:
          - (0,4) and (0,5)
          - (1,5) and (2,5)
          - (2,2) and (3,2)
          - (3,2) and (3,3)
          - (5,4) and (6,4)
          - (6,4) and (6,5)
      - color: 1 (blue)
        shape: single cell
        positions:
            - (1,4)
            - (2,3)
            - (5,3)
    grid_size: (7, 7)

```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we identify three azure (color 8) objects. Two of them are 2x1 vertical rectangles, and one is a 1x2 horizontal rectangle. It could also be described as three azure objects that look like the number "8".
2.  **Preserve Objects:** These three azure objects are preserved in their original locations in the output grid.
3.  **Add Blue cell, first object:** A blue cell (color 1) is added to the output grid to the left of the top cell of the first vertical azure object.
4.  **Add Blue cell, second object:** A blue cell (color 1) is added to the output grid to the left of the top cell of the horizontal azure object.
5.  **Add Blue cell, third object:** A blue cell (color 1) is added to the output grid to the left of the top cell of the second vertical azure object.

**Complete Natural Language Description**

The transformation rule is: The output preserves the azure colored objects and adds a blue pixel adjacent to each azure object, to the left of its top-left corner. This description is slightly different and more concise compared to the first example, and it should generalize.

```python
"""
The output preserves the azure colored objects and adds a blue pixel adjacent to each azure object, to the left of its top-left corner.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find azure objects
    azure_objects = find_objects(input_grid, 8)

    # add blue pixels
    for obj in azure_objects:
        # sort object coordinates to find top-left
        sorted_obj = sorted(obj, key=lambda x: (x[0], x[1]))
        top_left = sorted_obj[0]

        #Add to the left of top left corner
        if top_left[1] - 1 >= 0:
            output_grid[top_left[0], top_left[1] - 1] = 1

    return output_grid
```

