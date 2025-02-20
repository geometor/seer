import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero cells to the bottom of their columns,
    preserving their original order.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)  # Convert to NumPy array *immediately*
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    for j in range(cols):
        # Get the non-zero elements in the current column.
        column_values = input_grid[:, j]
        non_zero_values = column_values[column_values != 0]

        # Place the non-zero elements at the bottom of the output column.
        output_grid[rows - len(non_zero_values):, j] = non_zero_values

    return output_grid.tolist()