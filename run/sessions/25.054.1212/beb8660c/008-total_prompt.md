# beb8660c • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 1
0 0 0 0
2 2 2 0
0 0 0 0
0 3 3 0
0 0 0 0
8 8 8 8
```

<PIL.Image.Image image mode=RGB size=256x448 at 0x7BFC44367820>

**output:**
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
0 0 3 3
0 2 2 2
8 8 8 8
```

<PIL.Image.Image image mode=RGB size=256x448 at 0x7BFC48A63190>
Okay, here's a breakdown of my observations and proposed transformation rule for the example:

**Perception of Elements:**

The task involves manipulating a grid of colored pixels. The primary operation seems to be a rearrangement or shifting of colored blocks (contiguous pixels of the same color) within the grid. The colors themselves remain unchanged, only their positions are altered. There appears to be a downward movement of blocks, potentially filling empty spaces (represented by white pixels, value 0) below them.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      - dimensions: 7x4 (rows x columns)
      - cell_values: [0-9] # Representing colors
  - type: block
    properties:
      - color: [blue, red, green, azure] # Determined by cell_values
      - shape: contiguous_pixels
      - movement: downward
      - constraint: within_grid_boundaries

actions:
  - name: shift_blocks_down
    description: Move blocks of pixels downward, filling empty spaces below.

relationships:
  - type: spatial
    description: Blocks can be above, below, or adjacent to other blocks or empty spaces.
  - type: containment
    description: The grid contains all blocks.
```


**Natural Language Program:**

1.  **Identify Blocks:** Recognize all contiguous blocks of non-zero colored pixels within the input grid.
2.  **Shift Down:** Move each identified block downwards as far as possible. The block will stop moving down when it reaches the bottom edge, any non-zero pixel or when empty pixels on other rows are present.
3. **Preserve the bottom row:** The bottom row should always be fixed and it should not move.

In summary, the transformation rule is to "shift all contiguous non-zero color blocks down, filling the spaces, but keep the bottom row fixed.".

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
