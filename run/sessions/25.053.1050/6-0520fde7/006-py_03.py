"""
1.  **Initialize Output:** Create a 3x3 output grid filled with white pixels (color 0).
2.  **Determine Center Column:** Find the middle column of the *input* grid using integer division (`input_width // 2`).
3. **Iterate over each position** Iterate through all nine positions (row, col) of the 3x3 *output* grid (from 0,0 to 2,2).
4. **Check Input:** check if the value of the input is 0 at the relative
   position:
      - row = output grid row
      - column = center column + output grid col
5. **Set output value.** if it is a 0, set the current position in output to 2.
6.  **Return:** Return the 3x3 output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Determine the center column of the input grid
    center_col = input_grid.shape[1] // 2

    # Iterate through all positions in the output grid
    for row in range(3):
        for col in range(3):
            # Calculate the corresponding position in the input grid
            input_row = row
            input_col = center_col + col -1 #adjust to the output grid coordinate

            # Check if the input_col is within the bounds of input_grid
            if 0 <= input_row < input_grid.shape[0] and 0 <= input_col < input_grid.shape[1]:
                # Check if the corresponding input pixel is 0
                if input_grid[input_row, input_col] == 0:
                    # Set the output pixel to 2
                    output_grid[row, col] = 2

    return output_grid