# 6-0520fde7 • 002 • example_1 - CODE

---

**input**
```
1 0 0 5 0 1 0
0 1 0 5 1 1 1
1 0 0 5 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0
0 2 0
0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
input_grid:
  dimensions: [3, 7]
  objects:
    - color: 1
      positions: [[0, 0], [1, 1], [1, 5], [1, 6], [2, 0]]
      shape: "scattered"
    - color: 5
      positions: [[0, 3], [1, 3], [2, 3]]
      shape: "vertical line"
    - color: 0
      positions: [[0, 1], [0, 2], [0, 4], [0, 5], [1, 0], [1, 2], [1, 4], [2, 1], [2, 2], [2, 4], [2, 5], [2, 6]]
      shape: "background"

output_grid:
  dimensions: [3, 3]
  objects:
    - color: 2
      positions: [[1, 1]]
      shape: "single cell"
    - color: 0
      positions: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
      shape: "background"
```

**Natural Language Program:**

1.  **Identify the vertical line of color 5:** In the input grid, locate the contiguous vertical line of cells with the color 5.

2.  **Change the color:** Change the color of the central cell of the identified vertical line of 5 from 5 to 2.

3.  **Create smaller output:** The output grid is 3x3

4. **Clear other cells**: Set all other cells in a new 3x3 output grid to color 0.

In essence, the transformation isolates the central cell occupied by the object of color 5, changes the color of that cell to 2, and places it in the center of an output grid where all other cells are 0.

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
