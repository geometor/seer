"""
Identify Azure Objects: Locate all azure (color 8) pixels in the input grid.

Place Blue Pixel: For every separated azure object made out of more than one pixel, detect the azure color with the highest x and lowest y, and place a new blue (color 1) pixel directly to its right.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    visited = np.zeros((rows, cols), dtype=bool)
    
    def get_neighbors(r, c):
        neighbors = []
        if r > 0 and input_np[r-1, c] == 8:
            neighbors.append((r-1, c))
        if r < rows - 1 and input_np[r+1, c] == 8:
            neighbors.append((r+1, c))
        if c > 0 and input_np[r, c-1] == 8:
            neighbors.append((r, c-1))
        if c < cols - 1 and input_np[r, c+1] == 8:
            neighbors.append((r, c+1))
        return neighbors

    def dfs(r, c, current_object):
        visited[r, c] = True
        current_object.append((r, c))
        for nr, nc in get_neighbors(r, c):
            if not visited[nr, nc]:
                dfs(nr, nc, current_object)

    objects = []
    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8 and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)

    for obj in objects:
        if len(obj) > 1:
            # Find rightmost-uppermost pixel
            rightmost_uppermost = None
            for r, c in obj:
                if rightmost_uppermost is None:
                    rightmost_uppermost = (r, c)
                else:
                    if c > rightmost_uppermost[1]:
                        rightmost_uppermost = (r, c)
                    elif c == rightmost_uppermost[1] and r < rightmost_uppermost[0]:
                        rightmost_uppermost = (r,c)

            # Place blue pixel to the right
            if rightmost_uppermost:
              r,c = rightmost_uppermost
              if c + 1 < cols:
                output_np[r, c + 1] = 1

    return output_np.tolist()


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."