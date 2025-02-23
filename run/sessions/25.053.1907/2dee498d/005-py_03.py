import numpy as np

def get_dimensions(grid_string):
    grid = np.array([list(map(int, row.split())) for row in grid_string.split('\n')])
    return grid.shape

# Example 1
input1 = "4 5 1 1 5 4 4 5 1\n5 5 5 5 5 5 5 5 5\n1 5 4 4 5 1 1 5 4"
expected1 = "4 5 1\n5 5 5\n1 5 4"
print(f"Example 1: Input Dimensions: {get_dimensions(input1)}, Expected Dimensions: {get_dimensions(expected1)}")

# Example 2
input2 = "2 0 0 1 2 0 0 1 2 0 0 1\n4 2 1 4 4 2 1 4 4 2 1 4\n4 1 2 4 4 1 2 4 4 1 2 4\n1 0 0 2 1 0 0 2 1 0 0 2"
expected2 = "2 0 0\n4 2 1\n4 1 2\n1 0 0"
print(f"Example 2: Input Dimensions: {get_dimensions(input2)}, Expected Dimensions: {get_dimensions(expected2)}")

# Example 3
input3 = "2 1 2 1 2 1\n2 3 2 3 2 3"
expected3 = "2 1\n2 3"
print(f"Example 3: Input Dimensions: {get_dimensions(input3)}, Expected Dimensions: {get_dimensions(expected3)}")
