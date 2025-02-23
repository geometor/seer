"""
1.  **Identify the central column:** Find the vertical line of pixels with the color blue (value 1) in the input grid.
2.  **Resize:** The width is changed from the original to a new smaller width of 3.
3.  **Translate:** Create the output grid with the same height as the input.
4. **Recolor:** Change the color of some of the vertical line's pixels from blue (1) to azure (8), based on row.
5. **Fill Surrounding:** Change the remaining of the output grid to white (0).
6. **Alternating Pattern:** If the row index is even, the azure pixel is in column 1. If the row index is odd and there are two azure pixels, they appear on column 1 and 2. If there is only one, it will still be in column 1.

"""

import numpy as np

def find_central_blue_line(grid):
    # Find the column index where all rows have the value 1 (blue).
    rows, cols = grid.shape
    for j in range(cols):
        if np.all(grid[:, j] == 1):
            return j
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    # Find the central blue line's column index.
    blue_line_col = find_central_blue_line(input_grid)

    # Initialize the output grid with the same height as the input and width 3, filled with white (0).
    rows, _ = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # If a blue line was found, replace the corresponding pixels in the output grid with azure (8).
    if blue_line_col != -1:
        for i in range(rows):
            if i % 2 == 0:
                output_grid[i, 1] = 8  # Even rows: azure in the second column (index 1)
            else:
                output_grid[i,1] = 8
                
                # check to see if we need an additional azure
                example = (input_grid, output_grid)
                
                metrics = analyze_example(input_grid, output_grid, output_grid)
                
                if len(metrics['expected_azure_cols']) > 1 :
                    output_grid[i, 2] = 8

    return output_grid

def analyze_example(input_grid, expected_output, actual_output):
    """Analyzes a single example and gathers metrics."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    actual_output = np.array(actual_output)

    # Find blue line column in input
    blue_col = -1
    for j in range(input_grid.shape[1]):
        if np.all(input_grid[:, j] == 1):
            blue_col = j
            break

    # azure pattern
    azure_cols_expected = []
    
    for j in range(expected_output.shape[1]):
        if np.any(expected_output[:,j] == 8):
            azure_cols_expected.append(j)

    metrics = {
        "input_size": input_grid.shape,
        "expected_output_size": expected_output.shape,
        "actual_output_size": actual_output.shape,
        "blue_line_col": blue_col,
        "expected_azure_cols": azure_cols_expected
    }
    return metrics