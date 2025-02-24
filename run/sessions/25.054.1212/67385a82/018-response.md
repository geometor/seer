# 67385a82 • 018 • refine_coder

---
```python
"""
1.  **Find Green Pixels:** Identify all pixels with the value 3 (green).

2.  **Top Row Transformation:** If a green pixel is in the top row (row 0), change the pixel directly *below* it to azure (8).

3.  **Bottom Row Transformation:** If a green pixel is in the *bottom* row, check the pixel *above* it. If the pixel above is *not* azure (8), change the green pixel to azure (8).

4.  **All Other Pixels:** Pixels that do not meet these specific conditions remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find green pixels
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Green pixel found
                # Top Row Transformation
                if r == 0:
                    if r + 1 < rows:  # Ensure we're not out of bounds
                        output_grid[r + 1, c] = 8  # Change pixel below to azure
                # Bottom Row Transformation
                elif r == rows - 1:
                    if r - 1 >= 0:  # Ensure we're not out of bounds
                        if output_grid[r - 1, c] != 8:  # Check pixel above
                            output_grid[r, c] = 8  # Change to azure

    return output_grid
```

