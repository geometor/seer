# ed36ccf7 • 016 • refine_coder

---
```python
"""
The input grid is rotated 90 degrees counter-clockwise. After the rotation, the pixel in the lower-left corner of the input grid moves to the lower-right corner of the output grid.
"""

import numpy as np

def transform(input_grid):
    """Rotates the input grid 90 degrees counter-clockwise and moves the lower-left pixel to the lower-right.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The rotated and modified output grid.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Rotate the array 90 degrees counter-clockwise.
    rotated_array = np.rot90(input_array)

    # Convert the rotated array back to a list of lists.
    output_grid = rotated_array.tolist()

    # Get the dimensions of the grid.
    rows = len(output_grid)
    cols = len(output_grid[0])

    # Move the lower-left pixel to the lower-right.
    lower_left_pixel = output_grid[rows - 1][0]
    output_grid[rows - 1][cols - 1] = lower_left_pixel
    output_grid[rows-1][0] = rotated_array[rows-1][cols-1] # original value in that spot


    return output_grid
```

