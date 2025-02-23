"""
The transformation rule is a color substitution where each cell's color value in the input grid is incremented by a specific value that depends on the original color. The structure and position of the colored regions remain unchanged.

- If the color is 2, add 4.
- If the color is 1, 3, or 8, add 1.
- If the color is 5 or 6, add 6.
- If the color is 4 or 9, add 9.
- If the input color is any other number, add 1.
- All operations are modulo 10.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by incrementing each cell's color value based on the defined rules.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed output grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Initialize the output grid as a copy of the input grid
    output_array = np.copy(input_array)

    # Apply the color transformation based on the original color
    for i in range(input_array.shape[0]):
        for j in range(input_array.shape[1]):
            if input_array[i, j] == 2:
                output_array[i, j] = (input_array[i, j] + 4) % 10
            elif input_array[i, j] in [1, 3, 8]:
                output_array[i, j] = (input_array[i, j] + 1) % 10
            elif input_array[i, j] in [5, 6]:
                output_array[i, j] = (input_array[i, j] + 6) % 10
            elif input_array[i, j] in [4, 9]:
                output_array[i, j] = (input_array[i, j] + 9) % 10
            else:
                output_array[i,j] = (input_array[i,j] + 1) % 10

    # Convert the NumPy array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid