# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: three separate objects. Two are 2x1 rectangles and one is 1x1
        positions:
          - (0,4) & (0,5) & (1,5) # First rectangle
          - (2,2) & (3,2) # Second rectangle
          - (3,3)  # third rectangle
          - (5,4)  # single cell.
          - (6,3) & (6,4)  # another rect
    background_color: 0 (white)
  output_grid:
    size: 7x7
    objects:
     - color: 8 (azure)
       shape: three separate objects. Two are 2x1 rectangles and one is 1x1
       positions:
          - (0,4) & (0,5) & (1,5) # First rectangle
          - (2,2) & (3,2) # Second rectangle
          - (3,3)  # third rectangle
          - (5,4)  # single cell.
          - (6,3) & (6,4)  # another rect
     - color: 1 (blue)
       shape: three single cells.
       positions:
        - (1,4) # adjacent left to top right object
        - (2,3) # adjacent right to second object
        - (5,3) # adjacent left to fourth object
    background_color: 0 (white)
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, we have multiple distinct azure (color 8) objects with different forms.

2.  **Detect Change:** The transformation involves the introduction of blue (color 1) pixels.

3.  **Predicate for Blue Pixel Placement:** Place the new pixel (with value = 1) adjacent to the azure objects, but the position depends on the shape of the azure objects.

4. **Refine Placement Rule:**
        -   If it is possible to place the new pixel (with value = 1) to the left of the azure object, do so.
        -   Otherwise, Place the new pixel (with value = 1) to the right of the azure object.

```python
"""
The transformation rule is as follows:
1. Identify all azure (color 8) objects in the input grid.
2. Introduce blue (color 1) pixels adjacent to the identified azure objects.
3.  Placement Rule:
    - If possible, place the new pixel (with value = 1) to the left of the azure object.
    - Otherwise, place the new pixel (with value = 1) to the right of the azure object.

"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color in the grid.
    Returns a list of lists, each sublist containing coordinates of an object.
    """
    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects
def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      #sort object by top-left coordinate
      sorted_obj = sorted(obj, key=lambda coord: (min(y for x, y in obj), min(x for x, y in obj)))
      
      #check if the object has one or two elements
      if len(sorted_obj) >= 2:
        # Place blue pixel to the left of the  object
        leftmost = min(sorted_obj, key=lambda coord: coord[1])
        
        #place to left if possible, otherwise to right.
        if leftmost[1] - 1 >= 0:
            if output_grid[leftmost[0], leftmost[1] - 1] == 0:
                output_grid[leftmost[0], leftmost[1] - 1] = 1
            else:
                top_rightmost = max(sorted_obj, key=lambda coord: coord[1])
                output_grid[top_rightmost[0], top_rightmost[1] + 1] = 1  
        else:
            top_rightmost = max(sorted_obj, key=lambda coord: coord[1])
            output_grid[top_rightmost[0], top_rightmost[1] + 1] = 1

      #if it's a single object
      elif len(sorted_obj) == 1:
          leftmost = sorted_obj[0]
          #place to left if possible, otherwise to right.
          if leftmost[1] - 1 >= 0:
            if output_grid[leftmost[0], leftmost[1] - 1] == 0:
                output_grid[leftmost[0], leftmost[1] - 1] = 1
            else:
                output_grid[leftmost[0], leftmost[1] + 1] = 1
          else:
                output_grid[leftmost[0], leftmost[1] + 1] = 1
    
    return output_grid
```

