import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by applying a color substitution cipher.
    """
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # define the color mapping
    color_map = {
        2: 6,  # red to magenta
        3: 4,  # green to yellow
        8: 9   # azure to maroon
    }

    # iterate through the grid and apply the color mapping
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid

# Example 1
input1 = np.array([[3, 1, 2], [3, 1, 2], [3, 1, 2]])
expected1 = np.array([[4, 5, 6], [4, 5, 6], [4, 5, 6]])
transformed1 = transform(input1)
print("Example 1:")
print("Input:\n", input1)
print("Expected:\n", expected1)
print("Transformed:\n", transformed1)
print("Match:", np.array_equal(transformed1, expected1))
print("-" * 20)

# Example 2
input2 = np.array([[2, 3, 8], [2, 3, 8], [2, 3, 8]])
expected2 = np.array([[6, 4, 9], [6, 4, 9], [6, 4, 9]])
transformed2 = transform(input2)
print("Example 2:")
print("Input:\n", input2)
print("Expected:\n", expected2)
print("Transformed:\n", transformed2)
print("Match:", np.array_equal(transformed2, expected2))
print("-" * 20)

# Example 3
input3 = np.array([[5, 8, 6], [5, 8, 6], [5, 8, 6]])
expected3 = np.array([[1, 9, 2], [1, 9, 2], [1, 9, 2]])
transformed3 = transform(input3)
print("Example 3:")
print("Input:\n", input3)
print("Expected:\n", expected3)
print("Transformed:\n", transformed3)
print("Match:", np.array_equal(transformed3, expected3))
print("-" * 20)

# Example 4
input4 = np.array([[9, 4, 2], [9, 4, 2], [9, 4, 2]])
expected4 = np.array([[8, 3, 6], [8, 3, 6], [8, 3, 6]])
transformed4 = transform(input4)
print("Example 4:")
print("Input:\n", input4)
print("Expected:\n", expected4)
print("Transformed:\n", transformed4)
print("Match:", np.array_equal(transformed4, expected4))
print("-" * 20)