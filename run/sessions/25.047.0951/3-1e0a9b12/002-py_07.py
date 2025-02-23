"""
1.  **Identify Non-Zero Objects:** Locate all the colored cells (non-zero values) in the input grid.
2.  **Move Objects to the Bottom:** Move all the identified non-zero objects to the last row of the output grid.
3.  **Preserve Horizontal Order:** Maintain their original horizontal order when moving.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    non_zero_elements = []

    # Collect non-zero elements *and* their column indices
    for j in range(input_grid.shape[1]):
        for i in range(input_grid.shape[0]):
            if input_grid[i, j] != 0:
                non_zero_elements.append((j, input_grid[i, j])) # Store column and value

    # Sort non-zero elements by their original column index
    non_zero_elements.sort()

    # Extract just the values, now in the correct order
    sorted_non_zero_values = [value for _, value in non_zero_elements]
    
    # Place them in the last row
    output_grid[-1, :len(sorted_non_zero_values)] = sorted_non_zero_values
    
    
    # Find columns with at least one zero
    zero_cols = []
    for j in range (input_grid.shape[1]):
      for i in range (input_grid.shape[0]):
        if input_grid[i,j] == 0 :
          zero_cols.append(j)
    
    # Remove duplicates
    unique_zero_cols = []
    for col in zero_cols:
      if col not in unique_zero_cols:
        unique_zero_cols.append(col)  
    
    # Fill the second-to-last row with zeros in the appropriate columns.
    row_above = output_grid.shape[0]-2
    output_grid[row_above, unique_zero_cols] = 0

    return output_grid


if __name__ == '__main__':

    input_grid = [
        [0, 4, 0, 9],
        [0, 0, 0, 0],
        [0, 4, 6, 0],
        [1, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 4, 0, 0],
        [1, 4, 6, 9]
    ]

    output_grid = transform(input_grid)
    if (output_grid == expected_output_grid).all():
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:\n", np.array(expected_output_grid))
        print("Transformed Output:\n", output_grid)

    print()
    assert (output_grid == expected_output_grid).all(), "Transformed output does not match expected output."
