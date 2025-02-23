# 4-0d3d703e • 002 • example_1 - CODE

---

**input**
```
3 1 2
3 1 2
3 1 2
```

![Image](000-example_1_input.png)


**output**
```
4 5 6
4 5 6
4 5 6
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block for Observations:**

```yaml
input_grid:
  dimensions: 3x3
  objects:
    horizontal_lines:
      color_sequence: [3, 1, 2]
      count: 3
      description: Three horizontal lines, each with the same color sequence (3, 1, 2).
output_grid:
  dimensions: 3x3
  objects:
    horizontal_lines:
      color_sequence: [4, 5, 6]
      count: 3
      description: Three horizontal lines, each with the same color sequence (4, 5, 6).
transformation:
  type: color_mapping
  details: Each color in the input grid is mapped to a different color in the output grid. The spatial arrangement remains identical.
```

**Natural Language Description of the Transformation Rule:**

The input grid consists of three horizontal lines, each with the color sequence 3, 1, 2. The output grid also has three horizontal lines. However, the colors have been transformed according to a specific mapping:

1.  Color 3 (green) in the input is replaced by color 4 (yellow) in the output.
2.  Color 1 (blue) in the input is replaced by color 5 (gray) in the output.
3.  Color 2 (red) in the input is replaced by color 6 (magenta) in the output.

The positions, sizes, and shapes of the objects (horizontal lines) remain unchanged; only the colors are altered based on the above mapping. There are no rotations, reflections or translations. The transformation consists on a color mapping.

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
