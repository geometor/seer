# 3af2c5a8 • 006 • example_3 - CODE

---
```python
"""
The transformation rule scales the input grid by a factor of 2 in both dimensions.
Then, it replicates the first row of the input to fill the entire top row of the output grid.
It replicates the first column of the input to fill the entire leftmost column of the output grid.
Finally, it fills the last column of the expanded grid with the value from the first column of the expanded grid (which is same color of the first element).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Replicate the first row across the top of the output.
    for j in range(cols * 2):
        output_grid[0, j] = input_grid[0, 0]

     # Replicate the first column down the left side of the output.
    for i in range(rows * 2):
        output_grid[i, 0] = input_grid[0, 0]
        output_grid[i, (cols*2)-1] = input_grid[0,0]

    # Fill the last row
    for j in range(cols * 2):
      output_grid[(rows*2)-1, j] = input_grid[0, 0]

    return output_grid.tolist()
```

