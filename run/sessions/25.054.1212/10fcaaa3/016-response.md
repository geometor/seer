# 10fcaaa3 • 016 • refine_coder

---
```python
"""
1.  **Duplication:** The input grid is duplicated to create a 2x2 grid pattern. This means the output grid's dimensions are exactly twice the input grid's dimensions in both height and width.
2. **Copy to output:** The input is copied to all four quadrants of the output.
3. **Fill with 8's** Fill spaces with 8's between copied patterns to connect them into a complete grid.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape

    # 1. Duplication: Calculate output grid size.
    output_rows = 2 * input_rows
    output_cols = 2 * input_cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # 2. Copy to output: Copy the input grid to the four quadrants.
    for i in range(2):
        for j in range(2):
            start_row = i * input_rows
            start_col = j * input_cols
            output_grid[start_row:start_row + input_rows, start_col:start_col + input_cols] = input_grid

    # 3. Fill with 8's: Connect with 8's.
    for r in range(output_rows):
        for c in range(output_cols):
             if output_grid[r, c] == 0:
                if r > 0 and (output_grid[r-1,c] != 0 and output_grid[r-1,c] != 8) :
                    output_grid[r,c] = 8
                elif r < output_rows -1 and (output_grid[r+1,c] != 0 and output_grid[r+1,c] != 8) :
                    output_grid[r,c] = 8
                elif c > 0 and (output_grid[r,c-1] != 0 and output_grid[r,c-1] != 8):
                    output_grid[r,c] = 8
                elif c < output_cols -1 and (output_grid[r,c+1] != 0 and output_grid[r,c+1] != 8):
                    output_grid[r,c] = 8
                

    return output_grid.tolist()
```
