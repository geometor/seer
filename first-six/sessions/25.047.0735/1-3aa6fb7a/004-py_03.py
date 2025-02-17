"""
The transformation identifies azure (color 8) objects in the input grid.
For each object, it finds the rightmost azure pixel in the top row of the object.
It then places a blue (color 1) pixel to the left of this azure pixel.
All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    processed_pixels = set()  # Keep track of processed pixels

    # Iterate through each cell to find azure objects
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8 and (r, c) not in processed_pixels:
                # Find the top-left pixel of the current object
                top_left_r, top_left_c = r, c

                # Find all connected azure pixels for this object
                object_pixels = []
                stack = [(top_left_r, top_left_c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    if (curr_r, curr_c) not in processed_pixels and 0 <= curr_r < rows and 0 <= curr_c < cols and input_grid[curr_r, curr_c] == 8:
                        object_pixels.append((curr_r, curr_c))
                        processed_pixels.add((curr_r, curr_c))
                        # Explore adjacent pixels
                        stack.extend([(curr_r + 1, curr_c), (curr_r - 1, curr_c),
                                      (curr_r, curr_c + 1), (curr_r, curr_c - 1)])

                # Find the rightmost azure pixel in the top row of the object
                top_row_pixels = [p for p in object_pixels if p[0] == top_left_r]
                rightmost_pixel = max(top_row_pixels, key=lambda x: x[1])

                # Place blue pixel to the left
                paint_r, paint_c = rightmost_pixel
                paint_c -= 1
                if 0 <= paint_c < cols:
                  output_grid[paint_r, paint_c] = 1

    return output_grid.tolist()



if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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