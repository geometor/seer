# 1b2d62fb • 009 • example_5 - NLP

---
Okay, let's analyze this example.

**YAML Observation:**

```yaml
input_grid:
  size: 5x7
  objects:
    blue_line:
      color: 1
      shape: vertical line
      position: center column
    maroon_pixels:
      color: 9
      shape: scattered
      position: surrounding the blue line
    white_pixels:
      color: 0
      shape: scattered
      position: surrounding the blue line

output_grid:
  size: 5x3
  objects:
    azure_pixels:
      color: 8
      shape: horizontal line
      position: second to last row, last two columns
    white_pixels:
      color: 0
      shape: background
      position: filling the remaining cells
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Blue Pixels:** Locate all pixels colored blue (value 1) in the input grid.

2.  **Resize the Grid:** The output grid maintains the same number of rows (5) as the input grid but reduces the width to 3 columns.

3.  **Map Blue to Azure:** If a blue pixel is in column 3 of the input, then put azure in (row, 1) of the output.

4.  **Fill Remaining with White:** All cells in the output grid that do not have an azure pixel placed in them are set to white (value 0).

**Explanation:**
This example presents the same scenario and rule as previous tests. The current program should be enough.

```python
import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of blue pixels in each row.
    The output grid has a width of 3 and the same number of rows as the input.
    If a blue pixel exists anywhere in columns 0, 1, or 2 of a given row,
    an azure pixel (8) is placed in position (row, 0) of the output grid.
    If a blue pixel exists in column 3 of a given row, an azure pixel is
    placed in position (row, 1) of the output grid.
    If a blue pixel exists in columns 4, 5, or 6 of a given row, an azure
    pixel is placed in (row, 2) of the output grid.  All other cells are 0.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 1:
                if j in [0, 1, 2]:
                    output_grid[i,0] = 8
                if j == 3:
                    output_grid[i,1] = 8
                if j in [4,5,6]:
                    output_grid[i,2] = 8

    return output_grid
```

