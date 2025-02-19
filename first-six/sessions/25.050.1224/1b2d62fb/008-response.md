# 1b2d62fb • 008 • example_4 - CODE

---
```python
import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of blue pixels in each row.
    The output grid has a width of 3 and the same number of rows as the input.
    If a blue pixel exists anywhere in columns 0, 1, or 2 of a given row,
    an azure pixel (8) is placed in position (row, 0) of the output grid.
    If a blue pixel exists in column 3 of a given row, an azure pixel is
    placed in position (row, 1) of the output grid.
    If a blue pixel exists in columns 4, 5, or 6 of a given row, an azure
    pixel is placed in (row, 2) of the output grid.  All other cells are 0.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 1:
                if j in [0, 1, 2]:
                    output_grid[i,0] = 8
                if j == 3:
                    output_grid[i,1] = 8
                if j in [4,5,6]:
                    output_grid[i,2] = 8

    return output_grid
```

