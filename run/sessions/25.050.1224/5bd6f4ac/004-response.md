# 5bd6f4ac • 004 • example_2 - CODE

---
```python
"""
The transformation extracts a 3x3 subgrid from the top right corner of the input grid 
(rows 0, 1 and 2, and columns 6, 7, and 8) to create the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 3x3 subgrid from the input grid.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The 3x3 extracted subgrid.
    """
    # Convert the input grid to a NumPy array
    input_array = np.array(input_grid)

    # Extract the 3x3 subgrid
    output_grid = input_array[0:3, 6:9]

    return output_grid
```

