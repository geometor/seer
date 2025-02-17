"""
The transformation rule is as follows:
1. Identify all azure (color 8) objects in the input grid.
2. Copy the azure objects to the output grid.
3. Find every azure object that is adjacent with only one cell in its x or y axis and add a blue (color 1) pixel adjacent to it, where available.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check neighbors
                neighbors = []
                if r > 0:
                    neighbors.append(input_np[r-1, c])
                if r < rows - 1:
                    neighbors.append(input_np[r+1, c])
                if c > 0:
                    neighbors.append(input_np[r, c-1])
                if c < cols - 1:
                    neighbors.append(input_np[r, c+1])

                # Count azure neighbors.
                azure_neighbors = neighbors.count(8)
                
                if azure_neighbors == 1:
                 # Find where to put the blue
                 if r > 0 and input_np[r-1,c] == 0:
                      output_np[r-1,c] = 1
                 elif r < (rows -1) and input_np[r+1, c] == 0:
                      output_np[r+1,c] = 1
                 elif c > 0 and input_np[r,c-1] == 0:
                      output_np[r,c-1] = 1
                 elif c < (cols - 1) and input_np[r, c+1] == 0:
                      output_np[r,c+1] = 1
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