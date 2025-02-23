# 2-0ca9ddb6 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

![Image](001-example_1_output.png)

Okay, here's a breakdown of my observations and plan for this task:

**General Assessment:**

The task involves transforming a grid of colored pixels. The input grid seems to have a few isolated pixels of different colors (red and blue in this example), while the output grid introduces new colors (yellow, orange) and expands some of the existing colors into patterns. The background remains white (0). My strategy will be to:

1.  Identify the colored pixels in the input grid.
2.  Analyze their positions and colors.
3.  Look for relationships between input pixel positions/colors and the new/modified pixels in the output grid.
4.  Formulate a rule that explains the transformation.

**Metrics and Observations (using code later to confirm):**

*   **Input:**
    *   One red pixel (value 2).
    *   One blue pixel (value 1).
    *   The rest are white (value 0).
*   **Output:**
    *   The red pixel remains.
    *   Yellow pixels appear around the area of red pixel
    *    The blue pixel remains
    *   Orange pixels appear around and within the blue pixel

**YAML Facts:**


```yaml
input_objects:
  - color: red
    value: 2
    position: (3, 2)  # (row, column) - 0-indexed
  - color: blue
    value: 1
    position: (6, 6)
output_objects:
  - color: red
    value: 2
    position: (3, 2)
  - color: blue
    value: 1
    position: (6, 6)
  - color: yellow
    value: 4
    positions: [(2,1), (2,3), (4,1), (4,3)]
  - color: orange
    value: 7
    positions: [(5,6), (6,5), (6,7), (7,6)]

transformations:
    - type: "add yellow"
      around: red
      shape: plus shape, radius one
    - type: "add orange"
      around: blue
      shape: plus shape, radius one

```


**Natural Language Program:**

1.  **Preserve:** Keep all original red and blue pixels in their original locations.
2.  **Add Yellow:** For the red pixel, add a yellow pixel one step above, one step below and on each side.
3.  **Add Orange:** For the blue pixel, add a orange pixel one step above, one step below and on each side.

Essentially, a cross of yellow pixels is added and centered around the original red pixel and an orange cross is added at the original blue pixel.

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
