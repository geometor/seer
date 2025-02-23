"""
The transformation rule varies between the examples.

- Example 1: Swap the first and last rows of the input grid. Then reverse the first and last rows.
- Example 2: Reverse each row of the input grid.
- Example 3: Shift each row downwards cyclically. The first row becomes the last row, the second row becomes the first, and the third row becomes the second.
- Example 4: Swap the first and last rows of the input grid. Reverse the first and last rows.
"""

import numpy as np

def transform(input_grid, example_id=None):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)

    if example_id == 1 or example_id == 4:
        # Swap first and last rows
        input_np[[0, -1]] = input_np[[-1, 0]]
        # Reverse first and last rows
        output_np = np.copy(input_np) # create a copy to avoid modifying original
        output_np[0] = output_np[0][::-1]
        output_np[-1] = output_np[-1][::-1]
    elif example_id == 2:
        # Reverse each row
        output_np = np.copy(input_np)
        for i in range(output_np.shape[0]):
            output_np[i] = output_np[i][::-1]
    elif example_id == 3:
        # shift rows down cyclically
        output_np = np.roll(input_np, shift=1, axis=0)

    else:
        # default to do nothing
        output_np = input_np

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()
    return output_grid