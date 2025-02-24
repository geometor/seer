# 017c7c7b • 011 • refine_coder

---
```python
"""
1.  **Identify Input:** Take the input grid, which contains white (0) and blue (1) pixels.
2.  **Color Substitution:** Replace all blue (1) pixels with red (2) pixels.
3.  **Height Extension:** Increase the height of the grid by 50% (adding rows at the bottom).
4. Copy the last row of the input into each of the new rows of the output.
5. **Output:** Return the modified grid.
"""

import numpy as np

def transform(input_grid):
    # Color Substitution: Replace all blue (1) pixels with red (2) pixels.
    output_grid = np.where(input_grid == 1, 2, input_grid)

    # Height Extension: Increase the height of the grid by 50% (adding rows at the bottom).
    input_height = output_grid.shape[0]
    extension_height = input_height // 2
    extended_output_grid = np.vstack([output_grid, np.zeros((extension_height, output_grid.shape[1]))])

    
    # Copy the last row of the *original* input into the *new* rows.
    last_row_input = input_grid[-1]
    for i in range(input_height, input_height + extension_height):
        extended_output_grid[i] = last_row_input

    # change output pixels to match color substitution
    extended_output_grid = np.where(extended_output_grid == 1, 2, extended_output_grid)


    return extended_output_grid
```
