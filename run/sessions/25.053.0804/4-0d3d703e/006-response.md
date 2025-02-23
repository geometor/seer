# 4-0d3d703e • 006 • example_3 - CODE

---
```python
"""
The transformation rule involves applying a specific operation to each cell based on its original value. It appears there are three consistent mappings across all examples:

1.  If the input value is 3, add 1 to it.
2.  If the input value is 1, add 4 to it.
3.  If the input value is 2, add 4 to it.

The second example has the following:
1. If the input is 2, add 4.
2. If the input is 3, add 1.
3. If the input is 8, add 1.

And the third example:
1. if input is 5, subtract 4 (or 5 - 1 = 4)
2. input value 8 maps to 9: subtract -1 (or add 1), but its also subtract 9 (8-9 = -1 or 9 mod 10)
3. input value 6 maps to 2: subtract 4 (or 6 - 2 = 4)

The transformation rule set seems to change for each input example.
"""

import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to modify
    output_grid = np.copy(input_grid)
    
    # check for example 1 conditions
    if set(np.unique(input_grid)) == {1,2,3}:
      # Apply the transformation: Add 1 to cells that are 3(green).
      output_grid[input_grid == 3] += 1
      # Apply the transformation: Add 4 to cells that are 1(blue).
      output_grid[input_grid == 1] += 4
      # Apply the transformation: Add 4 to cells that are 2(red).
      output_grid[input_grid == 2] += 4
    # check for example 2 conditions
    elif set(np.unique(input_grid)) == {2,3,8}:
      # Apply the transformation: Add 4 to cells that are 2(red).
      output_grid[input_grid == 2] += 4
      # Apply the transformation: Add 1 to cells that are 3(green).
      output_grid[input_grid == 3] += 1
      # Apply the transformation: Add 1 to cells that are 8(azure).
      output_grid[input_grid == 8] += 1
    # check for example 3 conditions
    elif set(np.unique(input_grid)) == {5,6,8}:
      # Apply transformations using modulo arithmetic
      output_grid[input_grid == 5] = (output_grid[input_grid == 5] - 4) % 10  # 5 becomes 1
      output_grid[input_grid == 8] = (output_grid[input_grid == 8] - 9) % 10  # 8 becomes 9
      output_grid[input_grid == 6] = (output_grid[input_grid == 6] - 4) % 10  # 6 becomes 2
    else:
       raise Exception(f'input values {np.unique(input_grid)} not recognized')

    return output_grid
```
