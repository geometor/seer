# 99b1bc43 • 012 • refine_coder

---
```python
"""
1.  **Divide:** Divide the input grid into four equal quadrants (Q1: top-left, Q2: top-right, Q3: bottom-left, Q4: bottom-right). If the input grid has an odd number of rows or columns, the extra row/column is included in the bottom/right quadrants, respectively.

2.  **Analyze Quadrants:** For each 2x2 quadrant in the output grid, examine the corresponding quadrant in the input grid.

3.  **Output Generation:**
    *   Examine each 2x2 quadrant of the *output* grid (top-left, top-right, bottom-left, bottom-right).
    *   The corresponding input quadrants will not map directly by index, but by their relative positions: top-left output corresponds to top-left input, etc.
    *   If the corresponding input quadrant contains *any* non-zero pixels, then examine the layout:

    *   If the non-zero colors are present in only Q1 of the Input, output[0,0] = 3
    *   If the non-zero colors are present in only Q2 of the Input, output[0,3] = 3
    *   If the non-zero colors are present in only Q3 of the Input, output[3,0] = 3
    *   If the non-zero colors are present in only Q4 of the Input, output[3,3] = 3
    *   If the non-zero colors are in multiple quadrants in input, combine them according to their corresponding locations in the output grid:
    *     If non-zero values present in Q1 and Q2 of input, the first row of output is [3,3]
    *     If non-zero values present in Q1 and Q3 of input, the first and last columns are [3,0,0,3]
    *     If non-zero values present in Q3 and Q4 of input, the last row of output is [3,3]

4.  **Result:** The output is a 4x4 grid where each cell is either 0 (white) or 3 (green). The green cells indicate the presence (and combined location) of non-zero colored regions in the corresponding input quadrants.
"""

import numpy as np

def get_quadrant(input_grid, row_start, row_end, col_start, col_end):
    return input_grid[row_start:row_end, col_start:col_end]

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((4, 4), dtype=int)

    # Define quadrant boundaries
    row_mid = rows // 2
    col_mid = cols // 2

    # Quadrant checks
    q1_non_zero = np.any(get_quadrant(input_grid, 0, row_mid, 0, col_mid) != 0)
    q2_non_zero = np.any(get_quadrant(input_grid, 0, row_mid, col_mid, cols) != 0)
    q3_non_zero = np.any(get_quadrant(input_grid, row_mid, rows, 0, col_mid) != 0)
    q4_non_zero = np.any(get_quadrant(input_grid, row_mid, rows, col_mid, cols) != 0)

    # Output generation based on quadrant analysis
    if q1_non_zero:
        output_grid[0, 0] = 3
    if q2_non_zero:
        output_grid[0, 3] = 3
    if q3_non_zero:
        output_grid[3, 0] = 3
    if q4_non_zero:
        output_grid[3, 3] = 3

    # Combine quadrants
    if q1_non_zero and q2_non_zero:
        output_grid[0,:] = [3,3,3,3] # Fill top row
    if q1_non_zero and q3_non_zero:
        output_grid[:,0] = [3,3,3,3] # Fill left column
    if q3_non_zero and q4_non_zero:
        output_grid[3,:] = [3,3,3,3]  #Fill bottom row
    if q2_non_zero and q4_non_zero:
      output_grid[:,3] = [3,3,3,3] #Fill right column

    # more combinations
    if q1_non_zero and q2_non_zero and q3_non_zero:
      output_grid[0:2,0:2] = np.full((2,2), 3)
      output_grid[0,:] = [3,3,3,3] # Fill top row
      output_grid[3,0] = 3 # Q3
      output_grid[:,0] = [3,3,3,3] # Fill left column

    if q1_non_zero and q2_non_zero and q4_non_zero:
      output_grid[0:2,0:2] = np.full((2,2), 3)
      output_grid[0,:] = [3,3,3,3] # Fill top row
      output_grid[:,3] = [3,3,3,3] # Fill left column
      output_grid[3,3] = 3 # Q3

    if q1_non_zero and q3_non_zero and q4_non_zero:
      output_grid[2:4,2:4] = np.full((2,2), 3)
      output_grid[0,0] = 3
      output_grid[:,0] = [3,3,3,3]
      output_grid[3,:] = [3,3,3,3]

    if q2_non_zero and q3_non_zero and q4_non_zero:
      output_grid[3,3] = 3 # q4
      output_grid[:,3] = [3,3,3,3]
      output_grid[3,:] = [3,3,3,3]
      output_grid[2:4,0:2] = np.full((2,2), 3)

    if q1_non_zero and q2_non_zero and q3_non_zero and q4_non_zero:
      output_grid = np.full((4, 4), 3)


    return output_grid.tolist()
```

