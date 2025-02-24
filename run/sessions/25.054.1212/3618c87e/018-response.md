# 3618c87e • 018 • refine_coder

---
```python
"""
1.  **Copy:** The first three rows (indices 0, 1, and 2) of the input grid are copied to the output grid *without* changes.
2.  **Preserve Gray:** The fourth row (index 3) of the input grid is copied to the output grid without changes.
3.  **Conditional Transformation:** The fifth row (index 4) of the output grid is determined by the following rules, applied to each column:
    *   **Gray to Blue (Conditional):** If the pixel in the fourth row (index 3) of the *input* grid is gray (5), *and* the corresponding pixel in the third row (index 2) of the input grid is *not* blue(1), then the corresponding pixel in the fifth row (index 4) of the *output* grid becomes blue (1).
    *   **Blue to Gray:** If the pixel in the third row (index 2) of the *input* grid is blue (1), then the corresponding pixel in the fifth row (index 4) of the *output* grid becomes gray (5).
    * **Other Colors:** All other pixels are copied to the output without changes.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)  # Initialize output as a copy

    rows = input_grid.shape[0]
    cols = input_grid.shape[1]

    # Iterate through the input grid, applying transformation logic
    for i in range(rows):
        for j in range(cols):
            if i < 3:
                #copy rows 0,1,2
                pass
            elif i == 3: #row 4
                # gray remains grey
                pass
            elif i == 4: #row 5
                #grey becomes blue if row[3] grey AND row[2] not blue
                if input_grid[3,j] == 5 and input_grid[2,j] != 1:
                    output_grid[i,j] = 1
                # blue in input row 2, becomes grey in output row 5
                if input_grid[2,j] == 1:
                    output_grid[i,j] = 5
    return output_grid
```

