# ed36ccf7 • 022 • refine_coder

---
```python
"""
The output grid is a 90 degree counter-clockwise rotation of the input grid.
Additionally, if a pixel in the rotated grid would have a value of 0, and the
pixel in the *original* grid at that location (pre-rotation) had a non-zero value,
then that pixel value is carried over to the rotated/output grid.  This is a
form of conditional overwrite based on comparing the "would-be" rotated value
to the original input value.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid 90 degrees counter-clockwise, with a conditional overwrite.
    """
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)

    # Rotate the array 90 degrees counter-clockwise.
    output_np = np.rot90(input_np)

    # Create a "pre-rotated" version by rotating clockwise once. This allows us
    # to easily index into the original input using the *output* coordinates.
    pre_rotated_np = np.rot90(input_np, k=-1)

    # Iterate through the *output* grid and apply the conditional overwrite.
    rows, cols = output_np.shape
    for row in range(rows):
        for col in range(cols):
            if output_np[row, col] == 0 and pre_rotated_np[row, col] != 0:
                output_np[row, col] = pre_rotated_np[row, col]


    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid
```

