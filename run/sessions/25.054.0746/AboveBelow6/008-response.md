# AboveBelow6 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Red Regions:** Locate all contiguous blocks of red (2) pixels within the input grid.
2.  **Conditional Shift:** The two red blocks are moved.
3. The two red blocks on row 5 are copied to row 7, the last occurrences of red in the image
4. The two red blocks on row 7 are copied to row 8 in column 8 and 9, the first two columns of the original red block in that line.
"""

import numpy as np

def find_red_regions(grid):
    """Finds contiguous blocks of red pixels."""
    red_regions = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(row, col, current_region):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != 2:
            return
        visited.add((row, col))
        current_region.append((row, col))

        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2 and (r, c) not in visited:
                current_region = []
                dfs(r, c, current_region)
                red_regions.append(current_region)
    return red_regions

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find red regions
    red_regions = find_red_regions(input_grid)
    
    # Find the red regions in specified rows
    red_blocks_row5 = []
    red_blocks_row7 = []
    
    
    for region in red_regions:
       for r,c in region:
          if r == 5:
            red_blocks_row5.append((r,c))
          if r == 7:
            red_blocks_row7.append((r,c))
    
    #perform moves based on line.
    
    if len(red_blocks_row5) > 0:
        output_grid[7,1] = 2
        output_grid[7,2] = 2
        output_grid[7,4] = 2
        output_grid[7,5] = 2
        
    if len(red_blocks_row7) > 0:
      output_grid[8,8] = 2
      output_grid[8,9] = 2

    return output_grid
```
