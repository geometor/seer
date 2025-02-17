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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FB2C2111CC0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FB2C2112E30>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate azure 'L' shapes, each composed of three cells."

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate azure 'L' shapes, similar to input."
    - color: 1
      positions: [(1, 2), (4, 4)]
      shape: "Two blue single cells inside L shape's corners."
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we find two distinct "L"-shaped objects made of azure (color 8) cells. Each "L" shape consists of three cells.

2.  **Locate Corners.**: For both azure L shapes, identify their inner corner.

3. **Change Color:** A blue cell (color code 1) is placed inside the corner of each "L".

4.  **Preserve Other Cells:** All other cells in the grid remain unchanged (color 0).

**In summary**: The transformation identifies particular L-shaped patterns and put a blue cell inside each L shape's corner. All other parts of the input are unchanged.


*text:*
```python
"""
The transformation identifies two azure (color 8) "L"-shaped objects in the input grid. 
It then places a blue cell (color 1) inside the corner of each "L". 
All other cells in the grid remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds "L" shapes of a specified color in the grid.
    Returns a list of corner coordinates for each L shape.
    """
    l_corners = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for L shape in all 4 orientations.
            if grid[r, c] == color:
                # Check different orientations of the L shape
                if grid[r + 1, c] == color and grid[r, c + 1] == color :
                    l_corners.append((r,c))
                elif grid[r+1,c] == color and grid[r,c-1] == color:
                      l_corners.append((r,c-1))
                elif grid[r-1,c] == color and grid[r,c+1] == color:
                    l_corners.append((r-1,c))
                elif grid[r-1,c] == color and grid[r, c-1] == color:
                    l_corners.append((r-1, c-1))

            elif grid[r,c+1] == color:
                if grid[r+1,c+1] == color and grid[r-1,c+1] == color:
                    l_corners.append((r-1,c))
            elif grid[r+1,c] == color:
                if grid[r+1, c-1] == color and grid[r+1, c+1] == color:
                    l_corners.append((r,c))
    
    filtered_corners = []
    for corner in l_corners:
        r, c = corner
        # Ensure the corner and its adjacent cells form an L-shape of 3 cells
        count = 0
        if grid[r,c] == color:
          if 0 <= r + 1 < rows and grid[r + 1, c] == color:
              count += 1
          if 0 <= r - 1 < rows and grid[r - 1, c] == color:
              count += 1
          if 0 <= c + 1 < cols and grid[r, c + 1] == color:
              count += 1
          if 0 <= c - 1 < cols and grid[r, c - 1] == color:
              count += 1
          if count == 2: #Check that there's indeed 2 other adjancent cells making the L
              # check diagonal to detect real corners.
              is_real_corner = False
              if 0 <= r+1 < rows and 0 <= c+1 < cols and grid[r+1,c+1] != color:
                  is_real_corner = True

              if 0 <= r+1 < rows and 0 <= c-1 < cols and grid[r+1, c-1] != color:
                  is_real_corner = True
              
              if 0 <= r-1 < rows and 0 <= c+1 < cols and grid[r-1, c+1] != color:
                  is_real_corner = True
              
              if 0 <= r-1 < rows and 0 <= c-1 < cols and grid[r-1, c-1] != color:
                  is_real_corner = True

              if is_real_corner:    
                filtered_corners.append(corner)


    return filtered_corners

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    l_corners = find_l_shapes(input_grid, 8)

    # Place a blue cell (color 1) at the identified corner of each L shape.
    for corner in l_corners:
        r, c = corner
        #find adjacent color 8
        if input_grid[r+1,c] == 8:
            if input_grid[r,c+1] == 8:
              output_grid[r + 1, c + 1] = 1
            elif 0<= c-1 and input_grid[r,c-1] == 8:
              output_grid[r+1,c-1] = 1
        elif 0 <= r-1 and input_grid[r-1,c] == 8:
            if input_grid[r,c+1] == 8:
                output_grid[r-1,c+1] = 1
            elif 0 <= c-1 and input_grid[r,c-1] == 8:
                output_grid[r-1,c-1] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FB2C2111C60>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7FB2C2111870>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
