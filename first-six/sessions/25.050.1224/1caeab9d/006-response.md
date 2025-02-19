# 1caeab9d • 006 • example_3 - CODE

---
Okay, let's analyze the transformation from the input grid to the output grid in the third example.

**YAML Description of Observations**

```yaml
input_objects:
  - object_1:
      color: 1 (blue)
      shape: 2x1 rectangle
      position: (2,1) # Top-left corner coordinates
  - object_2:
      color: 2 (red)
      shape: 1x2 rectangle
      position: (1,3)
  - object_3:
      color: 4 (yellow)
      shape: 2x1 rectangle
      position: (3,6)

output_objects:
 - object_1:
      color: 1 (blue)
      shape: 2x1 rectangle
      position: (2,1)
 - object_2:
     color: 2(red)
     shape: 2x1 rectangle
     position: (2,3)
 - object_3:
     color: 4(yellow)
     shape: 2x1 rectangle
     position: (2,6)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can see:
    *   A blue 2x1 rectangle at position (2,1).
    *  Two red cells making a non-contiguous shape at (1,3) and (2,3)
    *   A yellow 2x1 rectangle at position (3,6).

2.  **Transformation:**

    *   The blue object remains in the same position.
    *   The red cell at (1,3) moves down to (2,3). Now the two red cells construct a 2x1 rectangle.
    *   The yellow object remain in place.
    * The objects are re-arranged to reside in rows 2 and 3

3.  **Result:** The output grid contains:
    * A blue 2x1 rectangle at (2,1).
    *  A red 2x1 rectangle at (2,3)
    *   A yellow 2x1 rectangle at (2,6).

**Transformation Rule Summary**
Restructure the red cells to form a contiguous 2x1 rectangle. And put them to row 2.

```python
"""
The transformation involves identifying the blue, red, and yellow single cells/objects and arranging them into 2x1 rectangles in the output grid at row 2 (index 2). The blue and yellow 2x1 retangles maintain their column. The two separated red cells are combined together into a 2x1 rectangle at row 2.
"""

import numpy as np

def find_objects_and_single_cells(grid):
    """Finds 2x1 rectangle objects and separate single cells in the grid."""
    objects = []
    single_cells={}
    rows, cols = grid.shape
    
    #find 2x1 objects
    for r in range(rows - 1):
        for c in range(cols):
            rectangle = grid[r:r+2, c:c+1]
            if np.all(rectangle == rectangle[0,0]) and rectangle[0,0] != 0:
                objects.append({'color': rectangle[0,0], 'position': (r, c), 'shape':(2,1)})

    #find single cell
    for r in range(rows):
        for c in range(cols):
            if grid[r,c]!=0:
                flag=True
                for obj in objects:
                    if r>=obj['position'][0] and r<=obj['position'][0]+obj['shape'][0]-1 and c==obj['position'][1]:
                        flag=False
                        break
                if flag:
                    single_cells[(r,c)]=grid[r,c]

    return objects, single_cells

def transform(input_grid):
    """
    Transforms the input grid by moving the colored cells and aligning them at row 2.
    """
    # Initialize output grid as a zero array with the same shape as the input
    output_grid = np.zeros_like(input_grid)

    # Find the 2x1 rectangle objects and single cells.
    objects, single_cells = find_objects_and_single_cells(input_grid)

    
    #Move each object according to the observed rule
    for obj in objects:
        color = obj['color']
        r, c = obj['position']
        
        if color==1: #blue
            new_row = 2
            output_grid[new_row:new_row+2, c:c+1] = color
        elif color == 4: # yellow
            new_row = 2
            output_grid[new_row:new_row+2, c:c+1] = color
            
    #Move single cells
    red_cells=[]
    for pos, color in single_cells.items():
        r, c = pos
        if color==2:
            red_cells.append((r,c))
            
    #construct 2x1 red rectangle
    if len(red_cells)==2:
        output_grid[2:4, red_cells[0][1]:red_cells[0][1]+1] = 2
        
    return output_grid
```

