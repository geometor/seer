# 6aa20dc0 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 1 1 6 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 1 4 1 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 2 1 1 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
```

<PIL.Image.Image image mode=RGB size=1344x1280 at 0x70FFF4DABBB0>

**output:**
```
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 1 1 6 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 1 4 1 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 2 1 1 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 1 1 1 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 1 1 1 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 1 1 1 2 2 2 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 4 4 4 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 4 4 4 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 1 1 1 4 4 4 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 1 1 1 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 1 1 1 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 6 6 6 1 1 1 1 1 1 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
```

<PIL.Image.Image image mode=RGB size=1344x1280 at 0x70FFF4DABCD0>
Okay, here's my analysis of the provided example, focusing on perception, facts, and a natural language program describing the transformation.

**Perception of Elements:**

The input and output grids consist primarily of yellow (4) pixels.  Within the yellow background, there are distinct colored objects (blue (1), red (2), magenta (6)). The output seems to modify these colored objects, possibly expanding or duplicating them, while maintaining their general shape and relative positions.  The key seems to be the interaction of these objects, especially where they touch.

**YAML Fact Documentation:**


```yaml
facts:
  - object_types:
    - background:
      - color: yellow (4)
      - role: static_context
    - colored_shapes:
      - colors: [blue (1), red (2), magenta (6)]
      - role: dynamic_objects
      - properties:
        - shape: irregular, defined by contiguous pixels of the same color
        - size: variable
  - actions:
    - expansion:
      - description: Colored shapes expand based on adjacency to other shapes.
      - trigger: contact between different colored shapes
  - relationships:
    - adjacency:
      - description: Determines where expansion occurs.
      - types:
        - side-by-side:  Pixels share an edge.
        - diagonal: Pixels share a corner.
  - transformation_constraints:
      - relative_position_preserved: true
```


**Natural Language Program:**

1. **Identify Objects:** Locate all contiguous regions of non-yellow pixels. These are the "colored shapes."  Each shape is identified by its unique color (1, 2, or 6).

2. **Detect Contact Points:** For each colored shape, examine its perimeter (both side-by-side and diagonal neighbors). Identify any pixels where different colored shapes are adjacent.

3. **Conditional Expansion - Blue (1):** If a blue shape touches another blue shape, do not expand the blue shape at that adjacency. If a blue shape touches shapes of a *different* color, then fill all adjacent yellow cells in the *entire grid* with the same color and value as the original colored shape.

4. **Conditional Expansion - Red (2):** If a red shape touches other shapes of a *different* color, then extend a single continuous perimeter of the red shape around the the touching shape.

5. **Conditional Expansion - Magenta (6):** If a magenta shape touches shapes of a *different* color, then fill any immediately adjacent yellow cells with the color of the magenta shape.

6. **Background:** All remaining pixels retain their original yellow (4) color.

Key differences between expansion rules:
* Blue expands globally.
* Red extends locally along the point of adjacency.
* Magenta only extends to any adjacent yellow cells.

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
