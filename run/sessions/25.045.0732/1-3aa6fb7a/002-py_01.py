"""
For each contiguous block of color 8 (azure) in the input grid:
1. Identify all cells belonging to the block.
2. Find the cell within this block that is located at the topmost row and then leftmost column (prioritizing rows, then columns in reading order). Let's call this the 'top-leftmost' cell of the block.
3. Calculate the sum of the row index and column index of this 'top-leftmost' cell.
4. If this sum is less than 5, then change the color of the cell immediately to the right of the 'top-leftmost' cell to color 1 (blue).
5. If this sum is greater than or equal to 5, then change the color of the cell immediately below the 'top-leftmost' cell to color 1 (blue).

This transformation is applied independently to each block of color 8 in the input grid. Cells that are not part of a color 8 block, or are adjacent to it but not selected by the transformation rule, remain unchanged.
"""

import numpy as np

def transform(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid_np = np.copy(input_grid_np)
    rows, cols = input_grid_np.shape
    visited = np.zeros_like(input_grid_np, dtype=bool)

    def get_block_cells(r, c):
        block_cells = []
        stack = [(r, c)]
        visited[r, c] = True
        while stack:
            row, col = stack.pop()
            block_cells.append((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and input_grid_np[nr, nc] == 8 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    stack.append((nr, nc))
        return block_cells

    for r in range(rows):
        for c in range(cols):
            if input_grid_np[r, c] == 8 and not visited[r, c]:
                block_cells = get_block_cells(r, c)
                top_leftmost_cell = min(block_cells, key=lambda cell: (cell[0], cell[1]))
                top_r, top_c = top_leftmost_cell
                index_sum = top_r + top_c

                if index_sum < 5:
                    if top_c + 1 < cols:
                        output_grid_np[top_r, top_c + 1] = 1
                else:
                    if top_r + 1 < rows:
                        output_grid_np[top_r + 1, top_c] = 1

    return output_grid_np.tolist()


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
