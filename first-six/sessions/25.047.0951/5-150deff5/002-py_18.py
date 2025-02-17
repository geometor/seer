"""
1.  **Identify the Object:** Locate the single object in the input grid that is not color 0 (the background). In this case, it's the shape made of color 5.

2.  **Decompose into components**: The input 'E' shape is made up of four components: top bar, bottom bar, vertical bar, and middle bar.

3.  **Change the color in horizontal bars:** find the top and bottom horizontal components of this shape. Change the color of the components. The top horizontal bar changes to 8. The bottom horizontal bar also changes to 8.

4.  **Change the color in vertical and middle bars:** change the color of the other parts of the E shape (vertical and middle bars) to color 2.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the bounding box of the object
    coords = np.argwhere(input_grid == 5)
    if coords.size == 0:
        return output_grid.tolist() # Returns an all zero array when there is no object with color 5.
    
    min_row, min_col = coords.min(axis=0)
    max_row, max_col = coords.max(axis=0)

    # Top 2x2 square
    output_grid[min_row:min_row+2, min_col:min_col+2] = 8

    # Bottom 2x2 square
    output_grid[max_row-1:max_row+1, min_col:min_col+2] = 8
    
    # Remaining parts of "E": Vertical bar on the left, middle bar
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 5:
          if not ((r >= min_row and r < min_row+2 and c>= min_col and c < min_col + 2) or (r >= max_row-1 and r < max_row+1 and c>= min_col and c < min_col+2)):
            output_grid[r,c] = 2


    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0],
        [0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 5, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 8, 2, 2, 2, 0, 0, 0, 0],
        [0, 0, 0, 2, 8, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 8, 8, 8, 8, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid)

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."