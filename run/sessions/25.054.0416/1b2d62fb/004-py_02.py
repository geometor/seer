"""
1.  **Identify Center Column:** Find the vertical column in the input grid that contains a contiguous line of blue (1) pixels. This is the center column.
2.  **Determine Extraction Region:** Define a 5x3 region centered on the identified center column. The vertical position is determined such that the first row of the blue is always in position row 1.
3.  **Extract Region:** Create new output by copying the 5x3 extraction region.
4. **Color Replacement**: Within the extracted region
    - all blue (1) pixels are changed to azure (8).
    - All other colors are converted to black (0).

5.  **Output:** The resulting 5x3 modified subgrid is the output.
"""

import numpy as np

def find_blue_line_center(grid):
    # Find the column indices where blue (1) forms a vertical line
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i,j] == 1:
                if all(grid[k, j] == 1 for k in range(i, rows) if k < rows):
                  return j, i
    return -1, -1


def transform(input_grid):
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)

    # Find the central feature (vertical blue line) and top blue pixel row
    center_col, top_row = find_blue_line_center(input_grid)
    
    # Calculate start row index such that top_row is at index 0
    start_row = top_row -1

    # Calculate the extraction boundaries
    start_row = max(0, start_row)
    end_row = start_row + 5
    start_col = center_col - 1
    end_col = center_col + 2
    
    # Ensure that we don't go out of the bounds
    
    end_row = min(input_grid.shape[0], end_row)
    start_col = max(0, start_col)
    end_col = min(input_grid.shape[1], end_col)

    # Create output grid initialized with zeros
    output_grid = np.zeros((5, 3), dtype=int)

    # Extract the region and handle cases when region is not fully available, padding with black.
    extracted_region = input_grid[start_row:end_row, start_col:end_col]

    # Determine slice of extracted region to copy
    extracted_rows, extracted_cols = extracted_region.shape
    output_grid[:extracted_rows, :extracted_cols] = extracted_region
    
    # Modify colors within the extracted region
    output_grid[output_grid == 1] = 8  # Blue to azure
    output_grid[(output_grid != 0) & (output_grid != 8)] = 0 # Other non-black and non-azure to black

    return output_grid.tolist()