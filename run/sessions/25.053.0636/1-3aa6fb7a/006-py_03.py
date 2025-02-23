"""
1.  **Identify Azure Lines:** Locate all contiguous lines of azure pixels. A line is defined as a sequence of adjacent azure pixels forming either a horizontal or vertical straight line.
2.  **Classify Line Orientation**: For each azure line, determine if it is horizontal (pixels in the same row) or vertical (pixels in the same column)
3.  **Insert Blue Pixel:**
    *   **Horizontal Line:** Find the bottom-most pixel in the line. Insert a blue pixel immediately *below* this pixel.
    *    **Vertical Line:** Find the left-most pixel. Insert a blue pixel to the *right* of this pixel.
    *   Ensure that insertions are always within grid boundaries. If an insertion would be out of bounds, it is skipped.
"""

import numpy as np

def find_lines(grid, color):
    lines = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_line):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_line.append((r, c))

        # Explore adjacent cells
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_line)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_line = []
                dfs(r, c, current_line)
                if current_line:
                    lines.append(current_line)
    return lines

def classify_line(line):
    # Determine if a line is horizontal or vertical
    if len(line) > 1:
        if line[0][0] == line[1][0]:
            return "horizontal"  # Same row, different columns
        else:
            return "vertical"  # Different rows, same column
    else:
        return "single" # single pixel line

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    lines = find_lines(input_grid, 8) # Find all azure lines

    for line in lines:
        line_type = classify_line(line)

        if line_type == "horizontal":
            # Find the bottom-most pixel (they are all at the same row)
            # arbitrarily pick the first - check if x is the same and use y
            bottom_most = line[0]
            #Insert below
            insert_point = (bottom_most[0] + 1, bottom_most[1])

            if 0 <= insert_point[0] < output_grid.shape[0] and 0 <= insert_point[1] < output_grid.shape[1]:
                output_grid[insert_point] = 1

        elif line_type == "vertical":
            # Find the left-most pixel
            left_most = min(line, key=lambda p: p[1])
            #Insert to the right
            insert_point = (left_most[0], left_most[1] + 1)
            if 0 <= insert_point[0] < output_grid.shape[0] and 0 <= insert_point[1] < output_grid.shape[1]:
                output_grid[insert_point] = 1
        # else: single pixel lines can be ignored - no insertion

    return output_grid