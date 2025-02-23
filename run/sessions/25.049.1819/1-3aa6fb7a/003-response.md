# 1-3aa6fb7a • 003 • example_2 - NLP

---

*text:*

Okay, let's analyze the second example provided.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      positions: [[0,4], [0,5], [1,5]]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [[2,2], [3,2], [3,3]]
    - color: 8 (azure)
      shape: L-shape
      positions: [[5,4],[6,4],[6,5]]
  size: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      positions: [[0,4], [0,5], [1,5]]
    - color: 1 (blue)
      shape: single cell
      positions: [[1,4]]
    - color: 8 (azure)
      shape: L-shape (rotated)
      positions: [[2,2], [3,2], [3,3]]
      - color: 1 (blue)
        shape: single cell
        positions: [[2,3]]
    - color: 8 (azure)
        shape: L-shape
        positions: [[5,4],[6,4],[6,5]]
    - color: 1 (blue)
      shape: single cell
      positions: [[5,3]]
  size: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can see three distinct L-shaped objects of color 8 (azure).

2.  **Object Persistence:** The three azure L-shapes remain unchanged from the input to the output grid.

3.  **Detect Change:** New cells of color blue (1) appear.

4.  **Specify Insertion Rule:** The rule from the previous example appears to hold:
    *   Find each azure (8) colored L-shape.
    *   Examine the cell to the right of the vertex of the "L".
    *   If the cell is 0, change it to color blue (1). There are variations.
    * Top L-shape's vertex: [[0,4],[0,5],[1,5]], cell to the right: [[1,4]]
    * Middle L-shape's vertex: [[3,3],[3,2],[2,2]], cell to the right: [[2,3]]
    * Bottom L-shape's vertex: [[6,5],[6,4],[5,4]], cell to the right: [[5,3]]

5. **Confirm the rule**: In the cases of top L-shape: vertex (0,4), we insert 1 at (1,4), for vertex (2,2), we inserted 1 at (2,3), and for vertex (6,5) insert 1 at (5,3).

**Transformation Rule Summary**
The transformation is to find the azure (8) L-shapes. For each azure L-shape vertex, if an empty cell is present at its right, the program will turn this cell color blue (1). Other cells are left unchanged.

```python
"""
The transformation is to find the azure (8) L-shapes. For each azure L-shape vertex, if an empty cell is present at its right, the program will turn this cell color blue (1). Other cells are left unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the vertex of each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for the four possible L-shape orientations
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
                elif grid[r + 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r,c))
                elif grid[r - 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r,c))
                elif grid[r - 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(output_grid, 8)

    # Change the color of the cell to the right of the vertex to 1 (blue)
    for r, c in l_shapes:
        if output_grid[r,c] == output_grid[r+1,c] == output_grid[r,c+1] and c + 2 < cols :
            if r-1 >=0 and output_grid[r-1,c+1] == 0: output_grid[r-1, c+1] = 1
        if output_grid[r,c] == output_grid[r-1,c] == output_grid[r,c+1] and c + 2 < cols:
            if r+1<rows and output_grid[r+1,c+1] == 0 : output_grid[r+1,c+1] = 1
        if output_grid[r,c] == output_grid[r+1,c] == output_grid[r,c-1] and c - 2 >= 0 :
             if r-1 >=0 and output_grid[r-1,c-1] == 0: output_grid[r-1, c-1] = 1
        if output_grid[r,c] == output_grid[r-1,c] == output_grid[r,c-1]  and c-2>=0:
            if r+1 < rows and output_grid[r+1,c-1] == 0 : output_grid[r+1,c-1] = 1

    return output_grid
```

