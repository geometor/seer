"""
1.  **Identify Horizontal Lines:** Find all horizontal lines in the input grid. A horizontal line is a sequence of two or more adjacent pixels of the same color.
2.  **Identify Singletons:** Find all singleton pixels. A singleton is a pixel that is not horizontally or vertically adjacent to another pixel of the same color.
3. **Process Singletons by Color:**
   - Find horizontal lines that match the color of the singleton.
   - Extend any matching horizontal lines to the column of the singleton, adding pixels of that color.
   - Remove the singleton pixels from the grid.
4.  **Output:** The modified grid, where singletons have either been removed or have extended existing same-colored horizontal lines.
"""

import numpy as np

def find_horizontal_lines(grid):
    lines = {}
    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != 0:
                if x == 0 or grid[y, x-1] != pixel:
                    # Start of a potential line
                    line_length = 0
                    for x2 in range(x, grid.shape[1]):
                        if grid[y, x2] == pixel:
                            line_length += 1
                        else:
                            break
                    if line_length > 1: # Consider it a line only if longer than 1 pixel
                        if pixel not in lines:
                            lines[pixel] = []
                        lines[pixel].append((y, x, line_length))
    return lines

def find_singletons(grid):
    singletons = []
    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != 0:
                # Check if it's a singleton
                is_singleton = True
                if x > 0 and grid[y, x-1] == pixel:
                    is_singleton = False
                if x < grid.shape[1] - 1 and grid[y, x+1] == pixel:
                    is_singleton = False
                if y > 0 and grid[y-1, x] == pixel:
                    is_singleton = False
                if y < grid.shape[0] - 1 and grid[y+1, x] == pixel:
                    is_singleton = False
                if is_singleton:
                    singletons.append((y, x, pixel))
    return singletons

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find horizontal lines
    lines = find_horizontal_lines(input_grid)

    # Find singletons
    singletons = find_singletons(input_grid)

    # Process singletons
    for y_s, x_s, color_s in singletons:
        # Find matching horizontal lines
        if color_s in lines:
            for y_l, x_l, length_l in lines[color_s]:
                # Check if the singleton is on the same row as the line
                if y_s == y_l:
                    # Extend line to the left
                    if x_s < x_l:
                        for x in range(x_s,x_l):
                            output_grid[y_s,x] = color_s
                    # Extend line to the right
                    elif x_s > x_l + length_l -1:
                        for x in range(x_l + length_l, x_s + 1):
                            output_grid[y_s, x] = color_s

        output_grid[y_s, x_s] = 0 # remove singleton after extending line

    return output_grid