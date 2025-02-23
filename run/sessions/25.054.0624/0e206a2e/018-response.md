# 0e206a2e • 018 • refine_coder

---
```python
"""
1.  **Identify Green Pixels:** Note the locations of all green (3) pixels. These pixels will remain unchanged in the output.
2.  **Identify Movable Groups:** Find separated groups of blue (1) and red (2) pixels.  If blue/red are surrounded by azure, they move as a unit.
3. **Identify Yellow Pixels**: Find yellow (4) pixels. Delete them.
4. **Determine Group Movement:** Each separated group of blue and red will be treated as a unit and moved. The vector of movement is not yet clear - more examples are needed.
5.  **Reconstruct:** Create an output grid by keeping everything from the input grid except the yellow, and placing moving groups into the correct position in the output grid.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color)

def find_adjacent_pixels(grid, pixels):
    """finds adjacent pixels of a given color"""
    adjacent_pixels = set()
    for r, c in pixels:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                    adjacent_pixels.add((nr, nc))
    return adjacent_pixels

def find_connected_components(grid, colors):
    """Finds connected components of specified colors."""
    visited = set()
    components = []

    def dfs(r, c, component):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] not in colors:
            return
        visited.add((r, c))
        component.append((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                dfs(r + dr, c + dc, component)


    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if (r, c) not in visited and grid[r, c] in colors:
                component = []
                dfs(r, c, component)
                components.append(component)
    return components

def calculate_centroid(pixels):
    """Calculates the centroid of a set of pixels."""
    if len(pixels) == 0:
        return np.array([0, 0])
    return np.mean(pixels, axis=0)

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify and remove yellow pixels
    yellow_pixels = find_pixels_by_color(input_grid, 4)
    for r, c in yellow_pixels:
        output_grid[r, c] = 0

    # Find green pixels (they remain static).
    # green_pixels = find_pixels_by_color(input_grid, 3)

    # Find connected components of blue and red pixels.
    blue_red_groups = find_connected_components(input_grid, [1, 2, 8])

    # Determine Movement and place
    for group in blue_red_groups:
      #detect azure
      has_azure = False
      for r,c in group:
         if input_grid[r,c] == 8:
            has_azure = True
            break;

      if has_azure: # move as a group, use relative shift
        # Find azure pixels.
        azure_pixels = []
        other_pixels = []
        for r, c in group:
            if input_grid[r,c] == 8:
                azure_pixels.append((r,c))
            if input_grid[r,c] == 1 or input_grid[r,c] == 2:
                other_pixels.append((r,c))

        # Find blue and red pixels NOT in azure
        blue_red_not_azure = []
        for r in range(input_grid.shape[0]):
          for c in range(input_grid.shape[1]):
             if input_grid[r,c] == 1 or input_grid[r,c] == 2:
                is_found = False
                for gr, gc in group:
                  if r == gr and c == gc:
                    is_found = True
                    break
                if is_found == False:
                   blue_red_not_azure.append( (r,c) )


        azure_centroid = calculate_centroid(np.array(azure_pixels))

        blue_red_avg_pos = calculate_centroid(np.array(blue_red_not_azure))

        if len(azure_pixels)>0 and len(blue_red_not_azure) >0:
            relative_shift = blue_red_avg_pos - azure_centroid
        else:
            relative_shift = np.array([0,0]) #no shift


        #remove old, place new at shifted pos
        for r, c in group:
          output_grid[r,c] = 0
          new_r = int(round(r + relative_shift[0]))
          new_c = int(round(c + relative_shift[1]))

          if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
            output_grid[new_r, new_c] = input_grid[r,c]
      else:
         #move each blue/red
         for r, c in group:
          if input_grid[r,c] == 1:
             output_grid[r,c] = 0
             new_r = r + 1
             new_c = c+1
             if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
                output_grid[new_r, new_c] = 1
          elif input_grid[r,c] == 2:
             output_grid[r,c] = 0
             new_r = r - 1
             new_c = c-1
             if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
                output_grid[new_r, new_c] = 2


    return output_grid
```
