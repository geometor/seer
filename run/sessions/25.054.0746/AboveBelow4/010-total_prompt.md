# AboveBelow4 • 010 • refine_coder

---

Previous Code:
```python
"""
Identifies regions of color 3 (green) in the input grid and inserts color 6 (magenta)
to the immediate horizontal neighbors (left and right) if the neighbor is not already 3 or 6.
If color 3 is at the edge, add 6 only to available side.
The central magenta region remains unchanged.
"""

import numpy as np

def get_horizontal_neighbors(grid, r, c):
    """Gets the valid horizontal neighbors of a cell."""
    neighbors = []
    rows, cols = grid.shape
    if c > 0:
        neighbors.append((r, c - 1))  # Left neighbor
    if c < cols - 1:
        neighbors.append((r, c + 1))  # Right neighbor
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid to find green pixels (3)
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                neighbors = get_horizontal_neighbors(input_grid, r, c)
                for nr, nc in neighbors:
                    # Check if the neighbor is not green or magenta, then set to magenta
                    if input_grid[nr, nc] != 3 and input_grid[nr,nc] != 6:
                        output_grid[nr, nc] = 6

    return output_grid
```

Train Set Results:

## Example 1:

Input:
```
0 0 0 0 0 0 0 0 0 0
0 0 2 2 2 0 0 2 2 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0
```
Expected Output:
```
0 0 0 0 0 0 0 0 0 0
0 0 4 2 2 0 0 4 2 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 4 2 2 0 0 0
4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 2 4 0 0 0 0 0 0
0 0 0 0 2 2 4 0 0 0
0 0 0 0 0 0 0 0 0 0
```
Transformed Output:
```
0 0 0 0 0 0 0 0 0 0
0 0 2 2 2 0 0 2 2 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0
```
![Transformed Image](008-py_05-train-example_1.png)
match: False
pixels_off: 5
size_correct: True
color_palette_correct: True
correct_pixel_counts: False

## Example 2:

Input:
```
0 0 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0
6 6 6 6 6 6 6 6 6 6 6 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
Expected Output:
```
0 0 6 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 6 3 3 0 0
6 6 6 6 6 6 6 6 6 6 6 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
Transformed Output:
```
0 6 3 3 3 6 0 0 0 0 0 0
0 0 0 0 0 0 6 3 3 3 6 0
6 6 6 6 6 6 6 6 6 6 6 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 6 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
![Transformed Image](008-py_05-train-example_2.png)
match: False
pixels_off: 8
size_correct: True
color_palette_correct: True
correct_pixel_counts: False
Okay, let's analyze the results and update the natural language program.

**General Assessment:**

The initial code was based on a misinterpretation of the first training example. The original natural language program assumed that color 6 (magenta) was inserted next to *any* region of color 3 (green).  The second example clearly demonstrates a more specific rule: Color 6 (magenta) is inserted adjacent to color 3 (green) *only if the color 3 is on the border or edge of a larger object*. The existing code doesn't consider what the 3's are part of. It just adds 6's to the horizontal neighbors unconditionally.

**Strategy:**

1.  **Refine Object Identification:** We need to identify objects first, and then find color 3 (green) pixels at the horizontal edges (borders) of these objects.
2.  **Conditional Insertion:** Only insert color 6 (magenta) adjacent to these border pixels.
3.  **Re-evaluate Examples:** Test the refined logic against all examples.

**Metrics and Observations (using code execution where needed):**
Note - I cannot use code here, so I'll describe what I would do and provide estimated results.

*   **Example 1:**
    *   **Objects:** We have several distinct objects (regions of contiguous pixels) in the expected output.
    *   **Color 3 Border Pixels:** The expected output shows that color 4 is being inserted next to color 2.
        *   I would use code to iterate through the *expected output* grid, identify all '2' pixels, check their horizontal neighbors, and see if the neighbor *was* a '4' in the original.
    *   **Action:** Color 4 is being added.
    *   **Error Analysis:**  The current code does not identify different colored regions or find border pixels, explaining the incorrect transformation.
*   **Example 2:**
    *   **Objects:** Several distinct objects.
    *    Color 3 Border Pixels: The expected output shows that color 6 is being insert next to color 3
    *    Action: Color 6 is being added.
    *   **Error Analysis:** Again, the code lacks object and border awareness. It incorrectly adds 6's next to all 3s.

**YAML Fact Block:**

```yaml
objects:
  - description: Contiguous regions of the same color.
    properties:
      - color: integer (0-9)
      - shape: irregular
      - border_pixels: list of (row, col) tuples
        border_definition: horizontal_edges

actions:
  - name: insert_color
    trigger:
      object_property: border_pixels
      color_to_insert: varies by object and color
    location:
      relative_to: border_pixel
      direction: horizontal
    constraints:
        - neighbor_is_not: insert_color
        - neighbor_is_not: trigger_color

color_mapping:
    example_1:
        trigger: 2
        insert: 4
    example_2:
        trigger: 3
        insert: 6
```

**Natural Language Program:**

1.  **Identify Objects:** Divide the input grid into distinct objects, where each object is a contiguous region of pixels of the same color.
2.  **Find Border Pixels:** For each object, identify its border pixels. In this case, a border pixel is defined as a pixel within the object that has a horizontal neighbor (left or right) *that is part of a different object or the edge of the grid*.
3. **Determine Trigger and Insert Colors:** From the training set inputs and outputs, locate pairs of pixels that are horizontally adjacent. One pixel from each pair will be the *trigger*, and the other will be the *insert*. Record all unique trigger, insert pairs.
4.  **Conditional Insertion:**
    * Iterate through all trigger, insert color pairs found in step 3.
    * Locate the border pixels of each object in the input_grid.
    * If a border pixel is a trigger color, check its immediate horizontal neighbors.
        *  If a horizontal neighbor is not the same as either the *trigger* or *insert* color, change that neighboring pixel's color to the *insert* color.


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
