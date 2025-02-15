# 25.045.1245 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
The rule preserves the two L-shaped azure objects and adds the color 1 (blue) to the right of the highest point in each object.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    # Find azure (8) objects and their top-most pixel
    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check if it's the top-most part of an L-shape
                if r+1 < rows and input_np[r+1,c] == 8: # Check for something below
                    pass # It is an '8', but is it the top of something?
                
                # Now that we are at the top of the 8s, are we the top of the L?
                
                if r-1 >=0 and input_np[r-1, c] == 8:
                    continue; # There is an 8 above, not the top.

                # Color cell to the right blue if it's within bounds
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
```
