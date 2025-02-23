# 1-3aa6fb7a • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

**Natural Language Program:**

The task is to modify the input grid by identifying connected regions of azure color (color 8) and adding a blue cell (color 1) adjacent to each region. The placement of the blue cell depends on the shape of the azure region, specifically whether it is "left-leaning" or "right-leaning".

Here's the step-by-step transformation rule:

1.  **Identify Azure Regions:** Find all connected components of cells with color 8 in the input grid.
2.  **Analyze Each Region:** For each identified azure region, perform the following steps:
    a. **Determine Bounding Box:** Find the smallest rectangle that encloses the azure region. This is defined by the minimum and maximum row and column indices of the cells in the region.
    b. **Calculate Centroid:** Calculate the average row and average column of all cells in the azure region. This represents the "center of mass" of the region.
    c. **Calculate Bounding Box Center:** Calculate the center point of the bounding box by averaging its minimum and maximum row and column indices.
    d. **Compare Centroid and Bounding Box Center (Column-wise):** Compare the column coordinate of the centroid with the column coordinate of the bounding box center.
        - **If the centroid's column is to the left of the bounding box center's column (smaller column index):** This indicates a "left-leaning" shape. Place a blue cell (color 1) at the top-right corner of the bounding box. That is, at the row corresponding to the minimum row of the bounding box and the column corresponding to the maximum column of the bounding box.
        - **If the centroid's column is to the right of the bounding box center's column (larger column index):** This indicates a "right-leaning" shape. Place a blue cell (color 1) at the bottom-left corner of the bounding box. That is, at the row corresponding to the maximum row of the bounding box and the column corresponding to the minimum column of the bounding box.
    e. **Preserve Azure Region:** Ensure that the azure region itself remains unchanged in the output grid.
3.  **Maintain Background:** All cells in the input grid that are not part of any azure region and are not modified by step 2.d, remain white (color 0) in the output grid.

This process is applied independently to each connected azure region in the input grid to produce the final output grid.
**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
