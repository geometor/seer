"""
1.  **Identify Objects:** Find all non-white pixels in the input grid.
2.  **Pairwise Check:** Iterate through all unique pairs of these non-white pixels.
3.  **Distance Condition:** For each pair, calculate the Manhattan distance. If the distance is exactly 3:
    *   **Yellow Pixel Placement:**
        *   If the pair is horizontally aligned, place one yellow pixel one cell to the left of the leftmost pixel and one yellow pixel one cell to the right of the rightmost pixel.
        *   If the pair is vertically aligned, place one yellow pixel one cell above the topmost pixel and one yellow pixel one cell below the bottommost pixel.
        *   If the pair is diagonally aligned, place yellow pixel one cell diagonally adjacent to *both* pixels, maintaining relative positions.
    *   **Orange Filling:** Create a 3x3 square of orange pixels centered on the *two original pixels*. Ensure this filling occurs for every pair that meets the distance condition, regardless of their relative orientation (horizontal, vertical, or diagonal). The 3x3 fill region should always include both original pixels.
4.  **Preservation:** Copy any non-white pixels from the input grid that were *not* part of any pair with a Manhattan distance of 3 directly to the output grid at their original locations.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of non-white pixels."""
    rows, cols = np.where(grid != 0)
    return list(zip(rows, cols))

def manhattan_distance(p1, p2):
    """Calculates Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    non_white_pixels = get_non_white_pixels(input_grid)

    # iterate pairs of non-white pixels
    processed_pixels = set()
    for i in range(len(non_white_pixels)):
      for j in range(i + 1, len(non_white_pixels)):
        p1 = non_white_pixels[i]
        p2 = non_white_pixels[j]

        if manhattan_distance(p1,p2) == 3:
            #Yellow Pixel Placement.
            
            #horizontal
            if (p1[0] == p2[0]):
              output_grid[p1[0], min(p1[1],p2[1])-1] = 4
              output_grid[p1[0], max(p1[1],p2[1])+1] = 4
            #vertical
            if (p1[1] == p2[1]):
              output_grid[min(p1[0],p2[0])-1, p1[1]] = 4
              output_grid[max(p1[0],p2[0])+1, p1[1]] = 4

            # diagonal
            row_diff = p2[0] - p1[0]
            col_diff = p2[1] - p1[1]

            if abs(row_diff) + abs(col_diff) == 3 and row_diff !=0 and col_diff != 0: #confirm the diagonal
                output_grid[p1[0] + (1 if row_diff > 0 else -1), p1[1] + (1 if col_diff > 0 else -1)] = 4
                output_grid[p2[0] + (-1 if row_diff > 0 else 1), p2[1] + (-1 if col_diff > 0 else 1)] = 4

            
            # fill a 3x3 box with orange around the two pixels
            min_row = min(p1[0], p2[0])
            max_row = max(p1[0], p2[0])
            min_col = min(p1[1], p2[1])
            max_col = max(p1[1], p2[1])

            for row in range(min_row -1, max_row + 2):
              for col in range(min_col - 1, max_col + 2):
                if 0 <= row < output_grid.shape[0] and 0<= col < output_grid.shape[1]:
                    output_grid[row,col] = 7
            
            processed_pixels.add(p1)
            processed_pixels.add(p2)


    # preservation of other non-white pixels
    for p in non_white_pixels:
        if p not in processed_pixels:
            output_grid[p] = input_grid[p]
            

    return output_grid