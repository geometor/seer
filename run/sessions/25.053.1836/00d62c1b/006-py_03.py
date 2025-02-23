"""
1.  **Identify Connected Components:** Iterate through each pixel of the input grid. For each green (3) pixel, find its connected component. A connected component is a group of green pixels where each pixel is directly adjacent (shares a side, not just a corner) to at least one other green pixel in the component.
2.  **Determine Size:** Calculate the size (number of pixels) of each connected component.
3.  **Conditional Color Change:** If the size of a connected component is greater than 2, change all pixels within that component from green (3) to yellow (4). If a connected component's size is 1 or 2, the pixels remain green.
4.  All non-green pixels are unchanged.
5. The final result is output.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid according to the specified rule.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0])

    def get_connected_component(r, c, visited):
        """
        Performs a Depth-First Search (DFS) to find all pixels in a connected component.
        """
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                input_grid[r][c] != 3 or (r, c) in visited):
            return []

        visited.add((r, c))
        component = [(r, c)]

        # Cardinal directions (up, down, left, right)
        component.extend(get_connected_component(r + 1, c, visited))
        component.extend(get_connected_component(r - 1, c, visited))
        component.extend(get_connected_component(r, c + 1, visited))
        component.extend(get_connected_component(r, c - 1, visited))

        return component

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is green
            if input_grid[r][c] == 3:
                visited = set()
                connected_component = get_connected_component(r, c, visited)
                #change connected components greater than 2 to yellow
                if len(connected_component) > 2:
                    for row, col in connected_component:
                        output_grid[row][col] = 4
    return output_grid