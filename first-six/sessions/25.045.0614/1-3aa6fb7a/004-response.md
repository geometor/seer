# 25.045.0614 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
1. Identify Color Objects: Detect all distinct, connected regions of color 8 (azure) within the input grid.
2. Determine Top-Right Corner for Each Object: For every object identified in step 1, locate the cell that is simultaneously in the topmost row and the rightmost column among all cells belonging to that object.
3. Recolor Top-Right Cell: Change the color of the "top-right" cell identified in step 2 from its original color 8 (azure) to color 1 (blue).
4. Preserve Other Cells:  Ensure that all cells in the grid that are not identified as "top-right" cells of color 8 objects remain unchanged.
"""

import copy

def transform(input_grid):
    """
    Transforms the input grid by identifying contiguous blocks of color 8 and
    changing the color of the top-right cell of each block to color 1.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists of integers.

    Returns:
        list of lists: The transformed output grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
        return neighbors

    def find_block(r, c):
        block_cells = []
        queue = [(r, c)]
        visited[r][c] = True
        block_cells.append((r, c))

        while queue:
            row, col = queue.pop(0)
            for nr, nc in get_neighbors(row, col):
                if input_grid[nr][nc] == 8 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    block_cells.append((nr, nc))
        return block_cells

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8 and not visited[r][c]:
                block = find_block(r, c)
                if block:
                    top_row = float('inf')
                    right_col = float('-inf')
                    top_right_cell = None
                    for cell_r, cell_c in block:
                        if cell_r < top_row:
                            top_row = cell_r
                            right_col = cell_c
                            top_right_cell = (cell_r, cell_c)
                        elif cell_r == top_row and cell_c > right_col:
                            right_col = cell_c
                            top_right_cell = (cell_r, cell_c)
                    if top_right_cell:
                        tr_r, tr_c = top_right_cell
                        output_grid[tr_r][tr_c] = 1

    return output_grid


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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
```
