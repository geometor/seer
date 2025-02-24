"""
The transformation rule is as follows:
1. The first three rows of the input grid are copied to the output grid without changes.
2. In the fourth row (index 3), gray (5) pixels remain unchanged.
3. In the fifth row (index 4):
    - Gray pixels in row 4 of the input become blue pixels in row 4 of the output.
    - Blue pixels in row 2 (index 2) of the input become gray pixels in row 4 of the output.
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
            if i == 3: #row 4
                # gray remains grey
                pass
            elif i == 4: #row 5
                #grey becomes blue
                if input_grid[i,j] == 5:
                    output_grid[i,j] = 1
                # blue in input row 3, becomes grey in output row 5
                if input_grid[2,j] == 1:
                    output_grid[i,j] = 5
    return output_grid