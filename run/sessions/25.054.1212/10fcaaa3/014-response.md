# 10fcaaa3 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Expansion:** The input grid is expanded. The output grid is double and one more in width, with the input grid being doubled and then one is added. the height of the output is also doubled, then one added.

2. **Copy and Repetition:** the input is duplicated to a width two times the size of the original, and then the output is repeated, two times,

3.  **Border:** A border of 8's appears around the output.

4.  **Fill:** Around each yellow ('4') pixel in the expanded grid, fill the adjacent '0' (white) pixels with '8' (azure) in a checkerboard like pattern. Specifically, change some remaining '0' pixels to '8' to create the pattern seen. The 8's appear to fill in the spots and connect up to the yellow spots.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape

    # 1. & 2. Expansion and Repetition
    output_rows = 2 * input_rows + 1 + 4 #add 4 for the buffer between repetition and 1 for remainder
    output_cols = 2 * input_cols + 1 + 4 #add 4 for the buffer between repetition and 1 for remainder
    output_grid = np.zeros((output_rows, output_cols), dtype=int)
    
    #copy input and repeat horizontally and vertically
    
    for i in range(2):
        for j in range(2):
            start_row = i * (input_rows + 2 ) #the 2 is the buffer between each box
            start_col = j * (input_cols + 2)
            output_grid[start_row:start_row + input_rows, start_col:start_col + input_cols] = input_grid

    # 3. Border
    output_grid[0, :] = 8
    output_grid[-1, :] = 8
    output_grid[:, 0] = 8
    output_grid[:, -1] = 8

    # 4. Fill
    for r in range(output_rows):
        for c in range(output_cols):
            if output_grid[r, c] == 4:  # Find yellow pixels

                #check to see if cell is at the edge
                if r > 0 :
                    if output_grid[r-1,c] == 0: output_grid[r-1,c] = 8
                if r < output_rows - 1 :
                     if output_grid[r+1,c] == 0: output_grid[r+1,c] = 8
                if c > 0:
                    if output_grid[r,c-1] == 0: output_grid[r,c-1] = 8
                if c < output_cols - 1 :
                    if output_grid[r,c+1] == 0: output_grid[r,c+1] = 8
                
    return output_grid.tolist()
```
