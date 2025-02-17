"""
The transformation rule is a conditional color substitution, defined by a mapping.
This approach allows for different mappings in different examples.
"""

import numpy as np

def transform(input_grid, color_map):
    """
    Transforms the input grid based on a provided color map.

    Args:
      input_grid: The input grid as a list of lists.
      color_map: A dictionary where keys are input colors and values are output colors.

    Returns:
      The transformed grid as a list of lists.
    """
    output_grid = np.array(input_grid, copy=True)
    rows, cols = output_grid.shape

    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]
            # else:  # Optional: Handle colors not in the map (leave unchanged)
            #     pass

    return output_grid.tolist()

if __name__ == '__main__':
    # Example 1
    input_grid_1 = [
        [3, 1, 2],
        [3, 1, 2],
        [3, 1, 2]
    ]
    expected_output_grid_1 = [
        [4, 2, 3],
        [4, 2, 3],
        [4, 2, 3]
    ]
    color_map_1 = {3: 4, 1: 2, 2: 3}
    output_grid_1 = transform(input_grid_1, color_map_1)
    print("Example 1:")
    print("Expected:", expected_output_grid_1)
    print("Output  :", output_grid_1)    
    assert output_grid_1 == expected_output_grid_1, "Example 1 failed"
    print("SUCCESS!\n")


    # Example 2
    input_grid_2 = [
        [2, 3, 8],
        [2, 3, 8],
        [2, 3, 8]
    ]
    expected_output_grid_2 = [
        [6, 4, 9],
        [6, 4, 9],
        [6, 4, 9]
    ]
    color_map_2 = {2: 6, 3: 4, 8: 9}
    output_grid_2 = transform(input_grid_2, color_map_2)
    
    print("Example 2:")
    print("Expected:", expected_output_grid_2)
    print("Output  :", output_grid_2)
    assert output_grid_2 == expected_output_grid_2, "Example 2 failed"
    print("SUCCESS!\n")


    # Example 3
    input_grid_3 = [
        [5, 8, 6],
        [5, 8, 6],
        [5, 8, 6]
    ]
    expected_output_grid_3 = [
        [1, 9, 2],
        [1, 9, 2],
        [1, 9, 2]
    ]
    color_map_3 = {5: 1, 8: 9, 6: 2}
    output_grid_3 = transform(input_grid_3, color_map_3)

    print("Example 3:")
    print("Expected:", expected_output_grid_3)
    print("Output  :", output_grid_3)    
    assert output_grid_3 == expected_output_grid_3, "Example 3 failed"
    print("SUCCESS!\n")

