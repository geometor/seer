import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the bottom of their respective columns,
    stacking them from bottom to top.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column
    for j in range(cols):
        # Find non-zero elements in the column
        non_zero_indices = np.nonzero(input_grid[:, j])[0]
        num_non_zero = len(non_zero_indices)

        # Place the non-zero elements in the output grid, starting from the bottom
        for i in range(num_non_zero):
            output_grid[rows - num_non_zero + i, j] = input_grid[non_zero_indices[i], j]

    return output_grid