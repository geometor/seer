"""
1.  **Identify White Regions:** Scan the input grid and identify contiguous regions (shapes) of white (0) pixels.
2.  **Remove Interior White:** Remove the region, without removing pixels of different colors that border this shape.
3.  **Copy Other Pixels:** Copy all non-white pixels from the input grid to the output grid, preserving their original color and position.
4. **Output final grid.** The result is an output that looks like the input but without interior white filled areas.
"""

import numpy as np

def find_white_regions(grid):
    """Finds contiguous regions of white pixels in the grid."""
    white_regions = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_region):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != 0:
            return
        visited.add((r, c))
        current_region.append((r, c))
        # Explore adjacent cells
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 0 and (r, c) not in visited:
                current_region = []
                dfs(r, c, current_region)
                white_regions.append(current_region)
    return white_regions

def transform(input_grid):
    """Transforms the input grid by removing interior white regions."""
    
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find contiguous regions of white pixels
    white_regions = find_white_regions(input_grid)

    # Remove the identified white regions
    for region in white_regions:
        # Check if the region is completely surrounded by non-white pixels.
        is_interior = True
        for r,c in region:
             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1, 1), (-1,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if input_grid[nr,nc] == 0:
                        is_interior = False
                        break
                else:
                  is_interior = False
                  break
             if not is_interior:
                 break


        if is_interior:
            for r, c in region:
                output_grid[r,c] = 0

    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 0:
          output_grid[r,c] = 0

    #Remove white pixels
    for r in range(rows):
      for c in range(cols):
        if output_grid[r,c] == 0:
            is_interior = True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1, 1), (-1,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                  if output_grid[nr,nc] == 0:
                      is_interior=False
                      break
                else:
                  is_interior = False
                  break
            if is_interior:
              output_grid[r,c] = -1 #Mark as remove

    rows, cols = output_grid.shape
    final_grid = []
    for r in range(rows):
      row = []
      for c in range(cols):
        if output_grid[r,c] != -1:
          row.append(output_grid[r,c])
      if row:
        final_grid.append(row)

    final_grid = np.array(final_grid)

    return final_grid