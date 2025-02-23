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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations:**

*   **Input Grid:**
    *   Contains a single red (2) pixel near the center-top.
    *   Contains a single blue (1) pixel near the center-bottom.
    *   The rest of the grid is filled with white (0) pixels.
*   **Output Grid:**
    *   The red (2) pixel remains in the same position.
    *   The blue (1) pixel remains in the same position.
    *    Two yellow (4) pixels appear, one to the left and to the right of the red one, like one row above and one row below.
    *   Three orange(7) pixels appear around the blue pixel, specifically to the left, right and above of it.
    *    The rest of the grid is filled with white (0) pixels.

**Natural Language Program:**

1.  **Identify Key Pixels:** Locate the single red (2) pixel and the single blue (1) pixel in the input grid.
2.  **Preserve Positions:** Keep the red (2) and blue (1) pixels in their original positions in the output grid.
3.  **Add Yellow Pixels:** For the red (2) pixel:
    *   Place a yellow (4) pixel one row *above* and one column to the *left*.
    *   Place another yellow (4) pixel one row *above* and one column to the *right*.
    *    Place a yellow (4) pixel one row *below* and one column to the *left*.
    *   Place another yellow (4) pixel one row *below* and one column to the *right*.
4.  **Add Orange Pixels:** For the blue (1) pixel:
    *    Place an orange (7) pixel one column to the *left*.
    *   Place an orange (7) pixel one column to the *right*.
    *    Place an orange (7) pixel one row *above*.
5. **Fill Remaining:** All other cells in the output grid remain white (0).

**Summary of actions**

The transformation preserves the positions of the existing red and blue pixels and introduces new yellow pixels around the red one and orange pixels around the blue pixel based on their positions. The remaining pixels keep being white.

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
