# ed36ccf7 • 024 • refine_coder

---
```python
"""
Rotates the input grid 90 degrees counter-clockwise. If a pixel in the rotated
grid would have a value of 0, and the pixel in the *original* grid at the
location that would have rotated to the current position has a non-zero value,
then that pixel value is carried over to the rotated/output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)

    # Rotate the array 90 degrees counter-clockwise.
    output_np = np.rot90(input_np)

    # Iterate through the *output* grid and apply the conditional overwrite.
    rows, cols = output_np.shape
    for row in range(rows):
        for col in range(cols):
            # Calculate corresponding input coordinates
            input_row = col
            input_col = rows - 1 - row

            if output_np[row, col] == 0 and input_np[input_row, input_col] != 0:
                output_np[row, col] = input_np[input_row, input_col]

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid
```
