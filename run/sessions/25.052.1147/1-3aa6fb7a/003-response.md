# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the transformation from the second input grid to the output grid.

**YAML Block: Observations**

```yaml
observations:
  input_grid:
    objects:
      - color: 8 (azure)
        shape:  vertical and horizontal rectangles, mixed
        positions:
          - top_left: [0,4] # 1x2 horizontal
          - top_left: [2,2] # 2x1 verical
          - top_left: [5,5] # 2x1 reversed L
          - top_left: [6,3]

        notes: The azure objects are not uniform this time
    dimensions: [7, 7]
  output_grid:
    objects:
      - color: 8 (azure)
        shape: vertical and horizontal rectanges, mixed
        positions:
            - top_left: [0,4] # 1x2 horizontal
            - top_left: [2,2] # 2x1 verical
            - top_left: [5,5] # 2x1 reversed L
            - top_left: [6,3]
        notes: The azure objects are identical
      - color: 1 (blue)
        shape: three separate 1x1 squares
        positions:
            - top_left: [1, 4]
            - top_left: [2, 3]
            - top_left: [5, 3]
    dimensions: [7, 7]
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:** In the input grid, we see multiple objects made of color 8 (azure). These are of different shapes.

2.  **Preserve Existing:**  All the azure (8) objects in the input grid remain unchanged in the output grid. Their shapes and positions remain the same.

3.  **Detect Change:** We observe that the new color blue (1) appears in the output that was not there before.

4. **Add New Object:** For each vertical or horizontal segment of the azure color, add blue (1) in an adjacent column.
  - If we consider the top azure object starting at \[0,4]. This object is horizontal so we add blue (1) immediately to its left or to its right. In the output, the blue appears to the left at \[1,4].
  - The vertical segment starting at \[2,2]. Blue is added to its right at \[2,3]
  - The vertical segment starting at \[5,5]. Blue is added to its left \[5, 4]

**Natural Language Summary**

The transformation preserves all existing azure (8) objects, adding a blue (1) pixel immediately adjacent to each of them. The new pixel is added either immediately to the left or right depending on the orientation of the existing azure object.

```python
"""
The transformation preserves all existing azure (8) objects. It adds a blue (1) pixel immediately to the left or to the right of the azure rectangle.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find the azure (8) objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the found azure objects
    for obj in azure_objects:
        # Sort the coordinates to find top-left and dimensions
        sorted_coords = sorted(obj, key=lambda x: (x[0], x[1]))
        top_left = sorted_coords[0]
        
        # Determine placement based on object position
        
        #Vertical segment
        if len(obj) > 1 and obj[0][1] == obj[1][1]:
            output_grid[top_left[0], top_left[1] + 1] = 1
        
        #horizontal segment
        elif len(obj) > 1 and obj[0][0] == obj[1][0]:
            output_grid[top_left[0], top_left[1] - 1] = 1
        
        #Single pixel segments, determine position
        else:
            if top_left[0] < input_grid.shape[0] / 2 :
                output_grid[top_left[0], top_left[1] - 1] = 1
            
            else:
                rightmost = max(obj, key=lambda x: x[1])[1]
                output_grid[top_left[0], rightmost] = 1
    return output_grid
```

