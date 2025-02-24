"""
1.  **Identify Red Pixels:** Locate all red pixels (value 2) in the input grid. These are the anchor points.
2. **Connect Red Pixels:** For *every pair* of red pixels:
     * Check for the *shortest* possible straight-line connection between them. A connection can be:
        *   **Horizontal:**  The two pixels are on the same row.
        *   **Vertical:** The two pixels are on the same column.
        * **Diagonal:** Two pixels are connected by a diagonal straight line (either up-left to down-right or up-right to down-left). The absolute difference between their row indices must equal the absolute difference between their column indices, i.e., `abs(r1 - r2) == abs(c1 - c2)`
    *  If a valid shortest connection exists, and all pixels on that line are either red (2) or white (0), change the color of all *white* pixels (0) on the line to yellow (4).

3.  **Output:** The output grid is the result of applying the connection and filling rules to all pairs of red pixels.
"""

import numpy as np

def get_red_pixels(grid):
    red_pixels = []
    for r_idx, row in enumerate(grid):
        for c_idx, pixel in enumerate(row):
            if pixel == 2:
                red_pixels.append((r_idx, c_idx))
    return red_pixels

def connect_and_fill(grid, p1, p2):
    """Connects two red pixels and fills the intermediate white pixels with yellow."""
    r1, c1 = p1
    r2, c2 = p2
    output_grid = np.copy(grid)

    # Horizontal connection
    if r1 == r2:
        c_min = min(c1, c2)
        c_max = max(c1, c2)
        line = grid[r1, c_min:c_max+1]
        if all(pixel == 2 or pixel == 0 for pixel in line):
            for c in range(c_min + 1, c_max):
                if output_grid[r1, c] == 0:
                    output_grid[r1, c] = 4
        return output_grid
    
    # Vertical connection
    if c1 == c2:
        r_min = min(r1, r2)
        r_max = max(r1, r2)
        line = grid[r_min:r_max+1, c1]
        if all(pixel == 2 or pixel == 0 for pixel in line):
            for r in range(r_min + 1, r_max):
                if output_grid[r, c1] == 0:
                    output_grid[r, c1] = 4
        return output_grid

    # Diagonal connection
    if abs(r1 - r2) == abs(c1 - c2):
        r_dir = 1 if r2 > r1 else -1
        c_dir = 1 if c2 > c1 else -1
        r, c = r1, c1
        line_pixels = []
        while r != r2 + r_dir and c != c2 + c_dir:
           line_pixels.append(grid[r,c])
           r += r_dir
           c += c_dir
        if all(pixel == 2 or pixel == 0 for pixel in line_pixels):
            r, c = r1 + r_dir, c1 + c_dir  # Start after the first pixel
            while r != r2 and c != c2:
                if output_grid[r, c] == 0:
                    output_grid[r, c] = 4
                r += r_dir
                c += c_dir
        return output_grid

    return output_grid # no connection
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # get all red pixels
    red_pixels = get_red_pixels(input_grid)

    # iterate through all pairs of red pixels
    for i in range(len(red_pixels)):
        for j in range(i + 1, len(red_pixels)):
            output_grid = connect_and_fill(output_grid, red_pixels[i], red_pixels[j])

    return output_grid