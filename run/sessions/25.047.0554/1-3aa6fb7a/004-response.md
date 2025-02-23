# 1-3aa6fb7a • 004 Response

---

*text:*

Okay, here's the Python implementation based on the natural language program I described:




*text:*

```python
"""
Iterate through each cell of the input grid.
If a cell is azure (color 8), check if it's the top-most cell of a contiguous azure object.
If it is the top-most cell, change the cell immediately to its right in the output grid to blue (color 1).
If the azure cell is on the right border so there are no cells to the right, make no change.
Copy all the cells from input to output
"""

import numpy as np

def transform(input):
    input_array = np.array(input)
    output_array = np.copy(input_array)
    rows, cols = input_array.shape

    for r in range(rows):
        for c in range(cols):
            if input_array[r, c] == 8:
                # Check if it's the top-most cell of an azure object
                is_topmost = (r == 0) or (input_array[r-1, c] != 8)

                if is_topmost:
                    # Change the cell to the right to blue (if within bounds)
                    if c + 1 < cols:
                        output_array[r, c+1] = 1

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

```
