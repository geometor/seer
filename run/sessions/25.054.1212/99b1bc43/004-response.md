# 99b1bc43 • 004 • refine_coder

---
```python
"""
1.  **Input:** A 9x4 grid of integers (0-9) representing colors.
2.  **Output:** A 4x4 grid of integers, derived as follows:
3.  **Process in Sections:** Divide the input grid into four sections:
    *   Section 1: Rows 1 & 2
    *   Section 2: Rows 3 & 4
    *   Section 3: Row 5
    *   Section 4: Rows 6 & 7
    *   Section 5: Rows 8 & 9
4.  **Output Row Generation:**
    *   **Output Row 1:**
        * if either Section 1 or Section 2 has *any* non-zero, non-one value, the entire row is green.
        *   Otherwise, the row is composed of the pixel-wise XOR of the two rows.
    *   **Output Row 2:**
        * if either Section 1 or Section 2 has *any* non-zero, non-one value, the entire row is green.
        *   Otherwise, the row is composed of the pixel-wise XOR of the two rows.
    *   **Output Row 3:** If Row 5 contains all the same non-zero color, the output row is all green.
    *   **Output Row 4**
      * if either Section 4 or Section 5 has *any* non-zero, non-one value, the entire row is green.
      * Otherwise, the row is composed of the pixel-wise XOR of the two rows from Section 4.

5. **XOR rule:** When an output row must derive by using pixel-wise xor, do the following:
  *  if the two pixel have the same value, use 0
  *  otherwise, if there is a non-zero value, pick one color by cycling through the available
      colors (not white)
  * otherwise, if the colors are zero and one, use zero.
"""

import numpy as np

def xor_rows(row1, row2, section1, section2):
    # xor rule implementation
    output_row = []
    
    # get list of available colors, not white
    colors = []
    for r in [row1, row2, section1.flatten(), section2.flatten()]:
        for c in r:
          if c != 0 and c not in colors:
            colors.append(c)
    colors.sort()
    color_index = 0

    for i in range(len(row1)):
        if row1[i] == row2[i]:
            output_row.append(0)
        elif row1[i] != 0 and row2[i] != 0:
          output_row.append(colors[color_index % len(colors)])
          color_index+=1
        elif row1[i] == 0 and row2[i] == 1:
          output_row.append(0)
        elif row1[i] == 1 and row2[i] == 0:
          output_row.append(0)            
        else: # one is zero, other is not, pick that one.
          output_row.append(max(row1[i],row2[i]))
    return np.array(output_row)

def check_for_other_colors(section):
    # check a 2-row section for any colors other than 0 or 1
    unique_colors = np.unique(section)
    for color in unique_colors:
        if color != 0 and color != 1:
            return True  # Found a color other than 0 or 1
    return False

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((4, cols), dtype=int)

    # Section definitions
    section1 = input_grid[0:2, :]
    section2 = input_grid[2:4, :]
    section3 = input_grid[4:5, :]
    section4 = input_grid[5:7, :]
    section5 = input_grid[7:9, :]

    # Output Row 1
    if check_for_other_colors(section1) or check_for_other_colors(section2):
        output_grid[0, :] = 3
    else:
        output_grid[0, :] = xor_rows(input_grid[0,:], input_grid[1,:], section1, section2)

    # Output Row 2
    if check_for_other_colors(section1) or check_for_other_colors(section2):
        output_grid[1, :] = 3
    else:
        output_grid[1, :] = xor_rows(input_grid[2,:], input_grid[3,:], section1, section2)

    # Output Row 3
    unique_colors_row5 = np.unique(input_grid[4, :])
    if len(unique_colors_row5) == 1 and unique_colors_row5[0] != 0:
        output_grid[2, :] = 3
    else:
        output_grid[2, :] = input_grid[4,:] # direct copy

    # Output Row 4
    if check_for_other_colors(section4) or check_for_other_colors(section5):
        output_grid[3, :] = 3
    else:
        output_grid[3, :] = xor_rows(input_grid[5,:], input_grid[6,:], section4, section5) # use 6 and 7

    return output_grid.tolist()
```
