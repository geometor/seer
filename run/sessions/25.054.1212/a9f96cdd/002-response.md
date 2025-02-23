# a9f96cdd • 002 • example_1 • investigate_coder

---
```python
"""
The transformation identifies non-zero pixels in the input grid, removes them, and then introduces new objects with different colors at different positions in the output grid.  The positioning and color choice of the new objects do not follow an easily discernible pattern from the single example provided.
"""

import numpy as np

def get_nonzero_pixels(grid):
    """Finds the coordinates and values of non-zero pixels in a grid."""
    non_zero_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append(((row_index, col_index), value))
    return non_zero_pixels

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid, then set all to 0
    output_grid = np.zeros_like(input_grid)

    # Identify non-zero pixels in the input grid.
    non_zero_pixels = get_nonzero_pixels(input_grid)

    # Find unique non zero colors
    input_colors = set([v for _,v in non_zero_pixels])
    available_colors = set(range(1, 10))
    new_colors = list(available_colors - input_colors)
    
    # We can choose colors randomly
    np.random.shuffle(new_colors)
    
    empty_cells = []
    for row_index in range(input_grid.shape[0]):
        for col_index in range(input_grid.shape[1]):
            empty_cells.append((row_index, col_index))
            
    # Choose locations for the new colored objects randomly.
    np.random.shuffle(empty_cells)

    # need at least as many open cells and colors
    n = min(len(new_colors),len(empty_cells))
    for i in range(n):
        row, col = empty_cells[i]
        output_grid[row, col] = new_colors[i]
        
    return output_grid
```
