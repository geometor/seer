# d4469b4b • 026 • example_5 • investigate_coder

---
```python
"""
The input 5x5 grid is reduced to a 3x3 output grid. 
The output grid summarizes 3x3 regions of the central part of the input grid.
If any of the input pixels in a region are red (2), the corresponding output pixel is grey (5). 
Otherwise, the output pixel is white (0).
"""

import numpy as np

def transform(input_grid):
    """Transforms a 5x5 input grid to a 3x3 output grid based on summarization and color transformation."""

    input_array = np.array(input_grid)
    output_array = np.zeros((3, 3), dtype=int)

    # Iterate through the 3x3 output grid
    for i in range(3):
        for j in range(3):
            # Define the 3x3 region in the input grid.  These overlap.
            row_start = i
            row_end = i + 3
            col_start = j
            col_end = j + 3

            # Extract the region from the input
            region = input_array[row_start:row_end, col_start:col_end]

            # Check if any pixel in the region is red (2)
            if 2 in region:
                output_array[i, j] = 5  # Set output to grey (5)
            else:
                output_array[i, j] = 0  # Set output to white (0)

    return output_array.tolist()
```
