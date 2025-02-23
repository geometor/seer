# 3ac3eb23 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation replicates each non-zero pixel's value downwards, alternating the non-zero color with a zero value, creating a repeating pattern.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replicating non-zero pixels downwards in an alternating pattern.
    
    Args:
        input_grid (list of lists): The input grid.
    
    Returns:
        list of lists: The transformed output grid.
    """
    
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is non-zero
            if input_grid[r, c] != 0:
                # Replicate the non-zero pixel's value downwards in an alternating pattern
                for i in range(r + 1, rows):
                    if (i - r) % 2 != 0:
                      output_grid[i,c] = input_grid[r,c]
                    else:
                      output_grid[i, c] = 0
    return output_grid.tolist()
```
