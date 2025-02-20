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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

Here's a YAML block summarizing my initial observations:

```yaml
input_grid:
  size: 9x11
  objects:
    - color: 5 (gray)
      shape: irregular, but generally two connected components
      position: centered, spanning rows 2-7 and columns 2-7
    - color: 0 (white)
      shape: background
      position: fills the entire grid
output_grid:
  size: 9x11
  objects:
    - color: 8 (azure)
      shape: similar to the gray object in the input, two connected components
      position: same as the gray object in the input
    - color: 2 (red)
      shape: fills the "holes" and borders gray objects
      position: within the gray object's original outline
    - color: 0 (white)
      shape: background
      position: fills the entire grid
```

**Determining the Transformation Rule**

Here's a step-by-step natural language description of the transformation:

1.  **Identify the Gray Object:** Locate the contiguous region of gray (5) cells in the input grid. This object has two main connected components.

2.  **Change the main shape color:** For the gray object to azure (8).

3.  **Identify inside parts:** Locate the parts inside both gray objects.

4.  **Change the inside color:** Change this parts into red (2).

**Natural Language Program**
1. Find the gray object (color 5).
2. Copy gray object into output.
3. Change gray object color into azure (8).
4. Identify parts inside object.
5. Fill this parts with red (2).

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
