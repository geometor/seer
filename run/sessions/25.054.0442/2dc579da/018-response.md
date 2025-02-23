# 2dc579da • 018 • refine_coder

---
```python
"""
The transformation extracts a 5x5 subgrid from the input grid.
It then identifies colors present in the input subgrid but not in the output grid.
Pixels of these identified colors are removed from the subgrid. The relative
positions of the retained color pixels are preserved, producing the final
output.
"""

import numpy as np

def transform(input_grid, output_grid_expected):
    # Extract 5x5 subgrid
    subgrid = input_grid[:5, :5]

    # Identify colors to remove
    input_colors = set(np.unique(subgrid))
    output_colors = set(np.unique(output_grid_expected))
    colors_to_remove = input_colors - output_colors

    # Filter colors: Create a mask for pixels to keep
    mask = np.ones(subgrid.shape, dtype=bool)
    for color in colors_to_remove:
        mask &= (subgrid != color)

    # initialize output using the mask and subgrid, padding as needed.
    output_grid = np.full(output_grid_expected.shape, -1) # fill with -1 (for "blank").

    # figure out the subset to copy
    rows, cols = np.where(mask)

    if len(rows) > 0: # can be empty list!
        min_row, min_col = np.min(rows), np.min(cols)
        max_row, max_col = np.max(rows), np.max(cols)

        # copy only what will fit
        rows_to_copy = min(max_row - min_row + 1, output_grid.shape[0])
        cols_to_copy = min(max_col - min_col + 1, output_grid.shape[1])


        output_grid[:rows_to_copy, :cols_to_copy] = subgrid[min_row:min_row+rows_to_copy, min_col:min_col+cols_to_copy]


    output_grid[output_grid == -1] = 0 # replace blanks with 0.

    return output_grid
```
