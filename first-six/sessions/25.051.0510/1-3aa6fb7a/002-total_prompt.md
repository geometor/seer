# 1-3aa6fb7a • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: Two separate 2x1 vertical lines, and two separate 1x2 horizontal lines.
      positions:
        - [1,1] , [2,1] # Vertical line 1
        - [2,2] # Vertical Line 1
        - [3,4], [3,5] # Horizontal line 1
        - [4,5] # Horizontal line 2
    - color: 0 (white)
      shape: background
      position: everywhere else

output_grid:
  size: 7x7
  objects:
      - color: 8 (azure)
        shape: Two separate 2x1 vertical lines, and two separate 1x2 horizontal lines.
        positions:
          - [1,1] , [2,1] # Vertical line 1
          - [2,2] # Vertical Line 1
          - [3,4], [3,5] # Horizontal line 1
          - [4,5] # Horizontal line 2
      - color: 1 (blue)
        shape: Single pixel
        positions:
          - [1,2]
          - [4,4]
      - color: 0 (white)
        shape: background
        position: everywhere else
```

**Natural Language Program (Step-by-step transformation):**

1.  **Identify Objects:** The input grid consists of azure (8) colored objects and the white (0) background. The azure objects appear as two disconnected 2x1 vertical lines and two 1x2 horizontal lines.

2.  **Detect Change:** Comparing input to output, new blue (1) pixels appear.

3.  **Locate Blue Pixel Positions:**
    *   A blue pixel appears to the immediate right of the *topmost* vertical azure line. Specifically, it is at position [1,2].
    *    A blue pixel appears to the immediate left of the *bottommost* horizontal azure line. Specifically, at [4,4].

4. **Transformation Rule:** The overall transformation rule is:
    * Find the topmost vertical line of color 8. Place color 1 to the immediate right of the top of that segment.
    * Find the bottommost horizontal line of color 8. Place a color 1 to the immediate left of that segment.
    *   The azure (8) elements and the white (0) background remain unchanged.

In simple terms. The azure objects remain where they are, but one blue pixel is added to the right of the highest vertical azure line, and another is added to the left of the lowest horizontal azure line.

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
