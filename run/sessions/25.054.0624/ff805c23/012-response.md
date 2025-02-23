# ff805c23 • 012 • refine_coder

---
```python
"""
1.  **Identify Target Object:** Find the largest contiguous region of pixels where the colors present are any of: green (3), magenta (6) or gray (5). *One* of these colors will be the "primary" color of the object.
2.  **Determine Bounding Box:** Find the smallest rectangle (bounding box) that completely encloses the target object identified in step 1.
3. **Extract Sub-grid**: Extract the section of the input grid defined by this bounding box.
4. **Simplify Colors Inside Bounding Box**: Within the extracted sub-grid, change all pixels that *aren't* white (0) to the primary color.
5.  **Apply White Pixel Rule:** For each white (0) pixel *within the sub-grid*:
    *   Check its immediate neighbors (up, down, left, right) *in the original input grid*.
    *   If *any* of these neighbors are a color other than white (0), change the pixel in the subgrid to the primary color.
    *   Otherwise, leave the pixel as white (0).
6. **Output:** The modified sub-grid is the output.
"""

import numpy as np

def find_largest_object(grid, colors):
    """Finds the largest contiguous block containing the specified colors."""
    visited = set()
    max_size = 0
    max_coords = None
    primary_color = None

    def dfs(r, c, current_colors):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] not in current_colors:
            return 0, None
        visited.add((r, c))
        count = 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            c, _ = dfs(new_r, new_c, current_colors)
            count += c
        return count, grid[r,c]

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] in colors and (r, c) not in visited:
                # Find all connected colors first
                connected_colors = set()
                q = [(r,c)]
                seen = {(r,c)}
                while q:
                    cr, cc = q.pop()
                    connected_colors.add(grid[cr,cc])
                    for dr, dc, in [(0,1), (0,-1), (1,0), (-1, 0)]:
                        nr, nc = cr + dr, cc+dc
                        if 0<=nr<grid.shape[0] and 0<=nc<grid.shape[1] and (nr, nc) not in seen and grid[nr, nc] in colors:
                            q.append((nr, nc))
                            seen.add((nr, nc))
                
                size, color = dfs(r, c, connected_colors) #now run dfs using only these colors
                if size > max_size:
                    max_size = size
                    max_coords = (r, c)
                    primary_color = color

    return max_coords, max_size, primary_color

def get_bounding_box(grid, start_coords, colors):
    """
    Finds the smallest bounding box around a connected region,
    but only considers connected cells that contains specific colors
    """
    if start_coords is None:
        return (0,0), (0,0)

    rows, cols = grid.shape
    min_row, min_col = start_coords
    max_row, max_col = start_coords

    visited = set()
    q = [start_coords]
    visited.add(start_coords)
    
    while q:
        r,c = q.pop(0)
        min_row = min(min_row, r)
        max_row = max(max_row, r)
        min_col = min(min_col, c)
        max_col = max(max_col, c)

        for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
            nr, nc = r + dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and grid[nr, nc] in colors:
                q.append((nr,nc))
                visited.add((nr,nc))

    return (min_row, min_col), (max_row, max_col)


def get_neighbor_colors(grid, r, c):
    """Returns a set of the colors of the immediate neighbors."""
    rows, cols = grid.shape
    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    neighbor_colors = set()
    for nr, nc in neighbors:
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbor_colors.add(grid[nr, nc])
    return neighbor_colors

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    grid = np.array(input_grid)

    # 1. Identify Target Object
    colors = {3, 5, 6}
    start_coords, _, primary_color = find_largest_object(grid, colors)

    #if we can't find the object return empty
    if start_coords is None:
        return []

    #find the colors that exist within the object
    connected_colors = set()
    q = [start_coords]
    seen = {start_coords}
    while q:
        cr, cc = q.pop()
        connected_colors.add(grid[cr,cc])
        for dr, dc, in [(0,1), (0,-1), (1,0), (-1, 0)]:
            nr, nc = cr + dr, cc+dc
            if 0<=nr<grid.shape[0] and 0<=nc<grid.shape[1] and (nr, nc) not in seen and grid[nr, nc] in colors:
                q.append((nr, nc))
                seen.add((nr, nc))   

    # 2. Determine Bounding Box
    top_left, bottom_right = get_bounding_box(grid, start_coords, connected_colors)

    # 3. Extract Sub-grid
    sub_grid = grid[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
    output_grid = sub_grid.copy()

    # 4. Simplify Colors Inside Bounding Box
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if output_grid[r, c] != 0:
                output_grid[r, c] = primary_color

    # 5. Apply White Pixel Rule
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if output_grid[r, c] == 0:
                # Get original grid coordinates
                orig_r = top_left[0] + r
                orig_c = top_left[1] + c
                neighbor_colors = get_neighbor_colors(grid, orig_r, orig_c)
                if any(color != 0 for color in neighbor_colors):
                    output_grid[r, c] = primary_color

    return output_grid.tolist()
```
