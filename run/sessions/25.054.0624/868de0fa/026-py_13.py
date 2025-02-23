"""
1.  **Identify Rectangles:** Locate all rectangular shapes within the input grid. Rectangles are defined by a continuous blue (1) outline, one pixel thick, enclosing an area of white (0) pixels.
2.  **Determine Position:** Classify the identified rectangles based on their vertical position within the grid. Rectangles in the top half are considered "top," while those in the bottom half are considered "bottom."
3. **Fill Top Rectangle:** For any rectangle in the "top" half, change all pixels within its blue outline to orange (7).
4.  **Fill Bottom Rectangle:** For any rectangle in the "bottom" half, change all the pixels within its blue outline to red (2).
5. **Preserve outline**: Keep the outline blue (1)
6.  **Output:** Present the modified grid as the output.
"""

import numpy as np

def find_rectangles(grid):
    """Finds rectangular shapes with blue outline and white filling."""
    rectangles = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_rectangle):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] == 0:
            return

        visited.add((r, c))
        current_rectangle.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_rectangle)
    
    # Find the starting pixels and the enclosed
    for r in range(rows):
      for c in range(cols):
        if grid[r,c] == 1 and (r,c) not in visited:
          current_rectangle = []
          dfs(r,c,current_rectangle)
          # check if rectangle by checking if it has min/max
          if current_rectangle:
                min_r = min(x[0] for x in current_rectangle)
                max_r = max(x[0] for x in current_rectangle)
                min_c = min(x[1] for x in current_rectangle)
                max_c = max(x[1] for x in current_rectangle)
                
                # Check if all cells in bounding box are either 1 (outline) or 0(inside)
                valid_rect = True
                for i in range(min_r,max_r + 1):
                  for j in range(min_c, max_c + 1):
                    if (i,j) not in current_rectangle:
                        if grid[i,j] != 0:
                          valid_rect = False
                          break

                if valid_rect:
                      rectangles.append(current_rectangle)


    return rectangles

def get_rectangle_position(rectangle, grid_height):
    """Determines if a rectangle is in the top or bottom half."""
    avg_row = sum(r for r, _ in rectangle) / len(rectangle)
    return "top" if avg_row < grid_height / 2 else "bottom"

def fill_rectangle(grid, rectangle, color):
    """Fills the inside of a rectangle with the specified color."""
    min_r = min(r for r, _ in rectangle)
    max_r = max(r for r, _ in rectangle)
    min_c = min(c for _, c in rectangle)
    max_c = max(c for _, c in rectangle)

    for r in range(min_r + 1, max_r):
        for c in range(min_c + 1, max_c):
            grid[r, c] = color

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    # Find rectangles
    rectangles = find_rectangles(output_grid)

    # change output pixels 
    for rectangle in rectangles:
        position = get_rectangle_position(rectangle, rows)
        if position == "top":
            fill_rectangle(output_grid, rectangle, 7)  # Fill top with orange
        else:
            fill_rectangle(output_grid, rectangle, 2)  # Fill bottom with red

    return output_grid