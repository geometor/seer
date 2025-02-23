"""
The transformation rule can be described as follows:

1.  Identify all azure (color 8) objects in the input grid.
2.  For each azure object, locate its top-most pixel.
3.  If a pixel to the right of the top-most pixel is within the boundary, and that location is '0', set the value of the output grid at that location to blue (color 1).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Place a blue pixel (1) to the right of the top-most pixel of each azure (8) object.
    """
    input_array = np.array(input_grid)
    output_array = np.copy(input_array)
    rows, cols = input_array.shape

    # Find all azure pixels
    azure_pixels = np.where(input_array == 8)
    azure_coords = list(zip(azure_pixels[0], azure_pixels[1]))

    # Group azure pixels into objects (contiguous regions)
    objects = []
    visited = set()

    def get_neighbors(r, c):
        neighbors = []
        if r > 0 and input_array[r-1, c] == 8:
            neighbors.append((r-1, c))
        if r < rows - 1 and input_array[r+1, c] == 8:
            neighbors.append((r+1, c))
        if c > 0 and input_array[r, c-1] == 8:
            neighbors.append((r, c-1))
        if c < cols - 1 and input_array[r, c+1] == 8:
            neighbors.append((r, c+1))
        return neighbors

    for r, c in azure_coords:
        if (r, c) not in visited:
            new_object = []
            stack = [(r, c)]
            visited.add((r,c))

            while stack:
                curr_r, curr_c = stack.pop()
                new_object.append((curr_r, curr_c))
                neighbors = get_neighbors(curr_r, curr_c)
                for nr, nc in neighbors:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            objects.append(new_object)

    # For each object, find the top-most pixel and place a blue pixel to its right
    for obj in objects:
        top_most_pixel = min(obj, key=lambda x: x[0])
        right_pixel_r, right_pixel_c = top_most_pixel[0], top_most_pixel[1] + 1

        if 0 <= right_pixel_r < rows and 0 <= right_pixel_c < cols and output_array[right_pixel_r, right_pixel_c] == 0:
            output_array[right_pixel_r, right_pixel_c] = 1

    return output_array.tolist()


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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