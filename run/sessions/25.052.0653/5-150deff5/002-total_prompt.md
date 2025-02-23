# 5-150deff5 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0 0 0 0
0 0 5 5 5 5 5 0 0 0 0
0 0 0 5 5 5 0 0 0 0 0
0 0 0 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 5 0 0 0
0 0 0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0 0
0 0 8 8 2 2 2 0 0 0 0
0 0 0 2 8 8 0 0 0 0 0
0 0 0 2 8 8 8 8 0 0 0
0 0 0 2 0 0 8 8 0 0 0
0 0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_objects:
  - object_1:
      color: 5 (gray)
      shape: irregular, but roughly rectangular sections connected diagonally and orthogonally
      position: centered vertically and horizontally, extends across multiple rows and columns
      size: spans rows 2-7 and columns 3-8, varies in width and height
output_objects:
  - object_1:
      color: 8 (azure)
      shape: maintains a similar shape to the gray object but with some color changes
      position: occupies the same grid cells as the gray object in the input
      size: matches input size but the color 2 sections are carved out of the previous shape.
  - object_2:
      color: 2 (red)
      shape: fills the spaces within the largest connected sections of the azure object
      position: embedded within the azure object, occupying spaces previously held by gray (5)
      size: varies, conforming to the internal spaces of the azure object

```

**Natural Language Description of the Transformation Rule**

1.  **Identify the Gray Object:** In the input grid, locate the contiguous gray (color 5) object. This object is the primary focus of the transformation.

2.  **Change all Gray to Azure:** For all locations where the original object (gray) was, now all will be azure (color 8).

3.  **Change central-connected pixels to Red:** Inside of the gray object, now azure, there are some locations where a pixel has four neighbors (up, down, left, and right). If that is the case, and it creates a connected component inside the azure shape, change it to red (color 2).

**Step-by-step explanation:**
* We have a grey (5) shape.
* We change grey to azure (8)
* Inside, there is a new red (2) shape formed by the following rule.
* A pixel becomes red if it has four azure neighbors, and with other red pixels, forms a connected component.


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
