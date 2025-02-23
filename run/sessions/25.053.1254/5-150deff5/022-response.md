# 5-150deff5 • 022 • refine_coder

---
```python
"""
Identifies contiguous vertical segments of gray pixels (value 5) in the input grid. Within each segment, it replaces the gray pixels with an alternating pattern of azure (value 8) and red (value 2) pixels, starting with azure. The background (white, value 0) remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through columns and rows to find gray segments
    for c in range(cols):
        segment_start = -1
        for r in range(rows):
            if input_grid[r, c] == 5:
                if segment_start == -1:
                    segment_start = r
            elif segment_start != -1:
                # End of segment, perform replacement
                segment_length = r - segment_start
                for i in range(segment_length):
                    if (i) % 2 == 0:  # Even index: azure
                        output_grid[segment_start + i, c] = 8
                    else:  # Odd index: red
                        output_grid[segment_start + i, c] = 2
                segment_start = -1

        # Handle segment at the end of a column
        if segment_start != -1:
            segment_length = rows - segment_start
            for i in range(segment_length):
                if (i) % 2 == 0:  # Even index: azure
                    output_grid[segment_start + i, c] = 8
                else:  # Odd index: red
                    output_grid[segment_start + i, c] = 2

    return output_grid.tolist()
```
