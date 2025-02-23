import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of non-white pixels."""
    coords = np.argwhere(grid != 0)
    return [tuple(coord) for coord in coords]

def get_metrics(input_grid, expected_output, transformed_output):
    """Analyzes the transformation results."""

    input_non_white = get_non_white_pixels(input_grid)
    expected_non_white = get_non_white_pixels(expected_output)
    transformed_non_white = get_non_white_pixels(transformed_output)

    print("Input Non-White Pixels:", input_non_white)
    print("Expected Non-White Pixels:", expected_non_white)
    print("Transformed Non-White Pixels:", transformed_non_white)

    input_colors = [input_grid[r, c] for r, c in input_non_white]
    expected_colors = [expected_output[r, c] for r, c in expected_non_white]
    transformed_colors = [transformed_output[r, c] for r, c in transformed_non_white]

    print("Input Colors:", input_colors)
    print("Expected Colors:", expected_colors)
    print("Transformed Colors:", transformed_colors)


# Example usage with the provided examples:
input_grid1 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,8,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
expected_output1 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,8,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,8,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
transformed_output1 = np.array([[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
input_grid2 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
expected_output2 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,4,0,1,0,1,0,1,0,1,0,1,0,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,4,0,1,0,1,0,1,0,1,0,1,0,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
transformed_output2 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,4,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0]])
input_grid3 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
expected_output3 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,4,0,3,0,3,0,3,0,3,0,3,0,3,0,3,0,4,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,8,0,0,0,0,0,0,0,8,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,8,0,0,0,0,0,0,0,8,0,0,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,3,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,4,0,3,0,3,0,3,0,3,0,3,0,3,0,3,0,4,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
transformed_output3 = np.array([[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,4,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

get_metrics(input_grid1, expected_output1, transformed_output1)
get_metrics(input_grid2, expected_output2, transformed_output2)
get_metrics(input_grid3, expected_output3, transformed_output3)
