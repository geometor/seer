# 1cf80156 • 008 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0
0 0 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x795F858DE230>

**output:**
```
1 0 0
1 1 0
0 1 0
1 1 1
0 0 1
```

<PIL.Image.Image image mode=RGB size=192x320 at 0x795F84D03550>
Okay, here's my analysis of the example input-output pair, presented as a report:

**Perception of Elements:**

The input is a 12x12 grid, and the output is a 5x3 grid. The input grid contains a connected shape made of blue (1) pixels against a background of white (0) pixels. This shape resembles a stylized, downward-pointing arrow or triangle. The output grid appears to be a cropped and possibly rotated/reflected version of the blue shape in the input, with the surrounding white pixels removed.

**YAML Block - Facts:**


```yaml
objects:
  - id: background
    color: white (0)
    property: static
  - id: shape
    color: blue (1)
    property: connected, irregular
    relation: contained_within(background)
  - id: output_grid
     property: cropped_version, possibly_transformed
     relation: derived_from(shape)
transformations:
 - action: identify
   target: shape
   description: isolate the single interconnected blue (1) shape.
 - action: crop
   target: shape
   description: Remove all rows and columns that only contain background pixels.
 - action: rotate or reflect
    target: cropped shape
    description: it's unclear if this is a rotation or flip, but the shape changes, there may be a simple reorientation of a cropped bounding box of the shape
```


**Natural Language Program:**

1.  **Isolate the Shape:** Identify the single connected component of blue (1) pixels within the input grid. This constitutes the "shape".
2.  **Bounding Box:** Determine the smallest rectangular bounding box that completely encloses the shape.
3.  **Crop:** Extract the portion of the grid within the bounding box, removing all surrounding rows and columns containing only white (0) pixels.
4.  **Orientation?**: a transformation is performed, best described as selecting a minimal set of rows and columns that fully enclose the extracted shape.

The transformation's essence is extracting the core shape, removing the extraneous background, and reorienting the extracted portion.

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
