# 1-3aa6fb7a • 004 • example_2 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)  # First line
          - (4,4), (5,4)  # Second line
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)
          - (4,4), (5,4)
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,2)
          - (4,4)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Description of Transformation:**

1.  **Identify Objects:** In the input grid, we have two vertical lines of color 8 (azure), each two cells high. The rest of the grid is filled with color 0 (white).

2.  **Detect Changes:** We can see changes in the output inside each one of the azure lines. In the output grid, the azure lines that were found in the input, are kept intact.

3.  **Describe Action:** Within each azure line, the program searches for the cell located immediately to the right of the top cell of each vertical line. The color of this cell is changed to 1 (blue). If the cell to the right of the bottom cell of each line is also azure, it keeps its original color.

**Natural Language Program**
```
for each vertical azure line in the input:
    find top_cell
    find right_neighbor = cell to the right of the top_cell
    set color of right_neighbor to blue
    
```

```python
"""
The transformation rule identifies vertical lines of color 8 (azure) in the input grid.
For each of these lines, it finds the cell immediately to the right of the top cell of the line.
The color of this cell is then changed to 1 (blue) in the output grid. The azure lines themselves are kept.
"""

import numpy as np

def find_vertical_lines(grid, color):
    """
    Finds vertical lines of a specified color in the grid.
    Returns a list of (row, col) tuples representing the top cell of each line.
    """
    lines = []
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_lines = find_vertical_lines(input_grid, 8)

    for top_row, top_col in azure_lines:
        # Find the cell to the right of the top cell
        right_neighbor_row = top_row
        right_neighbor_col = top_col + 1

        # Check if the right neighbor is within bounds
        if right_neighbor_col < output_grid.shape[1]:
            output_grid[right_neighbor_row, right_neighbor_col] = 1

    return output_grid
```


**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

![Image](003-example_2_input.png)


**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

![Image](003-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: three 2x1 vertical lines, and a couple of single cells
        positions:
          - (0,4), (1,4)
          - (0,5), (1,5)
          - (2,2), (3,2)
          - (3,3), (4,3)
          - (5,4)
          - (6,3), (6,4)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: Same vertical components as the input
        positions: the vertical components from the input are preserved
      - color: 1 (blue)
        shape: single cells
        positions:
          - (0,5)
          - (2,3)
          - (5,3)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Description of Transformation:**

1.  **Identify Objects:** In the input grid, we observe some vertical components of color 8 (azure), made of contiguous cells of the same color stacked on top of each other forming columns. The remaining cells have color 0 (white).

2.  **Detect Changes:** The azure vertical lines in the input grid remain unchanged in the output grid. However, new single cells of color 1 (blue) appear in the output grid.

3.  **Describe Actions:**
    -   The transformation identifies the azure vertical lines and preserves them.
    -   For each azure line, it finds the top cell and identifies the cell to the right. The color of this cell to the right is changed to 1 (blue).

**Natural Language Program:**

```
for each vertical azure line in the input:
    find top_cell
    find right_neighbor = cell to the right of the top_cell
    set color of right_neighbor to blue

```

The natural language program and the Python implementation are identical to the first example, as the underlying transformation rule is the same. The code correctly handles multiple vertical lines of color 8 and places the blue cell to the right of the top cell of each identified line.

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
