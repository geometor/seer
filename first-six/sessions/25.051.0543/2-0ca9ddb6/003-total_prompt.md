# 2-0ca9ddb6 • 003 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(2, 1), (2, 3), (4, 1), (4, 3)]
      shape: four single cells forming a pattern around red
    - color: 7 (orange)
      positions: [(5, 5), (6, 5), (7, 5), (6, 7)]
      shape: four single cells in L-shape around the blue object
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell. In this case, we have a red cell at (3, 2) and a blue cell at (6, 6).

2.  **Yellow Surround:** For the red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3. **Orange Surround:** For the blue cell create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4.  **Preserve Original Objects:** The original red and blue cells remain in their original positions in the output grid.

**Natural Language Program**
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.

```python
"""
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell two positions to its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.
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
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4
            if x > 0:
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

**input**
```
0 0 0 8 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0 0
0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 8 0 0 0 0 0
0 0 0 0 0 4 0 4 0
0 0 7 0 0 0 2 0 0
0 7 1 7 0 4 0 4 0
0 0 7 0 0 0 0 0 0
0 0 0 0 0 0 7 0 0
4 0 4 0 0 7 1 7 0
0 2 0 0 0 0 7 0 0
4 0 4 0 0 0 0 0 0
```

![Image](002-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
