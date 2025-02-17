# 25.045.0652 • 1-3aa6fb7a • 003 Response

---

*text:*

**Natural Language Program:**

The task is to modify the grid based on connected regions of color '8' (azure).
First, identify all distinct connected components of cells containing the value '8'. Connectivity is defined by adjacency (horizontally or vertically).
For each connected component of '8's:
  1. Find the topmost-leftmost cell within this component. This is the cell with the minimum row index, and among those with the same minimum row index, the minimum column index. Let's call this cell the 'anchor' cell.
  2. Check the cell immediately to the right of the 'anchor' cell. If this cell is within the grid boundaries and its value is '0' (white), change its value to '1' (blue).
  3. Check the cell immediately below the 'anchor' cell. If this cell is within the grid boundaries and its value is '0' (white), change its value to '1' (blue).

This process is applied independently to each connected component of '8's in the input grid to produce the output grid.
