# 3befdf3e • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 2 # Red
      shape: rectangle
      position: (3,3)
      size: (4,4)
      properties:
        - Contains a 2x2 orange (7) square in the center.
    - color: 7 # Orange
      shape: rectangle
      position: (4,4)
      size: (2,2)

output_grid:
  objects:
    - color: 2 # Red
      shape:  "cross-like" or plus sign + surrounding cells
      position: (1,3) #relative
      size: (7,4) #approximate, the filled area
      properties:
        - Contains a larger, more complex orange shape, formed around the initial orange object
    - color: 7 # Orange
      shape: "cross-like" or plus sign
      position: (3,3)
      size: (3,4)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the core objects:**
    *   A 4x4 red (color 2) rectangle.
    *   A 2x2 orange (color 7) square inside the red rectangle.

2.  **Describe Object Interactions, Predicates, and Actions:**
    *   The 2x2 orange square expands. It expands to a cross-like shape, composed of orange at the center and four "arms" extending north, south, east and west. The vertical "arm" is of length three.
    *   The red shape expands vertically and horizontally. The top and bottom rows of the red shape are copied up/down by one row. And an additional two cells on each side appear to make the final shape.

3.  **Transformation as Action:**
    -   The orange 2x2 shape transforms into a cross, keeping its center, and expanding up, down and sideways.
    -    The red cells 'move' to accommodate and surround the new shape of the orange object.
**Transformation Rule Summary**

The transformation involves two main actions: The inner orange square expands into a cross-like shape, and the outer red rectangle expands and reshapes to fit and to surround the expanded orange object.

```python
"""
The transformation involves two main actions: The inner orange square expands into a cross-like shape, and the outer red rectangle expands and reshapes to fit and to surround the expanded orange object.
"""
import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the orange object
    orange_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 7:
                orange_coords.append((r, c))

    # Expand the orange object into cross shape
    if orange_coords:
      min_or = min(r for r,c in orange_coords)
      max_or = max(r for r,c in orange_coords)
      min_oc = min(c for r,c in orange_coords)
      max_oc = max(c for r,c in orange_coords)

      center_r = (min_or + max_or) //2
      center_c = (min_oc + max_oc) //2

      #central square
      for r in range(rows):
        for c in range(cols):
          if input_grid[r,c] == 7:
            output_grid[r,c] = 7
      #vertical arm
      output_grid[center_r -1, center_c] = 7
      output_grid[center_r -1, center_c + 1] = 7

    # find red object
    red_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 2:
              red_coords.append((r,c))
    if red_coords:
      min_rr = min(r for r, c in red_coords)
      max_rr = max(r for r, c in red_coords)
      min_rc = min(c for r, c in red_coords)
      max_rc = max(c for r, c in red_coords)
      # copy first and last rows
      for c in range(min_rc, max_rc+1):
        if min_rr > 0:
            output_grid[min_rr-1, c] = 2
        if max_rr < rows -1:
            output_grid[max_rr+1,c] = 2
      # add columns
      for r in range(min_rr-1, max_rr + 2):

          if min_oc > 0:
              output_grid[r,min_oc-1] = 2
          if max_oc < cols-1:
              output_grid[r,max_oc+2] = 2

          if 0 <= r < rows:
              if min_rc>0:
                  output_grid[r,min_rc-1] = 2
              if max_rc < cols -1:
                  output_grid[r,max_rc+1] = 2

    return output_grid
```

