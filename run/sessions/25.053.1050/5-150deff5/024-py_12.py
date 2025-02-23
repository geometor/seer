"""
1.  **Identify Background:** Locate the white (0) background pixels. These pixels' positions and colors remain unchanged in the output.

2.  **Identify Gray Object:** Find the contiguous gray (5) object in the input grid.

3.  **Segment Gray Object:** Divide the gray object into *contiguous* vertical segments.  A segment consists of gray pixels that are adjacent vertically *or* horizontally. A single-pixel white gap does not separate connected blocks.

4.  **Alternate Colors:**
    *   Assign red (2) to the leftmost segment.
    *   Assign azure (8) to the next segment to the right.
    *   Continue alternating between red and azure for subsequent segments.

5.  **Output:** Create the output grid by replacing the gray pixels of the original object with the colored segments, maintaining the position of the white background.
"""

import numpy as np

def get_vertical_segments(grid, color):
    """
    Identifies contiguous vertical segments of a specified color.
    Adjacency is both vertical and horizontal.
    """
    rows, cols = grid.shape
    segments = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_segment):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_segment.append((r, c))
        # Explore vertically and horizontally
        dfs(r + 1, c, current_segment)
        dfs(r - 1, c, current_segment)
        dfs(r, c + 1, current_segment)
        dfs(r, c - 1, current_segment)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_segment = []
                dfs(r, c, current_segment)
                if current_segment:
                    segments.append(current_segment)

    return segments

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # get the gray object segments
    gray_segments = get_vertical_segments(input_grid, 5)

    # if no gray object exists, return a copy of the original
    if not gray_segments:
      return output_grid
    
    # set all the gray pixels to white first
    for segment in gray_segments:
        for r, c in segment:
            output_grid[r,c] = 0

    # alternate coloring of segments
    color_index = 0
    colors = [2, 8]  # Red and Azure

    # Sort segments by leftmost column
    gray_segments.sort(key=lambda segment: min(c for r, c in segment))

    for segment in gray_segments:
        current_color = colors[color_index % 2]
        for r, c in segment:
            output_grid[r, c] = current_color
        color_index += 1

    return output_grid