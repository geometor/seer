# 746b3537 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation extracts the leftmost column of the input grid and uses that as the output grid. The program takes a 3x3 grid and reduces it to a 3x1 grid, effectively taking the first column of the input and presenting it as a single column output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a list
    output_grid = []

    # iterate through rows of the input_grid
    for row in input_grid:
        # append the first element of each row to the output_grid
        output_grid.append(row[0])

    return output_grid
```
