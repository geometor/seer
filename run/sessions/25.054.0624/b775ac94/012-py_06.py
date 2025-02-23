"""
Expands colored blocks vertically based on their height. If a different colored
block is horizontally adjacent to the original block, the adjacent block also
expands vertically next to the original block, maintaining their relative
positions. The expansion amount of any object is based on its own height.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous blocks of non-zero pixels in the grid.
    Returns a dictionary of objects, keyed by color, with a list of their coordinates.
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

def get_object_height(object_coords):
    """Calculates the height of an object given its coordinates."""
    rows = [r for r, _ in object_coords]
    return max(rows) - min(rows) + 1

def get_horizontally_adjacent_block(grid, object_coords):
    """
    Finds a horizontally adjacent block of a different color.

    Returns:
        A tuple (adjacent_color, adjacent_coords_list) or (None, None) if no adjacent block is found.
    """
    rows, cols = grid.shape
    main_color = grid[object_coords[0][0], object_coords[0][1]]
    adjacent_blocks = {}

    # Check for horizontal adjacency only
    for r, c in object_coords:
        for dr, dc in [(0, 1), (0, -1)]:  # Check right and left
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != 0 and grid[nr, nc] != main_color:
                neighbor_color = grid[nr, nc]
                if neighbor_color not in adjacent_blocks:
                    adjacent_blocks[neighbor_color] = []
                if (nr, nc) not in adjacent_blocks[neighbor_color]:
                    adjacent_blocks[neighbor_color].append((nr, nc))


    # DFS to get all coords of horizontally adjacent objects
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

                for dr, dc, in [(0,1), (1,0), (0, -1), (-1, 0)]:  # Include vertical neighbors in DFS
                    dfs_adjacent(r+dr, c+dc, adj_color)
            

            # start the DFS from each coordinate of this adjacent color
            for r,c in adjacent_blocks[color]:
                 dfs_adjacent(r,c, color)

            adjacent_coords_by_color[color] = adjacent_coords_list

    if adjacent_coords_by_color:
        first_key = list(adjacent_coords_by_color.keys())[0]
        return first_key, adjacent_coords_by_color[first_key] # Return the first horizontally adjacent object.
    else:
        return None, None

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)
    objects = get_objects(input_grid)

    for color, object_coords_list in objects.items():
        for object_coords in object_coords_list:
            object_height = get_object_height(object_coords)
            min_row = min(r for r, _ in object_coords)
            min_col = min(c for _, c in object_coords)

            # Vertical expansion of the main object
            for r, c in object_coords:
                for i in range(object_height):
                    if r + i < rows:
                        output_grid[r + i, c] = color

            # Check for horizontally adjacent blocks
            adjacent_color, adjacent_coords = get_horizontally_adjacent_block(input_grid, object_coords)
            if adjacent_color:
                adjacent_height = get_object_height(adjacent_coords)
                adj_min_row = min( r for r,_ in adjacent_coords)
                adj_min_col = min(c for _,c in adjacent_coords)

                # Vertical expansion of adjacent object
                
                #find relative position of adjacent to main
                rel_col = adj_min_col - min_col #should always be -1 or 1

                for r,c in object_coords:
                    for i in range(adjacent_height):
                        if r + i < rows and c + rel_col < cols and c + rel_col >= 0:
                            output_grid[r + i][c + rel_col] = adjacent_color

    return output_grid