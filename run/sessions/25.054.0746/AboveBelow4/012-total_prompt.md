# AboveBelow4 • 012 • refine_coder

---

Previous Code:
```python
"""
1. Identify Objects: Divide the input grid into distinct objects, where each object is a contiguous region of pixels of the same color.
2. Find Border Pixels: For each object, identify its border pixels. In this case, a border pixel is defined as a pixel within the object that has a horizontal neighbor (left or right) *that is part of a different object or the edge of the grid*.
3. Determine Trigger and Insert Colors: From the training set inputs and outputs, locate pairs of pixels that are horizontally adjacent. One pixel from each pair will be the *trigger*, and the other will be the *insert*. Record all unique trigger, insert pairs.
4. Conditional Insertion:
    * Iterate through all trigger, insert color pairs found in step 3.
    * Locate the border pixels of each object in the input_grid.
    * If a border pixel is a trigger color, check its immediate horizontal neighbors.
        *  If a horizontal neighbor is not the same as either the *trigger* or *insert* color, change that neighboring pixel's color to the *insert* color.
"""

import numpy as np
from collections import deque

def find_objects(grid):
    """Finds all contiguous objects in a grid."""
    rows, cols = grid.shape
    visited = set()
    objects = []

    def bfs(r, c, color):
        """Performs breadth-first search to find contiguous pixels of the same color."""
        obj = []
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()
            obj.append((row, col))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr, nc] == color:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return obj

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                obj = bfs(r, c, grid[r, c])
                objects.append(obj)
    return objects

def find_horizontal_border_pixels(grid, object_pixels):
    """Finds border pixels with horizontal neighbors of a different color."""
    border_pixels = []
    rows, cols = grid.shape
    for r, c in object_pixels:
        # Check left neighbor
        if c > 0 and grid[r, c - 1] != grid[r, c]:
            border_pixels.append((r, c))
            continue  # Avoid double-counting
        # Check right neighbor
        if c < cols - 1 and grid[r, c + 1] != grid[r, c]:
            border_pixels.append((r, c))
    return border_pixels

def get_trigger_insert_pairs(input_grid, output_grid):
    """
    Identifies pairs of (trigger_color, insert_color) based on horizontal adjacency
    changes between the input and output grids.
    """

    rows, cols = input_grid.shape
    pairs = set()

    for r in range(rows):
        for c in range(cols):
            # Check right neighbor
            if c < cols - 1:
                if input_grid[r,c] != output_grid[r,c] or input_grid[r, c+1] != output_grid[r,c+1]:
                    # something changed here
                    if input_grid[r,c] != input_grid[r,c+1]:
                        # different colors
                        if input_grid[r,c] == output_grid[r,c] and input_grid[r,c+1] != output_grid[r,c+1]:
                            # right changed
                            pairs.add( (input_grid[r,c], output_grid[r,c+1]) )
                        if input_grid[r,c+1] == output_grid[r,c+1] and input_grid[r,c] != output_grid[r,c]:
                            # left changed
                            pairs.add( (input_grid[r,c+1], output_grid[r,c]))

    return pairs

def transform(input_grid, input_grid_2=None, output_grid_2=None): # Added extra example grids
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find Objects
    objects = find_objects(input_grid)

    # 2. Determine Trigger-Insert Pairs (using both examples)
    trigger_insert_pairs = get_trigger_insert_pairs(input_grid, output_grid)
    if input_grid_2 is not None and output_grid_2 is not None:
         pairs2 = get_trigger_insert_pairs(input_grid_2, output_grid_2)
         trigger_insert_pairs = trigger_insert_pairs.union(pairs2)

    # 3. Iterate and apply transformations
    for obj in objects:
        # 3a. Find Horizontal Border Pixels
        border_pixels = find_horizontal_border_pixels(input_grid, obj)

        # 3b. Apply insertion rules
        for trigger_color, insert_color in trigger_insert_pairs:
            for r, c in border_pixels:
                if input_grid[r, c] == trigger_color:
                    # Check left neighbor
                    if c > 0 and input_grid[r, c - 1] != trigger_color and input_grid[r, c - 1] != insert_color:
                        output_grid[r, c - 1] = insert_color
                    # Check right neighbor
                    if c < cols - 1 and input_grid[r, c + 1] != trigger_color and input_grid[r, c + 1] != insert_color:
                        output_grid[r, c + 1] = insert_color

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
![Transformed Image](010-py_06-train-example_1.png)
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
![Transformed Image](010-py_06-train-example_2.png)
match: False
pixels_off: 3
size_correct: True
color_palette_correct: True
correct_pixel_counts: False
Okay, let's analyze the results and refine the natural language program.

**General Assessment:**

The initial approach of identifying objects and horizontal border pixels was partially correct. However, the trigger-insert logic is flawed. It correctly identifies *when* a change should happen (adjacent to a border pixel of a specific color), but it doesn't correctly capture the *directionality* of the change, and relies too heavily on the trigger color being present in output after the change, which may not be the case. Also, the current logic only looks for *horizontal* changes and won't apply a needed change if there are no eligible horizontal neighbors.

The core issue is that the code changes pixels adjacent to the border pixel *only if* those neighboring pixels are *not* the insert or trigger. The code should simply change the neighbor in output to the *insert* color regardless of current value in input *or* output.

The algorithm needs to focus on identifying the *changed* pixels between the input and output grids, and from that, deducing the rule for the change. It should *not* rely on the trigger color remaining unchanged.

**Metrics and Observations**

Here's a summary of the examples, focusing on relevant information for debugging:

**Example 1:**

*   **Input:** Contains objects of color 2 (red) and 4 (yellow).
*   **Output:** Some red pixels adjacent to yellow are replaced with yellow, others are unchanged. Yellow pixels are unchanged.
*   **Observation:** The changed pixels are always where red (2) is to the left or right of yellow (4). Red (2) pixels to the left of yellow become yellow (4). Red (2) pixels to the right of yellow (4) become yellow. Yellow (4) object is the *stable* object and expands into adjacent red (2) pixels.
*   **Mismatch:** The code did not change any pixels.

**Example 2:**

*   **Input:** Contains objects of color 3 (green) and 6 (magenta).
*   **Output:** Some green pixels adjacent to magenta become magenta.
* **Observation:** The changed pixels are always green (3) to the left or right of magenta(6). Green pixels next to Magenta become magenta. Magenta (6) object is the *stable* object which expands into adjacent green (3) pixels.
*   **Mismatch:** The code did not change any pixels.

**YAML Fact Documentation:**

```yaml
examples:
  - id: 1
    stable_object_color: 4  # Yellow
    changing_object_color: 2  # Red
    change_direction: "adjacent" # Red next to yellow changes to yellow
    border: horizontal

  - id: 2
    stable_object_color: 6  # Magenta
    changing_object_color: 3  # Green
    change_direction: "adjacent"   # Green next to magenta changes to magenta.
    border: horizontal
```

**Natural Language Program:**

1.  **Identify Objects:** Divide the input grid into distinct objects, where each object is a contiguous region of pixels of the same color.

2.  **Identify Stable and Changing Colors:** Compare each input/output pair. Determine which color expands into the other color. The expanding color is *stable*, the other color is *changing*.

3. **Find Horizontal Neighbors:** For each pixel in the input grid check its left and right neighbors.

4.  **Apply Rule:**
    *   If a pixel is the *changing* color, and is horizontally adjacent (left or right) to a pixel of *stable* color, the *changing* pixel becomes the *stable* color in the output grid.

**Revised Strategy**
Focus on identifying corresponding pixels in the input and output and determining color adjacency. Then, determine a simple rule that explains what changes. Finally, apply this rule to *all* objects in the input.

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
