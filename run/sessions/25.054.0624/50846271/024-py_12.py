"""
1.  **Identify Red Crosses:** Find "complete" red crosses. A complete cross is defined as a central red pixel with four immediately adjacent red pixels (up, down, left, and right).
2.  **Prioritize Complete Crosses:** Only consider complete crosses initially. Do not consider partial crosses for azure placement.
3.  **Analyze Cross Neighborhood:** For each *complete* red cross identified:
    *   Examine the eight neighboring positions (including diagonals) around the *central* red pixel of the cross.
4.  **Conditional Azure Placement (Restricted):**
    *   If a neighboring position is empty (0), and placing an azure (8) pixel there would connect the central red pixel to *another* complete red cross's center, place an azure pixel.
    *   Do *not* place azure if it only extends the arms of the current cross; it must bridge *between* complete crosses.
5. **Copy all other pixels:** All pixels from the input that are not part of the modification defined above are directly copied to the output.

"""

import numpy as np

def find_complete_crosses(grid):
    """Finds complete red crosses (central pixel with 4 neighbors)."""
    red_pixels = np.argwhere(grid == 2)
    complete_crosses = []

    for r, c in red_pixels:
        neighbors = 0
        if r > 0 and grid[r-1, c] == 2:  # Above
            neighbors += 1
        if r < grid.shape[0] - 1 and grid[r+1, c] == 2:  # Below
            neighbors += 1
        if c > 0 and grid[r, c-1] == 2:  # Left
            neighbors += 1
        if c < grid.shape[1] - 1 and grid[r, c+1] == 2:  # Right
            neighbors += 1

        if neighbors == 4:
            complete_crosses.append((r, c))
    return complete_crosses

def get_neighbors(grid, r, c):
    """Gets the 8 neighbors (including diagonals) of a pixel."""
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr, nc = r + i, c + j
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                neighbors.append((nr, nc))
    return neighbors

def should_place_azure_restricted(grid, r, c, complete_crosses):
    """Checks if placing an azure pixel bridges between complete crosses."""
    if grid[r, c] != 0:
        return False

    cross_connections = 0
    for nr, nc in get_neighbors(grid, r, c):
      if (nr, nc) in complete_crosses:
        cross_connections +=1
    
    return cross_connections >= 1

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find complete red crosses
    complete_crosses = find_complete_crosses(input_grid)

    # Analyze neighborhood and place azure pixels (restricted)
    for r, c in complete_crosses:
        for nr, nc in get_neighbors(input_grid, r, c):
            if should_place_azure_restricted(input_grid, nr, nc, complete_crosses):
                output_grid[nr, nc] = 8

    return output_grid