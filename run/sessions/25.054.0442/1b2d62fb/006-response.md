# 1b2d62fb • 006 • refine_coder

---
```python
"""
1.  **Find the Vertical Blue Line:** Locate the vertical line of blue (1) pixels within the input grid. Note its column index. The height/width ratio of the grid also appears important.
2. **Transpose and Mirror based on the blue line:** It appears that the subgrid to the left of the blue line (inclusive) gets transposed, and then a mirrored version of the transpose gets put below.
3.  **Create Output Grid:** The output grid has a dynamic size determined by transposing the input grid to the left of and including the blue vertical line.
4.  **Place Azure Pixels:** The subgrid defined by the region to the left of the blue line is transposed. All pixels in this transposed grid that are not 0 have their color changed to 8. Then a mirrored version of this transposed grid is placed below, creating a dynamic number of azure pixels.
5. **Fill Remaining with Black:** Fill all other cells in the output grid with black (0).
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the column index of a vertical line of the specified color."""
    height, width = grid.shape
    for j in range(width):
        is_line = True
        for i in range(height):
            if grid[i, j] != color:
                is_line = False
                break
        if is_line:
            return j
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    # Find the vertical blue line
    blue_column = find_vertical_line(input_grid, 1)

    # Extract the subgrid to the left of the blue line (inclusive)
    subgrid = input_grid[:, :blue_column + 1]

    # Transpose the subgrid
    transposed_subgrid = subgrid.T

    # Create the output grid based on transposed subgrid size and mirrored portion
    output_height, output_width = transposed_subgrid.shape
    output_grid = np.zeros((output_height * 2, output_width), dtype=int) # Double height to stack

    #change any non-zero values to azure
    transposed_subgrid_azure = np.where(transposed_subgrid != 0, 8, transposed_subgrid)

    # Copy the transposed subgrid to top half
    output_grid[:output_height, :] = transposed_subgrid_azure

    # Create a mirrored version of the top
    mirrored_top = transposed_subgrid_azure[::-1,:]

    # place on the bottom
    output_grid[output_height:,:] = mirrored_top

    return output_grid
```
