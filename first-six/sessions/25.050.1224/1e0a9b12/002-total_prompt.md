# 1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79CABA17ABC0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79CABA17AD10>
Okay, let's analyze the transformation between the input and output grids.

**Observations:**

Input Grid:

-   Dimensions: 4x4
-   Colors present: 0 (white), 1 (blue), 4 (yellow), 6 (magenta), 9 (maroon)
-   Objects:
    -   A single blue cell (1) at (3, 0).
    -   Two single yellow cells (4) at (0, 1) and (2, 1).
    -   A single magenta cell (6) at (2,2).
    -    A single maroon cell (9) at (0,3)

Output Grid:

-   Dimensions: 4x4
-   Colors present: 0 (white), 1 (blue), 4 (yellow), 6 (magenta), 9 (maroon)
-   Objects:
    -   A single blue cell (1) at (3, 0).
    -    A single yellow cell (4) at (3,1)
    -   A single magenta cell (6) at (3, 2).
    -   A single maroon cell (9) at (3, 3).

**Transformation Rule (Natural Language Program):**

1.  **Identify Objects:** Locate all non-white cells in the input grid. These are our objects.

2.  **Move Down:** Shift the identified colored cells to the last row of the grid.

3. **Preserve X, Sort by X** The colored cells preserve the column, that is their horizontal (X) position.

4. **Fill with White** Fill the cells that the objects leaved with white.

In summary: The colored cells are moved to the last row of the output, the other cells are filled with white.


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
