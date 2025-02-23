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

**Natural Language Program:**

1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Determine Leftmost Azure Block:** For each azure block, find its minimum column index (the smallest column index among all cells in the block). Identify the azure block with the overall smallest minimum column index. Let's call this the "leftmost block".
3. **Locate First Cell in Leftmost Block:** Within the "leftmost block", find the cell that appears first in reading order, scanning from top to bottom and left to right. We'll refer to this as the "top-leftmost cell" of the leftmost block in reading order.
4. **Add Blue Cell to the Right of Leftmost Block's First Cell:**  In the output grid, place a cell of color 1 (blue) immediately to the right of the "top-leftmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "top-leftmost cell" is already in the rightmost column).
5. **Determine Rightmost Azure Block:**  For each azure block, again consider its minimum column index. Identify the azure block with the overall largest minimum column index. Let's call this the "rightmost block".
6. **Locate Last Cell in Rightmost Block:** Within the "rightmost block", find the cell that appears last in reading order, scanning from top to bottom and left to right. This can be seen as the "bottom-rightmost cell" of the rightmost block in reading order.
7. **Add Blue Cell to the Left of Rightmost Block's Last Cell:** In the output grid, place a cell of color 1 (blue) immediately to the left of the "bottom-rightmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "bottom-rightmost cell" is already in the leftmost column).
8. **Result:** The resulting grid, after applying these steps, is the final output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify leftmost and rightmost blocks of azure color. Add a blue cell to the right of the first cell (reading order) of the leftmost block and to the left of the last cell (reading order) of the rightmost block."
objects:
  - type: "azure block"
    color: 8
    properties:
      - "contiguous region"
      - "minimum column index"
      - "first cell (reading order)"
      - "last cell (reading order)"
  - type: "blue cell"
    color: 1
    actions:
      - "add to the right of first cell of leftmost azure block"
      - "add to the left of last cell of rightmost azure block"
predicates:
  - "is_leftmost_block(azure_block)"
  - "is_rightmost_block(azure_block)"
  - "first_cell_in_reading_order(azure_block) -> cell"
  - "last_cell_in_reading_order(azure_block) -> cell"
actions:
  - "add_cell_to_right(cell, color=1)"
  - "add_cell_to_left(cell, color=1)"
```
```python
"""
1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Determine Leftmost Azure Block:** For each azure block, find its minimum column index (the smallest column index among all cells in the block). Identify the azure block with the overall smallest minimum column index. Let's call this the "leftmost block".
3. **Locate First Cell in Leftmost Block:** Within the "leftmost block", find the cell that appears first in reading order, scanning from top to bottom and left to right. We'll refer to this as the "top-leftmost cell" of the leftmost block in reading order.
4. **Add Blue Cell to the Right of Leftmost Block's First Cell:**  In the output grid, place a cell of color 1 (blue) immediately to the right of the "top-leftmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "top-leftmost cell" is already in the rightmost column).
5. **Determine Rightmost Azure Block:**  For each azure block, again consider its minimum column index. Identify the azure block with the overall largest minimum column index. Let's call this the "rightmost block".
6. **Locate Last Cell in Rightmost Block:** Within the "rightmost block", find the cell that appears last in reading order, scanning from top to bottom and left to right. This can be seen as the "bottom-rightmost cell" of the rightmost block in reading order.
7. **Add Blue Cell to the Left of Rightmost Block's Last Cell:** In the output grid, place a cell of color 1 (blue) immediately to the left of the "bottom-rightmost cell" identified in the previous step. Ensure that this new blue cell is within the grid boundaries (i.e., do not place it if the "bottom-rightmost cell" is already in the leftmost column).
8. **Result:** The resulting grid, after applying these steps, is the final output grid.
"""

import numpy as np

def find_objects(grid, color):
    """Find contiguous regions of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous cells."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_leftmost_block(objects):
    """Find the leftmost azure block."""
    min_col = float('inf')
    leftmost_block = None
    for obj in objects:
        for row, col in obj:
            if col < min_col:
                min_col = col
                leftmost_block = obj
    return leftmost_block

def find_rightmost_block(objects):
    """Find the rightmost azure block."""
    max_min_col = -1
    rightmost_block = None
    for obj in objects:
        min_col = float('inf')
        for row, col in obj:
            min_col = min(min_col,col)
        if min_col > max_min_col:
            max_min_col = min_col
            rightmost_block = obj
    return rightmost_block

def find_first_cell(block):
    """Find the first cell in reading order."""
    return sorted(block, key=lambda cell: (cell[0], cell[1]))[0]

def find_last_cell(block):
    """Find the last cell in reading order."""
    return sorted(block, key=lambda cell: (cell[0], cell[1]), reverse=True)[0]
def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find azure blocks (objects)
    azure_blocks = find_objects(input_grid, 8)
    
    # Handle edge case: No azure blocks present
    if not azure_blocks:
        return output_grid

    # Find the leftmost block
    leftmost_block = find_leftmost_block(azure_blocks)
    
    # Find the first cell of the leftmost block
    first_cell = find_first_cell(leftmost_block)
    
    # Add a blue cell to the right of the first cell, if possible
    if first_cell[1] + 1 < output_grid.shape[1]:
        output_grid[first_cell[0], first_cell[1] + 1] = 1

    # Find the rightmost block
    rightmost_block = find_rightmost_block(azure_blocks)
        
    # Find the last cell of the rightmost block
    last_cell = find_last_cell(rightmost_block)

    # Add a blue cell to the left of the last cell, if possible
    if last_cell[1] - 1 >= 0:
        output_grid[last_cell[0], last_cell[1] - 1] = 1
        
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

![Image](002-example_2_input.png)


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

![Image](002-example_2_output.png)

**Natural Language Program:**

1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Order Azure Blocks by Minimum Column Index:** For each azure block, determine its minimum column index (the smallest column index among all cells in the block). Order all identified azure blocks based on their minimum column index, from smallest to largest.
3. **Process the First (Leftmost) Azure Block:** Take the first block in the ordered list (the one with the smallest minimum column index). Find the cell within this block that comes first in reading order (top to bottom, left to right). In the output grid, place a cell of color 1 (blue) immediately to the right of this first cell. Ensure that the placement is within grid boundaries.
4. **Process the Last (Rightmost) Azure Block:** Take the last block in the ordered list (the one with the largest minimum column index). Find the cell within this block that comes last in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this last cell. Ensure that the placement is within grid boundaries.
5. **Process Middle Azure Blocks (if any):** For any azure blocks that are positioned between the first and the last in the ordered list, process each of them. For each such block, find its first cell in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this first cell. Ensure that the placement is within grid boundaries.
6. **Result:** The resulting grid, after applying these steps, is the final output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify and order azure blocks by minimum column index. Add blue cells to the right of the first cell of the leftmost block, to the left of the last cell of the rightmost block, and to the left of the first cell of any middle blocks."
objects:
  - type: "azure block"
    color: 8
    properties:
      - "contiguous region"
      - "minimum column index"
      - "first cell (reading order)"
      - "last cell (reading order)"
  - type: "blue cell"
    color: 1
    actions:
      - "add to the right of first cell of the first (leftmost) azure block"
      - "add to the left of last cell of the last (rightmost) azure block"
      - "add to the left of first cell of any middle azure block"
predicates:
  - "is_first_block_in_order(azure_block)"
  - "is_last_block_in_order(azure_block)"
  - "is_middle_block_in_order(azure_block)"
  - "first_cell_in_reading_order(azure_block) -> cell"
  - "last_cell_in_reading_order(azure_block) -> cell"
actions:
  - "add_cell_to_right(cell, color=1)"
  - "add_cell_to_left(cell, color=1)"
```
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
