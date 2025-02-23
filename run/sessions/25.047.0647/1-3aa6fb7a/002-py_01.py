"""
Identify azure (color 8) objects. For the topmost azure pixel of each object,
place a blue pixel (color 1) one position to its right.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    # Find azure pixels
    azure_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                azure_pixels.append((r, c))

    # Group azure pixels into objects (not strictly necessary for this simple case, but good practice)
    # For this specific problem, we can bypass object grouping as the rule works on individual top pixels
    # Instead, directly find and process the top pixels

    processed_top_pixels = set() # added to keep the top azure cells
    for r, c in azure_pixels:
      is_top = True
      for r2, c2 in azure_pixels:
        if (r2 == r -1) and (c2 == c):
          is_top = False
          break
      if is_top:
        # Place blue pixel
        if c + 1 < cols:
          output_np[r, c + 1] = 1
          processed_top_pixels.add((r,c))

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