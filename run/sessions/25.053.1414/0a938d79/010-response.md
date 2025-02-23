# 0a938d79 • 010 • refine_coder

---
```python
"""
Transforms an input grid by replicating any non-zero value in a row across the rest of that row.
Rows that are all zeros remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    
    Args:
        input_grid: A 2D numpy array representing the input grid.
    
    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    output_grid = np.copy(input_grid)  # Start with a copy to preserve original 0 rows.
    rows, cols = input_grid.shape

    # Iterate through each row
    for r in range(rows):
        row = input_grid[r, :]
        
        # Check if the row contains any non-zero values
        if np.any(row != 0):
            # Iterate through each cell in the row
            for c in range(cols):
                # If a non-zero value is found, replicate it to the rest of the row
                if input_grid[r, c] != 0:
                    output_grid[r, c:] = input_grid[r, c]
                    break  # Once a non-zero is found and replicated, move to the next row
        # else:  Implicitly, rows with all zeros remain as they are in the copied output_grid

    return output_grid
```

