# a64e4611 • 004 • refine_coder

---
```python
"""
The transformation overlays a green (3) cross shape onto the existing background grid. The background grid consists
of varying colors. The cross shape is centered on the grid, with its thickness determined by the grid's dimensions.
"""

import numpy as np

def calculate_thickness(dimension):
    """Calculates the thickness of the cross bars."""
    return dimension // 7 + 1

def create_cross(grid, cross_color=3):
    """Creates a green cross shape on a zero-filled grid of the same size as the input grid."""
    rows, cols = grid.shape
    thickness = calculate_thickness(min(rows, cols))  # Use the smaller dimension
    cross = np.zeros_like(grid)

    center_row = rows // 2
    center_col = cols // 2

    # Vertical part of the cross
    cross[center_row - thickness + 1:center_row + thickness, :] = cross_color

    # Horizontal part of cross
    cross[:, center_col - thickness + 1:center_col + thickness] = cross_color

    return cross

def transform(input_grid):
    """
    Overlays a green cross shape onto the input grid, replacing existing pixels.
    """
    # Initialize output_grid as copy of input
    output_grid = input_grid.copy()

    # Create cross based on the input_grid size
    cross = create_cross(input_grid)

    # Overlay the cross
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if cross[r, c] != 0:
                output_grid[r, c] = cross[r, c]

    return output_grid
```
