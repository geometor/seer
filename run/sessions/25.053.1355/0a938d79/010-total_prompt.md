# 0a938d79 • 010 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1472x448 at 0x70FA38392350>

**output:**
```
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
```

<PIL.Image.Image image mode=RGB size=1472x448 at 0x70FA383916C0>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids consist of cells containing numerical values, which can be interpreted as colors. The primary colors observed are white (0), blue (1), and green (3). The output grid appears to be a modified version of the input grid, with a specific pattern applied. The input has single instances of blue and green, while the output shows horizontal and vertical sequences of blue and green.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    name: input_grid
    properties:
      - dimensions: 7 x 23
      - cells: integers (0-9)
      - colors: [white, blue, green]
    observations:
      - single blue cell at (0,5)
      - single green cell at (6,8)
  - type: grid
    name: output_grid
    properties:
      - dimensions: 7 x 23
      - cells: integers (0-9)
      - colors: [white, blue, green]
    observations:
     - repeating sequence: blue, white, white, green
     - sequence repeats horizontally and starts at blue cell location
     - sequence repeats vertically and starts at green cell location

relationships:
  - type: transformation
    from: input_grid
    to: output_grid
    rule: "pattern replication"
```


**Natural Language Program:**

1.  **Identify Key Cells:** In the input grid, locate the single blue cell (value 1) and the single green cell (value 3).
2.  **Horizontal Replication (Blue):** Starting from the blue cell's position in the input, replicate the sequence, and moving left and right replace cell value with the pattern `1 0 0 3` (blue, white, white, green) horizontally across the entire row in the output grid.
3.  **Vertical Replication (Green):** Starting from the green cell's position in the input, replicate the sequence , and moving up and down, and replace cell value with the pattern `1 0 0 3` (blue, white, white, green) vertically across the entire column in the output grid.
4. Other cells remain with input cell's value.

In essence, the transformation takes the locations of the blue and green pixels in the input grid and uses them as starting points to generate repeating color sequences horizontally and vertically, respectively, in the output grid.

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
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
