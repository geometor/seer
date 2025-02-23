"""
The transformation rule is a conditional color substitution:
- Maroon (9) becomes Azure (8)
- Yellow (4) becomes Green (3)
- Red (2) becomes Magenta (6)
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

    input_grid = [
        [9, 4, 2],
        [9, 4, 2],
        [9, 4, 2]
    ]

    expected_output_grid = [
        [8, 3, 6],
        [8, 3, 6],
        [8, 3, 6]
    ]
    color_map = {9: 8, 4: 3, 2: 6}
    output_grid = transform(input_grid, color_map)

    print("Expected:", expected_output_grid)
    print("Output  :", output_grid)
    assert output_grid == expected_output_grid, "Test case failed"
    print("SUCCESS!\n")
