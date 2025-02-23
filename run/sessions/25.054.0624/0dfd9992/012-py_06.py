"""
The transformation rule identifies and removes all contiguous regions (objects) of color 0 (white) from the input grid.
All other pixels (non-white) remain unchanged. The output grid has the same dimensions as the input grid.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
    """
    Transforms the input grid by removing all contiguous regions of color 0.

    Args:
        input_grid (list of lists): The input 2D grid.

    Returns:
        list of lists: The transformed 2D grid.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)
    output_array = np.copy(input_array)

    # Label connected regions of 0s.
    labeled_array, num_features = label(input_array == 0)

    # Iterate through each labeled region.
    for region_label in range(1, num_features + 1):  # Labels start from 1
        # Find all pixels belonging to the current region.
        region_pixels = (labeled_array == region_label)

        # Remove the region by setting all its pixels to a different value
        output_array[region_pixels] = input_array[~region_pixels][0] if np.any(~region_pixels) else input_array[region_pixels][0]

    output_grid = output_array.tolist()

    return output_grid