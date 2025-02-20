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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**Observations and Documentation**

Here's a YAML block summarizing my initial findings:

```yaml
task: 001-example_1
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-left)
      position: (1,1) , (2,1), (2,2)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position: (3,4) , (3,5), (4,5)
    - color: 0 (white)
      shape: background
      position: fills the rest
output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-left)
      position: (1,1) , (2,1), (2,2)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position:  (3,4) , (3,5), (4,5)
    - color: 1 (blue)
      shape: single cell
      position: (1,2)
    - color: 1 (blue)
      shape: single cell
      position: (4,4)
    - color: 0 (white)
      shape: background
      position: fills the rest
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case, there are two L-shaped objects.

2.  **Preserve Azure Objects:** The azure objects remain unchanged in their positions and shapes in the output grid.

3.  **Introduce Blue Pixels:** For each azure object, identify the cell immediately to the right of the top-most and left-most corner of the "L". Change the color of these cells to blue (color 1).

    *   For the top-left L-shape, this cell is (1, 2).
    *    For the bottom-right L-shape, this is the cell (4,4).

4. Fill with the color white all the cells that are not azure or blue.

**Natural Language Program**
```
input:  a grid of pixels with colors from 0 to 9.
output: a grid of pixels with colors from 0 to 9.

program:
  for each azure (8) object in input:
    copy object to the output
    let P be the top-left corner of the bounding box that contains the object
    paint in blue the pixel at P.right
  paint in white all other pixels
```

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
