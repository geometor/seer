# 5c0a986e • 003 • example_2 - NLP

---
Okay, let's analyze the second transformation example.

**YAML Summary of Observations**

```yaml
input_objects:
  red_square:
    color: 2 (red)
    shape: square (2x2)
    position: (0,2)
  blue_square:
    color: 1 (blue)
    shape: square (2x2)
    position: (7,6)

output_objects:
  red_square:
    color: 2 (red)
    shape: square (2x2)
    position: (0,2)
  blue_square:
    color: 1 (blue)
    shape: square (2x2)
    position: (7,6)
  extra_blue:
    color: 1
    shape: single cell
    positions: [(1,0), (2,1), (3,2), (4,3), (5,4), (6,5)]
  extra_red:
    color: 2
    shape: single cell
    positions:  [(2,5), (3,6), (4,7), (5,8), (7,9)]
```

**Natural Language Program**

1.  **Identify Objects:** The input contains:
    *   A 2x2 red square (color 2) at (0,2).
    *   A 2x2 blue square (color 1) at (7,6).

2.  **Preservation:** These two squares are preserved in the output at their original locations.

3.  **Diagonal of Blue Pixels:** A diagonal line of single blue pixels (color 1) is added, starting from the top-left and going down. The positions are (1,0), (2,1), (3,2), (4,3), (5,4), and (6,5).

4. **Diagonal of Red Pixels:** A diagonal line of red pixels (color 2) are added to the output grid starting two to the right of the first extra added blue pixel. The position are (2,5), (3,6), (4,7), (5,8) and (7,9). Notice that the position (6,8) is skiped.

**Summary of Transformation**
The two main squares keep their position and two diagonals are added, starting outside of the top-left square and the bottom-right square.

```python
import numpy as np

def transform2(input_grid):

    output_grid = np.copy(input_grid)

    #Diagonal blue
    for i in range(6):
        output_grid[1+i,i] = 1
    #Diagonal red
    output_grid[2,5] = 2
    output_grid[3,6] = 2
    output_grid[4,7] = 2
    output_grid[5,8] = 2
    output_grid[7,9] = 2

    return output_grid

```

