# cf98881b • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Target Colors:** The target colors for the output grid are yellow (4) and maroon (9).
2.  **Locate Subgrid:** within input_grid, locate a minimal rectangular sub-grid that contains every instance of color 9.
3.  **Select Columns/Rows:** select from input_grid, any column that contains an element of color 9 and keep all rows.
4. **compose output:** construct output_grid from the selected subgrid.
"""

import numpy as np

def get_columns_with_color(grid, color):
    # returns indices of any columns with the color
    cols = []
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            if grid[y][x] == color:
                cols.append(x)
                break # only need one per col
    return cols

def transform(input_grid):
    # make input a numpy array
    input_grid = np.array(input_grid)

    # get the columns that contain color 9
    cols = get_columns_with_color(input_grid, 9)

    # select subgrid based upon the columns
    output_grid = input_grid[:, cols]

    return output_grid.tolist()
```
