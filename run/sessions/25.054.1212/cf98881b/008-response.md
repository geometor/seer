# cf98881b • 008 • example_2 • investigate_coder

---
```python
"""
1. **Crop:** Extract a 4x4 sub-grid from the input grid. The exact location of this sub-grid within the larger input grid is not immediately obvious.
2. **Color Substitution/Filter:**
    -   Change pixels with value `2` (red) to `1` (blue).
    -   Keep pixels with values `0`, `4`, and `9` unchanged.
    -   Remove/ignore all other colors.
"""

import numpy as np

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)
    
    # Initialize the output grid (we'll crop later)
    output_grid = np.copy(input_grid)


    # Apply color substitution
    output_grid[output_grid == 2] = 1

     # Define cropping boundaries (these values might need adjustment in future iterations)
    start_row = 0
    start_col = 0
    end_row = 4
    end_col = 4

    # Crop a 4x4 region.  we guess it will be at 0,0
    cropped_grid = output_grid[start_row:end_row, start_col:end_col]

    return cropped_grid.tolist()
```
