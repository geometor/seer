# 1b2d62fb • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Locate the central feature:** Find the vertical line of blue (1) pixels in the input grid. It is in the center column.
2.  **Extract a region:** Extract a 5x3 region (a subgrid) from the input. The region of extraction seem to correspond with two row below and two rows above the first occurance of blue. The extraction is always 3 wide and is centered on the central feature.
3.  **Modify colors:** Within this extracted subgrid, locate blue pixels (value 1).
4.  **Replace Color**: Change value of any pixel with the value of 1 to have a value of 8.
5.  **Output:** The modified 3x5 subgrid is the output.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find the column indices where the specified color forms a vertical line
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i,j] == color:
                if all(grid[k, j] == color for k in range(i, rows) if k < rows):
                  return j, i
    return -1, -1

def transform(input_grid):
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)

    # Find the central feature (vertical blue line)
    center_col, top_row = find_vertical_line(input_grid, 1)

    # Calculate the extraction boundaries
    start_row = top_row
    end_row = top_row + 5
    start_col = center_col - 1
    end_col = center_col + 2
    
    # Ensure that we don't go out of the bounds
    start_row = max(0, start_row)
    end_row = min(input_grid.shape[0], end_row)
    start_col = max(0, start_col)
    end_col = min(input_grid.shape[1], end_col)


    # Extract the region
    extracted_region = input_grid[start_row:end_row, start_col:end_col]

    # Create output grid
    output_grid = extracted_region.copy()
    
    # Modify colors: replace 1 (blue) with 8 (azure)
    output_grid[output_grid == 1] = 8

    return output_grid.tolist()
```
