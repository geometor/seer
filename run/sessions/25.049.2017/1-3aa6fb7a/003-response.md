# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids in this second example.

**YAML Block Summary**

```yaml
observations:
  input_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
    size: [7, 7]
  output_grid:
    objects:
      - color: 8
        shape: irregular
        positions: [[0, 4], [0, 5], [1, 5], [2, 2], [3, 2], [3, 3], [5, 4], [6, 3], [6, 4]]
      - color: 1
        shape: single_cell
        positions: [[1, 4], [2, 3], [5,3]]
    size: [7, 7]
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we have several objects of color `8` (azure).

2.  **Preserve Some, Change Some:**
    Most of azure color `8` remains at the same positions.
    Some pixels of color `8` changes to color `1`.
    The changed `8` are at positions next to color `8`.

3. **Identify Changing Cells Position:** The cells that are changed are:
    -   The single azure cell in the top object, adjacent to another azure cell.
    -   One azure cell in the center object, adjacent to another azure cell.
    -   One azure cell in the bootom object, adjacent to another azure cell.

**Transformation Rule (In Natural Language)**

The rule can be summarized as follows:

Locate all of `8` colored pixels that forms a group (at least 2). For each group, find the pixel that have another pixel in the group adjacent to it. For all this cases, change color `8` by color `1`. Keep the rest of the grid equal.

This program and the Python code are the same that the previous case.

