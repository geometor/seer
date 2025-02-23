"""
1.  Identify all objects of color 8 (azure).
2.  For each identified object, find the top-most pixel.
3.  Place a pixel of color 1 (blue) immediately to the right of this top-most pixel.
4. If placing it to the right is not possible because that location does not exist, do not place any pixel.
"""

import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    output_array = np.copy(input_array)
    rows, cols = input_array.shape

    # Find all pixels with color 8
    azure_pixels = np.where(input_array == 8)
    azure_coords = list(zip(azure_pixels[0], azure_pixels[1]))

    # Group pixels into objects (contiguous regions)
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
        if (r,c) not in visited:
            new_object = []
            queue = [(r,c)]
            visited.add((r,c))

            while queue:
                curr_r, curr_c = queue.pop(0)
                new_object.append((curr_r, curr_c))
                neighbors = get_neighbors(curr_r, curr_c)
                for nr, nc in neighbors:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            objects.append(new_object)

    # For each object, find the top-most pixel and add a blue pixel to the right
    for obj in objects:
        # Find top-most pixel (lowest row index)
        top_pixel = min(obj, key=lambda x: x[0])
        top_row, top_col = top_pixel

        # Add blue pixel to the right if possible
        if top_col + 1 < cols:
            output_array[top_row, top_col + 1] = 1

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