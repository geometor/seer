# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
1. **Identify Azure Blocks:** Find all contiguous regions of color 8 (azure) in the input grid. Consider these regions as distinct objects, which we will call "azure blocks".
2. **Order Azure Blocks by Minimum Column Index:** For each azure block, determine its minimum column index (the smallest column index among all cells in the block). Order all identified azure blocks based on their minimum column index, from smallest to largest.
3. **Process the First (Leftmost) Azure Block:** Take the first block in the ordered list (the one with the smallest minimum column index). Find the cell within this block that comes first in reading order (top to bottom, left to right). In the output grid, place a cell of color 1 (blue) immediately to the right of this first cell. Ensure that the placement is within grid boundaries.
4. **Process the Last (Rightmost) Azure Block:** Take the last block in the ordered list (the one with the largest minimum column index). Find the cell within this block that comes last in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this last cell. Ensure that the placement is within grid boundaries.
5. **Process Middle Azure Blocks (if any):** For any azure blocks that are positioned between the first and the last in the ordered list, process each of them. For each such block, find its first cell in reading order. In the output grid, place a cell of color 1 (blue) immediately to the left of this first cell. Ensure that the placement is within grid boundaries.
6. **Result:** The resulting grid, after applying these steps, is the final output grid.
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

def order_blocks_by_min_col(objects):
    """Order blocks based on their minimum column index."""
    blocks_with_min_col = []
    for obj in objects:
        min_col = min(cell[1] for cell in obj)
        blocks_with_min_col.append((obj, min_col))
    return sorted(blocks_with_min_col, key=lambda x: x[1])

def find_first_cell(block):
    """Find the first cell in reading order."""
    return sorted(block, key=lambda cell: (cell[0], cell[1]))[0]

def find_last_cell(block):
    """Find the last cell in reading order."""
    return sorted(block, key=lambda cell: (cell[0], cell[1]), reverse=True)[0]

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    
    output_grid = np.copy(input_grid)
    azure_blocks = find_objects(input_grid, 8)

    if not azure_blocks:
        return output_grid

    ordered_blocks = order_blocks_by_min_col(azure_blocks)

    # Process the first (leftmost) block
    first_block, _ = ordered_blocks[0]
    first_cell = find_first_cell(first_block)
    if first_cell[1] + 1 < output_grid.shape[1]:
        output_grid[first_cell[0], first_cell[1] + 1] = 1

    # Process the last (rightmost) block
    last_block, _ = ordered_blocks[-1]
    last_cell = find_last_cell(last_block)
    if last_cell[1] - 1 >= 0:
        output_grid[last_cell[0], last_cell[1] - 1] = 1

    # Process middle blocks (if any)
    for block, _ in ordered_blocks[1:-1]:
        first_cell = find_first_cell(block)
        if first_cell[1] - 1 >= 0:
            output_grid[first_cell[0], first_cell[1] - 1] = 1

    return output_grid
```

