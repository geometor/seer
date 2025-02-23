# 1a07d186 • 004 • example_2 - CODE

---
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_observations:
  - object_1:
      color: 3 (green)
      shape: vertical line
      position: column 4
      length: 18
  - object_2:
      color: 4 (yellow)
      shape: vertical line
      position: column 13
      length: 18
  - object_3:
      color: 2 (red)
      shape: single cell
      position: (11,8)
  - object_4:
        color: 4
        shape: single cell
        position: (4,2)
  - object_5:
        color: 3
        shape: single cell
        position: (12, 17)

output_observations:
   - object_1:
      color: 3 (green)
      shape: vertical line
      position: column 4
      length: 18
   - object_2:
      color: 4 (yellow)
      shape: vertical line
      position: column 13
      length: 18
   - object_3:
      color: 3,
      shape: single cell
      position: (4,5)
   - object_4:
      color: 4,
      shape: single cell
      position: (4,14)      
   - object_5:
      color: 4,
      shape: single cell
      position: (8, 12)      
   - object_6:
      color: 3,
      shape: single cell
      position: (12,5)          
```

**Natural Language Program: Transformation Rule**

1.  **Identify Persistent Objects:** There are two primary persistent objects: a green vertical line (color 3) in column 4 and a yellow vertical line (color 4) in column 13. These remain unchanged in terms of shape, color, and position.

2.  **Copy, move and change color**: Every other color, different from 3 and 4 will:

    *   Be deleted if they exist.
    *    If they are green or yellow, two copies of them must be made next to the green and yellow columns respectively, to the right of the green column and to the left of the yellow one.

**Step-by-step explanation based on the example:**

*   The red cell (2) is removed.
*    The single green cell at (12,17) will be moved to (12,5)
*    The single yellow cell at (4,2) will be moved to (4,14) and (8,12).


```python
"""
The transformation rule is as follows:
1. Two vertical lines, one green (color 3) in column 4 and one yellow (color 4) in column 13, remain unchanged.
2. Every other color, different from 3 and 4 will:
    *   Be deleted if they exist.
    *   If they are green or yellow, two copies of them must be made next to the green and yellow columns respectively, to the right of the green column and to the left of the yellow one.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)

    # Find the green and yellow lines
    green_line_col = 4
    yellow_line_col = 13
   
    # Iterate the input
    for r in range(input_grid.shape[0]):
      for c in range(input_grid.shape[1]):
        # Keep green and yellow columns
        if c == green_line_col and input_grid[r,c] == 3:
           output_grid[r,c] = 3          
        elif c == yellow_line_col and input_grid[r,c] == 4:
           output_grid[r,c] = 4   
        # Move other single cells       
        elif input_grid[r,c] == 3 and c != green_line_col:
          output_grid[r,c] = 0
          output_grid[r, green_line_col + 1] = 3
        elif input_grid[r,c] == 4 and c!= yellow_line_col:
          output_grid[r,c] = 0
          output_grid[r, yellow_line_col - 1] = 4
        elif input_grid[r,c] != 3 and input_grid[r,c] != 4:
          output_grid[r,c] = 0

    return output_grid
```

