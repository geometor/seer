# 1a07d186 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x960 at 0x70FFF4DABBB0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 2 0 0 0 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x960 at 0x70FFEBF9FE50>
Okay, here's my analysis of the provided input-output example pair:

**Perception of Elements:**

The task involves 2D grids containing single-digit integers representing different colors. The primary colors observed are white (0), red (2), blue (1), and yellow (4). The transformation seems to involve a selective deletion or movement of certain colored objects/pixels based on their color and possibly their spatial relationship to other objects. The yellow (4) in the input is not in the output.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: [15, 14] # Height x Width
      colors: [0, 1, 2, 4] # white, blue, red, yellow

  - type: object_group
    properties:
      color: 2 # Red
      shape: horizontal_line
      y_coordinate: 3

  - type: object_group
     properties:
        color: 1
        shape: horizontal_line
        y_coordinate: 10

  - type: pixel
    properties:
      color: 4 # Yellow
      coordinates: [1, 9]
      deleted: true

  - type: pixel
    properties:
       color: 1
       coordinates: [ 5, 10 ]
       moved_to: [11,2]

  - type: pixel
    properties:
      color: 2
      coordinates: [ 7, 6 ]
      moved_to: [4,6]

  - type: pixel
    properties:
      color: 2
      coordinates: [13, 10]
      moved_to: [4,10]

  - type: pixel
     properties:
       color: 1
       coordinates: [12, 2]
       moved_to: [11, 2]
```


**Natural Language Program:**

1.  **Identify Key Lines:** Find the two horizontal lines composed of contiguous pixels of the same color: one red (color 2) and one blue (color 1).
2.  **Preserve Lines:** Keep the red and blue horizontal lines intact.
3. **Drop Singletons:** Identify any objects that are a single pixel of one color.
4.  **Move Blue and Red Singletons**:
    *   If the object singleton is the color blue (1), move the objects to the empty row immediately above the solid blue line.
    *   If the object singleton is the color red (2), move the objects to the empty row immediately above the solid red line.
5.  **Remove Yellow:** Delete any single-pixel yellow (4) object.
6.  **Output:** Generate the output grid with the remaining colored object locations after deletions and translations.


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
