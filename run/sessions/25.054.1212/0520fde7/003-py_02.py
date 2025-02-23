import numpy as np

# Example Data (reproduced for easy access)
inputs = [
    np.array([[1, 0, 0, 5, 0, 1, 0],
              [0, 1, 0, 5, 1, 1, 1],
              [1, 0, 0, 5, 0, 0, 0]]),
    np.array([[1, 1, 0, 5, 0, 1, 0],
              [0, 0, 1, 5, 1, 1, 1],
              [1, 1, 0, 5, 0, 1, 0]]),
    np.array([[0, 0, 1, 5, 0, 0, 0],
              [1, 1, 0, 5, 1, 0, 1],
              [0, 1, 1, 5, 1, 0, 1]])
]
outputs = [
    np.array([[0, 0, 0],
              [0, 2, 0],
              [0, 0, 0]]),
    np.array([[0, 2, 0],
              [0, 0, 2],
              [0, 2, 0]]),
    np.array([[0, 0, 0],
              [2, 0, 0],
              [0, 0, 2]])
]

def get_central_column(grid):
    _, num_cols = grid.shape
    central_col_index = num_cols // 2
    return central_col_index

for i, (input_grid, output_grid) in enumerate(zip(inputs, outputs)):
    central_col_index = get_central_column(input_grid)
    central_column = input_grid[:, central_col_index]
    gray_indices = np.where(central_column == 5)[0]
    expected_red_indices = np.where(output_grid == 2)[0]
    print(f"Example {i+1}:")
    print(f"  Central Column: {central_column}")
    print(f"  Indices of Gray (5) in Central Column: {gray_indices}")
    print(f"Expected Red Indices {expected_red_indices}")