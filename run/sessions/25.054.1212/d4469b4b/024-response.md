# d4469b4b • 024 • refine_coder

---
```python
"""
Condenses a 5x5 input grid into a 3x3 output grid. Each cell in the output grid represents an overlapping 3x3 region in the input. If a 3x3 region in the input contains at least one pixel of a "trigger" color (determined from the example, can be red, blue, or green), the corresponding output cell is gray (5). Otherwise, it's white (0).
"""

import numpy as np

def _get_trigger_color(input_grid, expected_output):
    """
    Determines the trigger color based on input and expected output.
    """
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    trigger_colors = []
    for color in np.unique(input_grid):
        if color == 0:  # Skip white
            continue
        
        test_output = np.zeros((3, 3), dtype=int)
        for r in range(3):
            for c in range(3):
                region = input_grid[r:r+3, c:c+3]
                if color in region:
                    test_output[r, c] = 5
                else:
                    test_output[r,c] = 0 # add to set white for no matching trigger
        if np.array_equal(test_output, expected_output):
            trigger_colors.append(color)
    # check if no trigger color has been set, which means we set all output to white
    if not trigger_colors:
       return 0
    return trigger_colors[0]  # Return the first matching trigger color.

def transform(input_grid):
    """
    Transforms a 5x5 input grid into a 3x3 output grid based on the presence of trigger color in overlapping 3x3 subgrids.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through each cell of the output grid
    for row in range(3):
        for col in range(3):
            # Define the corresponding 3x3 region in the input grid
            start_row = row
            end_row = row + 3
            start_col = col
            end_col = col + 3

            # Extract the 3x3 region
            region = input_grid[start_row:end_row, start_col:end_col]

            # Determine the trigger color dynamically
            trigger_color = _get_trigger_color(input_grid, output_grid) # will be corrected
            
            # Check if at least one pixel of the trigger color exists in the region
            if trigger_color in region:
                output_grid[row, col] = 5  # Set to gray (5)
            else:
                output_grid[row,col] = 0
    
    return output_grid.tolist()
```
