# bbc9ae5d • 024 • refine_coder

---
```python
"""
1.  **Input:** The input is a single-row grid.
2.  **Identify Non-Zero Sequence:** Determine the sequence of non-zero colored pixels at the beginning of the input row. Also note the sequence of trailing zero-colored pixels.
3.  **Determine Number of output rows.** Determine the length of the full input. Also determine the number of output rows based on the non zero sequence. Output rows continue until the non-zero sequence fills the output row width.
4.  **Create Output Rows:** Create a series of output rows.
5.  **Extend Sequence:**
    *   The first output row is a copy of the input row.
    *   For each subsequent output row:
        *   Copy the previous row
        *   Find the position of the first zero after the intial non-zero sequence. Change it to be the same color as the preceding pixel.
6. Stop when output row is entirely non-zero colors.
"""

import numpy as np

def transform(input_grid):
    # Input is a single row.
    input_row = input_grid[0]

    # Identify the sequence of non-zero colors and trailing zeros.
    first_zero_index = len(input_row)
    for i, pixel in enumerate(input_row):
        if pixel == 0:
            first_zero_index = i
            break

    # Determine number of output rows and initialize
    num_output_rows = 0
    current_row = input_row.copy()
    while True:
       num_output_rows +=1
       all_non_zero = True
       for pixel in current_row:
          if pixel == 0:
             all_non_zero = False
             break
       if all_non_zero:
          break
       # extend by finding and setting the first zero.
       for i in range(len(current_row)):
          if current_row[i] == 0:
              current_row[i] = current_row[i-1] if i> 0 else current_row[i]
              break

    output_grid = np.zeros((num_output_rows, len(input_row)), dtype=int)

    # Create output rows, extending the sequence.
    current_row = input_row.copy()
    output_grid[0] = current_row
    for row_index in range(1,num_output_rows):
        # Copy the previous row.
        next_row = current_row.copy()

        # Find the position of the first zero after the initial non-zero and fill
        for i in range(len(next_row)):
          if next_row[i] == 0:
            next_row[i] = next_row[i-1]
            break
        output_grid[row_index] = next_row
        current_row = next_row

    return output_grid
```
