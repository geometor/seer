# 5-150deff5 • 002 Response

---

*text:*

Okay, here's the Python code implementing the transformation rule described above:




*text:*

```python
"""
The transformation rule can be described as follows:

1.  **Identify the Object:** Locate the contiguous region of color '5' in the input grid. This forms the primary object.

2.  **Bounding Box (Implicit):** Conceptually, imagine a bounding box around the "5" shaped object.

3. **Color Substitution within the bounding box:** The transformation recolors portions of the object of '5'.

4. **Recolor Rule**: The area defined by color 5 is recolored according to the following rule: The bounding box is divided into two parts:
   + The first part of the shape is the rectangle with the corners in (2,2) and (3,3). And a second shape that are all the rest of the points of color '5'.
   + The first part is recolored to 8.
   + The second part is recolored to 2.

**Step-by-step explanation (symbolic):**

1. Find the connected component of color 5.
2. Consider the coordinates (row, col) = (2,2) and (3,3) of the input. All cells of color 5 in those positions are replaced by color 8 in the output.
3. The rest of the color 5 cells in the original connected component are all replaced by color 2.
4. The background (color 0) remains unchanged.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    rows, cols = input_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 5:
                if r >= 1 and r <=2 and c >=2 and c <=3:
                  output_grid[r,c] = 8
                else:
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
```
