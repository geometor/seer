# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
The transformation rule is applied cell by cell across the input grid to generate the output grid.  For each cell in the input grid, we check its color.

If a cell in the input grid is red (color 2), then in the output grid, its immediate orthogonal neighbors (up, down, left, and right cells) are changed to yellow (color 4). The red cell itself remains unchanged in the output grid.

If a cell in the input grid is blue (color 1), then in the output grid, its immediate orthogonal neighbors are changed to orange (color 7). The blue cell itself remains unchanged in the output grid.

If a cell in the input grid is any other color (including white), it remains unchanged in the output grid, and it does not affect its neighbors.

This process is applied independently for each red and blue cell in the input grid. If a cell is a neighbor of both a red and a blue cell, it will be affected by both rules.  However, based on the examples, it seems the transformation is applied independently for each non-white cell without considering overlaps or priorities. If a cell is targeted to be changed by multiple source cells, it will be overwritten based on the order of processing the source cells. However, based on the description and examples, it appears that neighbor cells simply take the color effect of each source cell, without interaction between neighbor modifications from different source cells.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels
    for i in range(rows):
        for j in range(cols):
            # Process only red and blue cells
            if input_grid[i, j] == 2:  # Red cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                        output_grid[r, c] = 4  # Set to yellow
            elif input_grid[i, j] == 1:  # Blue cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                        output_grid[r, c] = 7  # Set to orange

    return output_grid
```

