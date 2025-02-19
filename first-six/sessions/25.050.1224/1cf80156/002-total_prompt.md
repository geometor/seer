# 1cf80156 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0 0 0
0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 2 2 2 0 0 0 0 0 0
0 0 0 2 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x640 at 0x79CABAB06380>

**output**
```
0 2 2 2
0 0 2 0
2 2 2 0
2 0 2 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79CABA179BD0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  size: 10x12
  objects:
    - color: 2 (red)
      shape: Irregular, composed of two 3x1 rectangles connected at a corner. One rectangle is in the 3rd row and one in the 5th row.
      position: Centered horizontally, spanning rows 3-6.
    - color: 0 (white)
      shape: Background
      position: Everywhere else.

output_grid:
  size: 4x4
  objects:
    - color: 2 (red)
      shape: Multiple 1x1 squares
      position: Occupying a checkerboard pattern.
    - color: 0 (white)
      shape: Multiple 1x1 squares
      position: Occupying a checkerboard pattern.
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Object:** In the input grid, locate the single contiguous object composed of red (color 2) cells.

2.  **Isolate:** Disregard background white pixels.

3. **Bounding Box:** find the smallest rectangle containing the red object.

4.  **Crop and Resize:** Extract the object within bounding box, and resize the object to 4x4.

5. **Checkerboard:** within this resized region, all red pixels stay red and white pixels are replaced by a chekerboard pattern.

**Explanation and Reasoning**

The core transformation involves isolating the non-background object (the red shape), finding its bounding box, and reducing it to a smaller, patterned square. The final 4x4 is filled with checkerboard pattern where the original pixels of the shape are located.

This natural language program sufficiently describes the input to output transformation.

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
