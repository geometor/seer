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

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
        shape: Two separate 2x1 vertical and 1x2 horizontal azure blocks.
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        positions: [(1,1), (2,1), (2,2), (3,4), (3,5), (4,5)]
        shape:  Two separate 2x1 vertical and 1x2 horizontal azure blocks.
      - color: 1 (blue)
        positions: [(1,2), (4,4)]
        shape: Two single blue cells.
```

**Natural Language Program:**

The transformation rule can be described as follows:

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. There are two distinct shapes formed by azure colored cells: two cells forming a vertical line, and two cells forming a horizontal line.

2.  **Preserve Azure Objects:** Copy all azure colored areas to the output grid, in their respective locations.

3.  **Introduce Blue Pixel, Top:** Identify the azure object with the upper-leftmost coordinate. Add a blue (color 1) pixel to the right of its upper-rightmost coordinate.

4. **Introduce Blue Pixel, Bottom:** Identify the azure object with the bottom-leftmost coordinate. Add a blue pixel (color 1) to the left of its bottom-leftmost coordinate.

In summary, the transformation preserves the azure objects and introduces two blue pixels that are placed according to the described rules.

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
