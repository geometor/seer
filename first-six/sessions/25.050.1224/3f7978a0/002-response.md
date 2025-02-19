# 3f7978a0 • 002 • example_1 - CODE

---
```python
"""
Extracts a 5x5 subgrid from the input 9x9 grid. The corners of the 5x5 grid 
are filled with azure (color 8) if present in specific input locations.
Two vertical gray lines from the input are repositioned to the edges of the output.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 9x9 input grid into a 5x5 output grid based on specific rules.
    
    Args:
        input_grid (numpy.ndarray): A 9x9 NumPy array representing the input grid.
        
    Returns:
        numpy.ndarray: A 5x5 NumPy array representing the output grid.
    """
    # Initialize the 5x5 output grid with all zeros.
    output_grid = np.zeros((5, 5), dtype=int)

    # Place azure (color 8) cells in the corners and center of the output grid.
    # These correspond to specific locations in the input grid.
    if input_grid[1, 1] == 8:
      output_grid[0, 0] = 8
    if input_grid[1, 5] == 8:
      output_grid[0, 4] = 8
    if input_grid[3, 3] == 8:  
      output_grid[4, 0] = 8
    if input_grid[7, 3] == 8:
      output_grid[4, 4] = 8
    if input_grid[1, 8] == 8:
      output_grid[2, 2] = 8
    

    # Extract and reposition the two vertical gray (color 5) lines.
    output_grid[1:4, 0] = input_grid[2:5, 1]
    output_grid[1:4, 4] = input_grid[2:5, 5]
    
    #check that these pixels are actually 5.
    for i in range(1,4):
        if output_grid[i,0] != 5: output_grid[i,0] = 0
        if output_grid[i,4] != 5: output_grid[i,4] = 0

    return output_grid
```
