# bbc9ae5d • 018 • refine_coder

---
```python
"""
Transforms a 1xN input grid into an MxN output grid where non-zero values in the input expand into
growing "triangles" to the right, and zero values are copied to all rows. The height M of the
output grid depends on the number of non-zero elements up to and including each position.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    width = input_grid.shape[1]

    # Calculate height and initialize
    non_zero_counts = []
    count = 0
    for x in input_grid[0]:
      if x != 0:
        count += 1
      non_zero_counts.append(count)
    height = max(non_zero_counts)

    output_grid = np.zeros((height, width), dtype=int)

    # Iterate and expand
    current_height = 0
    for j in range(width):
        pixel_val = input_grid[0, j]
        if pixel_val == 0:
            # Copy zero to all rows
            for i in range(height):
                output_grid[i, j] = pixel_val
        else:
            # Expand non-zero
            rows_to_affect = non_zero_counts[j]
            for i in range(rows_to_affect):
                expansion_length = i + 1
                for k in range(min(expansion_length, width - j)):  # Limit expansion to width
                    output_grid[i, j + k] = pixel_val


    return output_grid
```
