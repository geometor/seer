# b775ac94 • 010 • refine_coder

---
```python
"""
Expands colored blocks based on their size and adjacency.  A colored block expands
vertically by a factor of its size. If a different colored block is adjacent
to the original block, the adjacent block also expands vertically next to the
original block, maintaining their relative positions.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous blocks of non-zero pixels in the grid.
    Returns a dictionary of objects, keyed by color, with their bounding box coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, coords):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        coords.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, color, coords)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                coords = []
                dfs(r, c, grid[r, c], coords)
                if grid[r,c] not in objects:
                    objects[grid[r,c]] = []

                objects[grid[r,c]].append(coords)
    return objects

def get_adjacent_block(grid, object_coords):
    """
    Finds an adjacent block of a different color, if any.  Prioritizes
    horizontal adjacency (left or right).

    Returns:
        A tuple (adjacent_color, adjacent_coords_list) or (None, None) if no adjacent block is found.
    """
    rows, cols = grid.shape
    main_color = grid[object_coords[0][0], object_coords[0][1]]
    adjacent_blocks = {}

    # Check for horizontal adjacency first, building a dictionary of adjacent blocks
    for r, c in object_coords:
        for dr, dc in [(0, 1), (0, -1)]:  # Check right and left
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != 0 and grid[nr, nc] != main_color:
                neighbor_color = grid[nr, nc]
                if neighbor_color not in adjacent_blocks:
                    adjacent_blocks[neighbor_color] = []
                if (nr, nc) not in adjacent_blocks[neighbor_color]:
                    adjacent_blocks[neighbor_color].append((nr, nc))


    # Now, find *all* coordinates that comprises the adjacent block by performing
    # another DFS for each of the adjacent colors found

    adjacent_coords_by_color = {}
    for color in adjacent_blocks:
            visited_adj = set()
            adjacent_coords_list = []

            def dfs_adjacent(r, c, adj_color):
                if (r,c) in visited_adj:
                    return
                if not (0 <= r < rows and 0 <= c < cols) or grid[r,c] != adj_color:
                    return
                
                visited_adj.add((r,c))
                adjacent_coords_list.append((r,c))

                for dr, dc, in [(0,1), (1,0), (0, -1), (-1, 0)]:
                    dfs_adjacent(r+dr, c+dc, adj_color)
            

            # start the DFS from each coordinate of this adjacent color
            for r,c in adjacent_blocks[color]:
                 dfs_adjacent(r,c, color)

            adjacent_coords_by_color[color] = adjacent_coords_list



    if adjacent_coords_by_color:  #return the coordinates of the first adjacent object
        first_key = list(adjacent_coords_by_color.keys())[0]
        return first_key, adjacent_coords_by_color[first_key]
    else:
        return None, None

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)
    objects = get_objects(input_grid)


    # iterate through all objects
    for color, object_coords_list in objects.items():
      for object_coords in object_coords_list:
        # Number of copies of pixels
        object_count = len(object_coords)

        # get minimum row, col for object - used for positioning copied pixels
        min_row = min(r for r, _ in object_coords)
        min_col = min(c for _, c in object_coords)
        
        # iterate through all coordinates of object
        for i in range(len(object_coords)):
            # get coordinates of object
            rx,ry = object_coords[i]

            # change output pixels
            for j in range(object_count):
                if rx + j < rows: # prevent out of bounds
                  output_grid[rx+j][ry]=color

        # Check for an adjacent block
        adjacent_color, adjacent_coords = get_adjacent_block(input_grid, object_coords)
        if adjacent_color is not None:
              adjacent_count = len(adjacent_coords)
              
              #get minimum row and col for adjacent object
              adj_min_row = min( r for r, _ in adjacent_coords)
              adj_min_col = min( c for _, c in adjacent_coords)


              for i in range(len(object_coords)):
                  rx, ry = object_coords[i]
                  
                  #find relative position of adjacent to main object
                  rel_col = adj_min_col - ry # should always be -1 or 1
                  
                  for j in range(adjacent_count):
                    #place relative to main object
                    if rx + j < rows and ry + rel_col < cols and ry+rel_col >=0:  # prevent out of bounds access
                        output_grid[rx+j][ry + rel_col] = adjacent_color
    return output_grid
```
