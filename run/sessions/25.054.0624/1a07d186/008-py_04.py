"""
1.  **Identify Key Lines:** Find the two horizontal lines composed of contiguous pixels of the same color: one red (color 2) and one blue (color 1).
2.  **Preserve Lines:** Keep the red and blue horizontal lines intact.
3. **Drop Singletons:** Identify any objects that are a single pixel of one color.
4.  **Move Blue and Red Singletons**:
    *   If the object singleton is the color blue (1), move the objects to the empty row immediately above the solid blue line.
    *   If the object singleton is the color red (2), move the objects to the empty row immediately above the solid red line.
5.  **Remove Yellow:** Delete any single-pixel yellow (4) object.
6.  **Output:** Generate the output grid with the remaining colored object locations after deletions and translations.
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
    for y, x, color in singletons:
        if color == 4:  # Remove yellow singletons
            output_grid[y, x] = 0
        elif color == 1:  # Move blue singletons
            if 1 in lines:
              target_row = min([line[0] for line in lines[1]]) -1 #Find the blue row
              if (target_row >=0):
                 # find an empty space
                 for line_x in range(0, output_grid.shape[1]):
                    if output_grid[target_row, line_x] == 0:
                       output_grid[y,x] = 0
                       output_grid[target_row, line_x] = 1
                       break

        elif color == 2: #move red singletons
            if 2 in lines:
               target_row = min([line[0] for line in lines[2]]) - 1 #Find the first red row
               if (target_row >= 0):
                  for line_x in range(0, output_grid.shape[1]):
                     if output_grid[target_row, line_x] == 0:
                        output_grid[y,x] = 0
                        output_grid[target_row, line_x] = 2
                        break


    return output_grid