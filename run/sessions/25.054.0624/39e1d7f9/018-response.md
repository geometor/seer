# 39e1d7f9 • 018 • refine_coder

---
```python
"""
The transformation identifies regions enclosed by azure (8) lines. White (0) pixels within these enclosed regions are filled with yellow (4). Other colored regions within the azure boundaries are preserved. The azure boundaries themselves are also preserved.
"""

import numpy as np
from scipy.ndimage import label, binary_erosion

def get_objects_by_color(grid, color):
    """Find contiguous regions of the specified color."""
    mask = (grid == color)
    labeled_array, num_features = label(mask)
    return labeled_array, num_features

def get_enclosed_mask(grid, boundary_color):
    """
    Finds the mask of pixels enclosed by the boundary color.

    Args:
        grid: The input grid.
        boundary_color: The color of the boundary.

    Returns:
        A boolean mask where True indicates an enclosed pixel.
    """

    # Create a mask for the boundary pixels
    boundary_mask = (grid == boundary_color)

    # Invert the boundary mask to find non-boundary areas
    inverted_mask = ~boundary_mask

    # Label connected regions in the inverted mask
    labeled_array, _ = label(inverted_mask)

    # Find the label of the background (exterior) region.  We assume the
    # top-left corner is always part of the exterior.
    background_label = labeled_array[0, 0]
    
    # Create a mask for the background
    background_mask = (labeled_array == background_label)    

    # The enclosed region is everything *except* the background
    enclosed_mask = ~background_mask

    return enclosed_mask

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """

    # Initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Get the mask for enclosed regions
    enclosed_mask = get_enclosed_mask(input_grid, boundary_color=8)

    # Iterate through the grid and apply the transformation
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is white, enclosed, and not part of the boundary
            if input_grid[r, c] == 0 and enclosed_mask[r, c]:
                output_grid[r, c] = 4  # Fill with yellow

    return output_grid
```
