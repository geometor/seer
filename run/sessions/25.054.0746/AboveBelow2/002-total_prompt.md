# AboveBelow2 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 4 4 4 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
0 0 4 4 4 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
0 2 2 2 0 0 2 2 2 0 0 0 0 2 2 2 0 0 0 0
0 2 2 2 0 0 2 2 2 0 0 0 0 2 2 2 0 0 0 0
0 2 2 2 0 0 2 2 2 0 0 0 0 2 2 2 0 0 0 0
0 2 2 2 0 0 0 0 0 0 0 0 0 2 2 2 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1280x1152 at 0x7995F90382E0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 4 4 4 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1280x1152 at 0x7995F8FEFA60>
Okay, here's a breakdown of my observations, documented facts, and a natural language program describing the transformation:

**Perception of Task Elements:**

The task involves identifying and potentially removing or retaining specific colored rectangular objects within a grid. The primary colors involved seem to be blue (1), red (2), green (3), and yellow (4). White (0) appears to act as a background or empty space. The output seems to retain some of the original colored rectangles while removing others. The decision of which to keep, and which to remove is not based on color, only the green and yellow remain.

**YAML Fact Documentation:**


```yaml
facts:
  - observation: |
      The input grid contains multiple rectangular objects of different colors (blue, red, green, yellow) on a white background.
  - object_types:
      - type: rectangle
        properties:
          - color: [blue, red, green, yellow, white]
          - shape: rectangular
          - size: varies
  - actions:
      - name: remove
        description: |
            Certain colored rectangles are completely removed from the grid, replaced by the background color (white).
      - name: retain
        description: |
           Other rectangles remain in the grid
  - selection_criteria: unknown
    - description:
      The criteria to keep specific objects is not obvious
  - relationships:
      - type: spatial
        description: |
            Objects are positioned in different locations within the grid, some are adjacent.
```


**Natural Language Program:**

1.  **Identify Rectangles:** Locate all rectangular shapes formed by contiguous blocks of pixels of the same color (excluding white/0).
2.  **Selective Retention:** Retain any Green and yellow rectangles.
3.  **Removal:** remove red and blue rectangles
4.  **Output:** Produce a new grid with the selected color areas retained and all others replaced with background (white/0).


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
