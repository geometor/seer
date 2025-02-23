# 2-0ca9ddb6 • 005 • example_3 - NLP

---
Okay, let's analyze the third example.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (2, 2)
      shape: single cell
    - color: 1 (blue)
      position: (7, 3)
      shape: single cell
    - color: 6 (magenta)
      position: (5,6)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (2, 2)
      shape: single cell
    - color: 1 (blue)
      position: (7, 3)
      shape: single cell
    - color: 6 (magenta)
      position: (5,6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(1, 1), (1, 3), (3, 1), (3, 3)]
      shape: single cells forming a pattern
    - color: 7 (orange)
      positions: [(6, 2), (7, 2), (8, 2), (7, 4)]
      shape: single cells forming a pattern
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects consisting of a single cell. This includes a red cell at (2, 2), a blue cell at (7, 3) and a magenta cell at (5,6).

2.  **Yellow Surround:** For the red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3.  **Orange Surround:** For the blue cell, create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4. **Preserve all single cells:** The original single cells remain in their original positions in the output grid. The magenta cell is kept.

**Natural Language Program**

1.  Find every object of size 1 in the input.
2.  For each of those objects:
    -   if the object is red:
        -   Place a yellow cell above it.
        -   Place a yellow cell below it.
        - Place a yellow cell at its left.
        - Place a yellow cell diagonally up and to the left
    -   if the object is blue:
        -   Place 3 orange cells to form a vertical line at its left.
        -   Place one orange cell at the bottom-right of the blue cell, with distance 1.
3.  Maintain original objects of size 1.

This transformation rule is consistent with the previous examples, confirming that single objects are sorrounded based on the rules for the red and blue color. Additionally all the single objects are kept, including the magenta cell.
The python implementation does not require changes.

```python
"""
1. Find every object of size 1 in the input, except those of color 8.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
     - Place a yellow cell diagonally up and to the left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1, except those of color 8.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 8:
          continue
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4 # Up and to the left
            if x > 0:
                output_grid[y,x-1] = 4 # to the left
            if x > 0 and y < output_grid.shape[0]-1:   
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
    return output_grid
```

