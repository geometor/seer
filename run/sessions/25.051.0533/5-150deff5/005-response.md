# 5-150deff5 • 005 • example_3 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in this third example.

**YAML Observations**

```yaml
observations:
  input_grid:
    objects:
      - color: 5 (gray)
        shape: irregular, roughly rectangular and linear arrangements
        positions: various, forming a discontinuous pattern
        size: varies
    background:
      - color: 0 (white)
        shape: fills the entire grid
  output_grid:
    objects:
      - color: 8 (azure)
        shape: parts of the gray regions, typically the rightmost or bottommost parts
        positions: corresponding to parts of the gray regions
        size: varies
      - color: 2 (red)
        shape: fills remaining spaces that were part of the gray object
        positions: replacing gray
    background:
      - color: 0 (white)
        shape: fills the remaining space

```

**Natural Language Program**

Here's a step-by-step description of the observed transformation:

1.  **Identify Objects:** First, identify the distinct objects in the input grid. These are the contiguous regions of gray (5) cells.

2.  **Partial Color Transformation**: The gray cells within the input grid are changed to one of two colors:
    *   Azure (8): The rightmost gray pixels within a row are turned into azure.
    *   Red (2): The remaining gray pixels, other than the rightmost, become red.

3.  **Bounding Box**: It's implicitly understood that we only consider transformations within the bounding box encompassing the original gray objects.

**Summary of the Rule**

The transformation rule can be summarized as follows:

1.  Locate all gray (5) colored regions.
2.  Within each contiguous horizontal segment of a gray region, change all gray cells to red (2) except the rightmost cell.
3.  Change the rightmost gray cell in each contiguous horizontal segment to azure (8).

```python
"""
The transformation rule can be summarized as follows:

1.  Locate all gray (5) colored regions.
2.  Within each contiguous horizontal segment of a gray region, change all gray cells to red (2) except the rightmost cell.
3.  Change the rightmost gray cell in each contiguous horizontal segment to azure (8).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                # Find the rightmost cell in this contiguous horizontal segment
                c_end = c
                while c_end + 1 < cols and output_grid[r, c_end + 1] == 5:
                    c_end += 1

                # Change the rightmost cell to azure (8)
                output_grid[r, c_end] = 8

                # Change the remaining cells in the segment to red (2)
                for c_inner in range(c, c_end):
                    output_grid[r, c_inner] = 2
                
                c = c_end # optimization

    return output_grid
```

