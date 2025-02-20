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