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

**YAML Observation:**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (1,1) # Top-left corner of the object
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (3,4) # Top-left corner of the object
  output_grid:
      - object_1:
          color: 8 (azure)
          shape: L-shape
          position: (1,1)
      - object_2:
          color: 8 (azure)
          shape: L-shape
          position: (3,4)
      - object_3:
          color: 1 (blue)
          shape: single cell
          position: (1,2)
      - object_4:
          color: 1(blue)
          shape: single cell
          position: (4,5)
```

**Natural Language Program:**

1.  **Identify Objects:** In the input grid, we can see two L-shaped objects made of azure (color 8) pixels.

2.  **Preserve Objects:** These objects keep shape, color and location in the output grid.

3. **Add blue pixel:** In the output, a blue pixel (color 1) appears on the right of the corner of each object.

**Transformation Rule (In Natural Language):**

The transformation preserves the two azure L-shaped objects, maintaining their original positions and shapes. Additionally, it adds a single blue pixel (color 1) to the right of each object's corner, in both cases.

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
