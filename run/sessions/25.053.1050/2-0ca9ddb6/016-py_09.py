"""
1.  **Identify Objects:** Find the coordinates of all non-white pixels in the input grid.
2.  **Pairwise Comparison:** Iterate through all unique pairs of non-white pixels.
3.  **Distance Check:** Calculate the Manhattan distance between the two pixels in each pair.
4.  **Conditional Actions (If Distance is 3):**
    *   **Yellow Placement:**
        *   If the pixels are horizontally aligned: Place a yellow pixel one cell to the left of the leftmost pixel and one cell to the right of the rightmost pixel.
        *   If the pixels are vertically aligned: Place a yellow pixel one cell above the topmost pixel and one cell below the bottommost pixel.
        *   If the pixels are diagonally aligned: Place a yellow pixel diagonally adjacent to each of the paired pixels. Specifically, add yellow at p1 + sign(p2-p1) and at p2 - sign(p2-p1).
    *   **Orange Filling:** Create a 3x3 square of orange pixels centered on *each* of the two original pixels. If the resulting 3x3 regions around the two pixels overlap, the overlapping cells should all be orange.
5. **Preservation** Copy all pixels that were *not* part of a pair with Manhattan Distance of 3 to output, maintaining position and color.
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
                output_grid[p1[0] + np.sign(row_diff), p1[1] + np.sign(col_diff)] = 4
                output_grid[p2[0] - np.sign(row_diff), p2[1] - np.sign(col_diff)] = 4

            
            # Orange Filling: 3x3 around EACH pixel
            for p in [p1, p2]:
                for row in range(p[0] - 1, p[0] + 2):
                    for col in range(p[1] - 1, p[1] + 2):
                        if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:
                            output_grid[row, col] = 7
            
            processed_pixels.add(p1)
            processed_pixels.add(p2)


    # preservation of other non-white pixels
    for p in non_white_pixels:
        if p not in processed_pixels:
            output_grid[p] = input_grid[p]
            

    return output_grid