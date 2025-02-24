import numpy as np

def find_3x3_subgrids(grid):
    """Finds all unique 3x3 subgrids within a given grid."""
    subgrids = []
    rows, cols = grid.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = grid[i:i+3, j:j+3]
            subgrids.append(subgrid)
    return subgrids

# Example Inputs (as numpy arrays)
example_inputs = [
    np.array([[8, 9, 8], [9, 8, 8], [8, 8, 8], [2, 2, 1], [2, 2, 1], [1, 1, 2], [4, 4, 4], [4, 4, 3], [3, 3, 3]]),
    np.array([[1, 5, 5], [5, 1, 1], [5, 1, 1], [3, 3, 3], [3, 6, 3], [3, 6, 6], [7, 7, 7], [7, 2, 2], [7, 2, 2]]),
    np.array([[2, 2, 2], [2, 2, 3], [2, 3, 3], [5, 7, 7], [7, 5, 5], [7, 5, 5], [8, 8, 1], [1, 8, 1], [1, 8, 1]]),
    np.array([[8, 8, 4], [4, 4, 4], [4, 4, 8], [1, 1, 3], [1, 3, 3], [3, 3, 1], [6, 2, 2], [2, 2, 2], [2, 2, 6]]),
]
example_outputs = [
    np.array([[4, 4, 4], [4, 4, 3], [3, 3, 3]]),
    np.array([[7, 7, 7], [7, 2, 2], [7, 2, 2]]),
    np.array([[8, 8, 1], [1, 8, 1], [1, 8, 1]]),
    np.array([[8, 8, 4], [4, 4, 4], [4, 4, 8]]),

]
# Analyze each example
for idx, (input_grid, output_grid) in enumerate(zip(example_inputs, example_outputs)):
    print(f"Example {idx + 1}:")
    print("Input:\n", input_grid)
    print("Expected Output:\n", output_grid)
    
    subgrids = find_3x3_subgrids(input_grid)

    print("All 3x3 Subgrids:")
    for i, subgrid in enumerate(subgrids):
        print(f"  Subgrid {i+1}:\n{subgrid}")
        if np.array_equal(subgrid, output_grid):
            print(f"    *** MATCHES EXPECTED OUTPUT ***")

    print("-" * 20)