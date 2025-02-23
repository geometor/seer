# 484b58aa • 006 • refine_coder

---
```python
"""
The transformation rule is to remove all pixels of color 0 (white) from the input grid. The remaining pixels should maintain their relative positions within each row. Then, pad each row with zeros until it is the same size as the longest row.
"""

import numpy as np

def transform(input_grid):
    """
    Removes all white (0) pixels from the input grid, shifting remaining pixels left, and pads
    rows with zeros so all are same size as longest.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array with white pixels removed and other pixels shifted left within each row.
    """
    output_grid = []
    max_len = 0
    # first pass, collect non-zero pixels and determine max row length
    for row in input_grid:
        new_row = []
        for pixel_value in row:
            if pixel_value != 0:
                new_row.append(pixel_value)
        output_grid.append(new_row)
        max_len = max(max_len, len(new_row))


    # second pass, create numpy array and pad as needed
    final_grid = []
    for row in output_grid:
      pad_width = max_len - len(row)
      padded_row = np.pad(row, (0, pad_width), mode='constant', constant_values=0)
      final_grid.append(padded_row)

    return np.array(final_grid)
```
