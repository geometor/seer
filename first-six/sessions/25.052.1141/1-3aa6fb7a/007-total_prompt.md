# 1-3aa6fb7a • 007 • refine_code - CODE

---

Previous Code:
```python
import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def find_1x2_horizontal_rectangles(grid, color):
    """
    Finds coordinates of 1x2 horizontal rectangles
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols-1):
            if grid[r,c] == color and grid[r,c+1] == color:
                rectangles.append(((r,c),(r,c+1)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles_v = find_2x1_vertical_rectangles(output_grid, 8)
    azure_rectangles_h = find_1x2_horizontal_rectangles(output_grid, 8)

    for top_coord, bottom_coord in azure_rectangles_v:
        r_top, c_top = top_coord
        r_bot, c_bot = bottom_coord

        # Check if a 2x2 square can *only* be formed to the right
        can_form_right = (c_top + 1 < output_grid.shape[1] and
                          output_grid[r_top, c_top + 1] == 8 and
                          output_grid[r_bot, c_bot + 1] == 8)
        
        can_form_left = (c_top -1 >= 0 and c_top -2 >=0 and
                        output_grid[r_top, c_top -1] == 8 and
                        output_grid[r_bot, c_top -1] == 8)

        if can_form_right and not can_form_left:
            if c_top - 1 >= 0:
                output_grid[r_top, c_top - 1] = 1  # Place blue to the left

    for left_coord, right_coord in azure_rectangles_h:
        r_left, c_left = left_coord
        r_right, c_right = right_coord

        #Check if 2x2 can only be formed below
        can_form_below = (r_left + 1 < output_grid.shape[0] and
                         output_grid[r_left + 1, c_left] == 8 and
                         output_grid[r_right + 1, c_right] == 8)

        can_form_above = (r_left -1 >= 0 and r_left -2 >= 0 and
                          output_grid[r_left - 1, c_left] == 8 and
                         output_grid[r_left - 1, c_right] == 8)
        if can_form_below and not can_form_above:
            if r_left - 1 >= 0:
                output_grid[r_left - 1, c_left] = 1  # Place blue above
    return output_grid
```

Train Set Results:

**Example 1:**
Input:
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
Expected Output:
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
Transformed Output:
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
![Transformed Image](005-py_04-train-example_1.png)
Status: False

**Example 2:**
Input:
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```
Expected Output:
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```
Transformed Output:
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```
![Transformed Image](005-py_04-train-example_2.png)
Status: False
Okay, let's analyze the provided examples and refine the natural language program to describe the transformation accurately.

**YAML Description of Observations:**

```yaml
task: 005-color_and_fill
summary: |
  The task involves placing a blue (1) pixel adjacent to azure (8) rectangles
  (either 2x1 or 1x2) in specific positions based on whether a 2x2 azure square could be
  formed. It favors completing the 2x2 azure square if possible. If not, and the completion
  can *only* be done in one direction, a blue pixel is placed to force this azure square
  completion if done.

objects:
  - name: azure_rectangle_v
    type: rectangle
    color: 8
    size: 2x1
    position: variable

  - name: azure_rectangle_h
    type: rectangle
    color: 8
    size: 1x2
    position: variable

  - name: blue_pixel
    type: pixel
    color: 1
    size: 1x1
    position: strategically placed adjacent to azure rectangles

predicates:
  - can_form_2x2_square_right: Checks if a 2x1 azure rectangle can form a 2x2 square to its right.
  - can_form_2x2_square_left: Checks if a 2x1 azure rectangle can form a 2x2 square to its left.
  - can_form_2x2_square_below: Checks if a 1x2 azure rectangle can form a 2x2 square below it.
  - can_form_2x2_square_above: Checks if a 1x2 azure rectangle can form a 2x2 square above it.

actions:
  - place_blue_left: Places a blue pixel to the immediate left of a 2x1 azure rectangle.
  - place_blue_above: Places a blue pixel immediately above a 1x2 azure rectangle.

```

**Natural Language Program:**

1.  **Identify Azure Rectangles:** Find all 2x1 vertical and 1x2 horizontal azure (8) rectangles in the input grid.

2.  **Prioritize filling:**
    If a 2x2 azure square can be formed, it is. Do not add a blue square.

3.  **Vertical Rectangles (2x1):** For each 2x1 vertical azure rectangle:

    *   Check if a 2x2 azure square can be formed to the *right* of the rectangle.
    *   Check if a 2x2 azure square can be formed to the *left* of the rectangle.
    *   If a 2x2 square can *only* be formed to the right (and not to the left, ignoring the possibility of formation):
        *   Place a blue (1) pixel immediately to the *left* of the *top* azure pixel of the vertical rectangle.

4.  **Horizontal Rectangles (1x2):** For each 1x2 horizontal azure rectangle:

    *   Check if a 2x2 azure square can be formed *below* the rectangle.
    *   Check if a 2x2 azure square can be formed *above* the rectangle.
    *   If a 2x2 square can *only* be formed below (and not above, ignoring the possibility of formation):
        *  Place a blue (1) pixel immediately *above* the *left* azure pixel of the horizontal rectangle.

5.  **Otherwise**: The output grid remains identical to the input grid.

**Explanation of the Errors and Corrections:**

The previous code was on the right track, but it was missing a crucial part of the logic: the *exclusivity* condition. It should ONLY place the blue pixel if the 2x2 square could be formed in one direction and *not* the other, ignoring the fact that there *is* a direction where a 2x2 square *could* be completed if the blue square was present.

The examples revealed that the blue pixel wasn't being placed when it should have been. This is because the original code was just checking if a square could be completed in one way, and the conditional `if can_form_right` or `if can_form_below` were not enough. The key is to ensure the completion is exclusively possible in only one direction by introducing "and not `can_form_left` and `can_form_above`", respectively.

The description above highlights this logic.

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
