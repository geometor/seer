"""
Iterate through each pixel of the input grid.
If a pixel is part of an azure ('8') object, check if it's the topmost pixel of that object.
If it is the topmost pixel, change the pixel to its immediate right in the output grid to blue ('1').
All the other pixels stay the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Place a blue (1) pixel to the right of the topmost azure (8) pixel of each azure object.
    """
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    # Find all azure pixels
    azure_pixels = np.where(input_np == 8)
    azure_coords = list(zip(azure_pixels[0], azure_pixels[1]))

    # Group azure pixels into objects
    objects = []
    while azure_coords:
        current_object = []
        queue = [azure_coords[0]]
        while queue:
            row, col = queue.pop(0)
            if (row, col) in azure_coords:
                current_object.append((row, col))
                azure_coords.remove((row, col))
                # Check neighbors (up, down, left, right)
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) in azure_coords:
                        queue.append((nr, nc))
        objects.append(current_object)

    # Find the topmost pixel of each object and place a blue pixel to its right
    for obj in objects:
        # Sort by row (ascending) to find topmost
        obj.sort(key=lambda x: x[0])
        topmost_pixel = obj[0]
        row, col = topmost_pixel
        if col + 1 < cols:  # Check boundary
            output_np[row, col + 1] = 1

    return output_np.tolist()


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