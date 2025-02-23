"""
The task is to identify and modify cells within connected regions of color 8 (azure).
1. Identify Connected Regions: Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. Order the Regions:  For each connected region, find its "top-leftmost" cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions based on their top-leftmost cells, first by row index and then by column index in ascending order. Let's call the regions Region 1 and Region 2 based on this order.
3. Modify Region 1: In Region 1, locate its top-leftmost cell and change its color to 1 (blue).
4. Modify Region 2: In Region 2, locate its bottom-rightmost cell. The bottom-rightmost cell is defined as the cell with the largest row index, and among those with the same largest row index, the largest column index. Change the color of this bottom-rightmost cell to 1 (blue).
"""

import copy

def find_connected_regions(grid, color):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def get_neighbors(r, c):
        return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

    def dfs(r, c, current_region):
        visited[r][c] = True
        current_region.append((r, c))
        for nr, nc in get_neighbors(r, c):
            if is_valid(nr, nc) and grid[nr][nc] == color and not visited[nr][nc]:
                dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and not visited[r][c]:
                current_region = []
                dfs(r, c, current_region)
                regions.append(current_region)
    return regions

def get_top_leftmost_cell(region):
    top_leftmost_cell = region[0]
    for r, c in region:
        if r < top_leftmost_cell[0] or (r == top_leftmost_cell[0] and c < top_leftmost_cell[1]):
            top_leftmost_cell = (r, c)
    return top_leftmost_cell

def get_bottom_rightmost_cell(region):
    bottom_rightmost_cell = region[0]
    for r, c in region:
        if r > bottom_rightmost_cell[0] or (r == bottom_rightmost_cell[0] and c > bottom_rightmost_cell[1]):
            bottom_rightmost_cell = (r, c)
    return bottom_rightmost_cell

def transform(input_grid):
    output_grid = copy.deepcopy(input_grid)
    regions = find_connected_regions(input_grid, 8)

    if not regions:
        return output_grid

    regions.sort(key=lambda region: get_top_leftmost_cell(region))

    if len(regions) >= 1:
        region1 = regions[0]
        tl_r1, tl_c1 = get_top_leftmost_cell(region1)
        output_grid[tl_r1][tl_c1] = 1

    if len(regions) >= 2:
        region2 = regions[1]
        br_r2, br_c2 = get_bottom_rightmost_cell(region2)
        output_grid[br_r2][br_c2] = 1

    return output_grid


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."