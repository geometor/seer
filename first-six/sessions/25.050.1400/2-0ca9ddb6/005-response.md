# 2-0ca9ddb6 • 005 • example_3 - NLP

---
**Natural Language Program: Transformation Rule**

The transformation rule operates by examining each cell of the input grid. For every cell, we check its color.

- **If the cell is red (color 2):** In the output grid, we change the color of its immediate orthogonal neighbors (the cells directly above, below, to the left, and to the right) to yellow (color 4). The red cell itself remains unchanged in the output grid.
- **If the cell is blue (color 1):** In the output grid, we change the color of its immediate orthogonal neighbors (up, down, left, right) to orange (color 7). The blue cell itself remains unchanged in the output grid.
- **If the cell is any other color (including white and magenta):** This cell and its neighbors are not affected by this rule. The cell retains its original color in the output grid, and it does not cause any changes to its neighboring cells.

This process is applied independently for each cell in the input grid. If a cell is a neighbor to multiple red or blue cells, it might be targeted for color change multiple times. The final color of such a cell is determined by the last transformation applied to it based on the order in which the red/blue source cells are processed. However, according to the problem description, it is implied that the neighbor cells simply take on the color effects of each source cell, without complex interaction or priority rules between modifications from different source cells.

```python
"""
The transformation rule operates by examining each cell of the input grid. For every cell, we check its color.

- If the cell is red (color 2): In the output grid, we change the color of its immediate orthogonal neighbors (the cells directly above, below, to the left, and to the right) to yellow (color 4). The red cell itself remains unchanged in the output grid.
- If the cell is blue (color 1): In the output grid, we change the color of its immediate orthogonal neighbors (up, down, left, right) to orange (color 7). The blue cell itself remains unchanged in the output grid.
- If the cell is any other color (including white and magenta): This cell and its neighbors are not affected by this rule. The cell retains its original color in the output grid, and it does not cause any changes to its neighboring cells.

This process is applied independently for each cell in the input grid. If a cell is a neighbor to multiple red or blue cells, it might be targeted for color change multiple times. The final color of such a cell is determined by the last transformation applied to it based on the order in which the red/blue source cells are processed. However, according to the problem description, it is implied that the neighbor cells simply take on the color effects of each source cell, without complex interaction or priority rules between modifications from different source cells.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 2:  # Red cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:
                        output_grid[r, c] = 4
            elif input_grid[i, j] == 1:  # Blue cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:
                        output_grid[r, c] = 7
    return output_grid
```
