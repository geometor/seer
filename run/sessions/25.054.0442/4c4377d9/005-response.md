# 4c4377d9 • 005 • refine_coder

---
```python
"""
The input grid is mirrored along both its horizontal and vertical axes to create a 2x2 grid where:
- The top-left quadrant is the original input.
- The top-right quadrant is the input flipped horizontally.
- The bottom-left quadrant is the input flipped vertically.
- The bottom-right quadrant is the input flipped both horizontally and vertically.
"""

import numpy as np

def flip_horizontal(grid):
    """Flips a grid horizontally."""
    return np.fliplr(grid)

def flip_vertical(grid):
    """Flips a grid vertically."""
    return np.flipud(grid)

def transform(input_grid):
    """Transforms the input grid according to the mirroring rule."""
    # Create mirrored versions of the input grid.
    horizontal_mirror = flip_horizontal(input_grid)
    vertical_mirror = flip_vertical(input_grid)
    both_mirrored = flip_vertical(horizontal_mirror)

    # Initialize the output grid (2x the size of the input).
    rows, cols = input_grid.shape
    output_grid = np.zeros((2 * rows, 2 * cols), dtype=input_grid.dtype)

    # Fill in the quadrants of the output grid.
    output_grid[:rows, :cols] = input_grid  # Top-left: Original
    output_grid[:rows, cols:] = horizontal_mirror  # Top-right: Flipped horizontally
    output_grid[rows:, :cols] = vertical_mirror  # Bottom-left: Flipped vertically
    output_grid[rows:, cols:] = both_mirrored  # Bottom-right: Flipped both ways

    return output_grid
```

