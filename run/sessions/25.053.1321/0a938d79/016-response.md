# 0a938d79 • 016 • refine_coder

---
```python
"""
1. Identify Seed Rows: Scan the input grid to find rows containing only one non-zero pixel. These are the "seed rows". Record the row index, the color of the pixel, and the column index of the pixel for each seed row.

2. Extend Seed Colors: In the output grid, for each seed row, fill the cells from the seed pixel's column to the end of the row with the seed color.

3. Fill Remaining Cells: For all rows in the output grid:
    * If the row already contains colored cells (from step 2): Do not modify this row.
    * Otherwise, fill the row by creating a repeating sequence of the seed row colors.
    * If a row has no colored cells, the entire row is filled by the repeating sequence of seed colors.

4. Preserve empty rows: If after completing these steps, a cell remains 0, and was also 0 in the input, keep it at 0.
"""

import numpy as np

def find_seed_rows(grid):
    """
    Identifies rows with exactly one non-zero pixel and returns their information.
    """
    seed_rows = []
    for i, row in enumerate(grid):
        non_zero_indices = np.nonzero(row)[0]
        if len(non_zero_indices) == 1:
            seed_rows.append({
                "row_index": i,
                "color": row[non_zero_indices[0]],
                "column_index": non_zero_indices[0]
            })
    return seed_rows

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    seed_rows = find_seed_rows(input_grid)

    # Extend seed colors to the right
    for seed_info in seed_rows:
        row_index = seed_info["row_index"]
        color = seed_info["color"]
        column_index = seed_info["column_index"]
        output_grid[row_index, column_index:] = color

    # Get seed colors and their original order
    seed_colors = [sr['color'] for sr in seed_rows]

    # Fill remaining cells (both to the left and between seed rows)
    num_rows, num_cols = output_grid.shape
    for r_idx in range(num_rows):
        if any(output_grid[r_idx]):  # Skip rows already filled by seed extension
            continue

        # build color sequence from seed colors
        color_seq = []
        if len(seed_colors) > 0 :
          color_seq = seed_colors
        
        # fill row if there is a color sequence
        if (len(color_seq) > 0):
          color_index = 0
          for c_idx in range(num_cols):
              output_grid[r_idx, c_idx] = color_seq[color_index % len(color_seq)]
              color_index += 1
        # if empty, will remain all 0

    return output_grid
```
