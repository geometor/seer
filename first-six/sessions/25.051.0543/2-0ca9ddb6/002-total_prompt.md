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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(2, 1), (2, 3), (4, 1), (4, 3)]
      shape: four single cells forming a pattern around red
    - color: 7 (orange)
      positions: [(5, 5), (6, 5), (7, 5), (6, 7)]
      shape: four single cells in L-shape around the blue object
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell. In this case, we have a red cell at (3, 2) and a blue cell at (6, 6).

2.  **Yellow Surround:** For the red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3. **Orange Surround:** For the blue cell create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4.  **Preserve Original Objects:** The original red and blue cells remain in their original positions in the output grid.

**Natural Language Program**
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.

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
