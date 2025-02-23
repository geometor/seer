# 1e0a9b12 • 002 • example_1 • investigate_coder

---

# Example

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7C67C764B880>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7C67C764B9D0>
Okay, here's my analysis of the provided example input-output pair.

**Perception of Elements:**

The task involves two 4x4 grids. The input grid contains single-digit integers (0-9), representing different colors. The output grid appears to be a rearrangement of some of the input grid's elements. Some elements are removed and the locations of other elements are changed. The most notable change is that many non-zero elements have moved to the bottom row.

**YAML Block (Facts):**


```yaml
facts:
  - type: grid
    dimensions: 4x4
    elements: integers (0-9)
    description: input grid
  - type: grid
    dimensions: 4x4
    elements: integers (0-9)
    description: output grid
  - observation: Non-zero elements from the input grid are present in the output grid, many in the bottom row.
  - observation: Zero elements in the input are typically zero in the output.
  - observation: The positions of elements can change between the input and output.
  - observation: Some elements present in the input might be absent in the output.
  - action: move
    description: Elements are repositioned within the grid.
  - action: filter
    description: Some values in the input might not present in the output.
```


**Natural Language Program:**

1.  **Identify** all non-zero elements in the input grid.
2.  **Move** all the non-zero elements to the last row of the output grid.
3.  **Preserve order**: arrange the non-zero elements in the last row from left to right in the same order they were encountered scanning the original image from left to right and top to bottom.
4.  **Fill** all other cells of the output grid with zeros.

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
