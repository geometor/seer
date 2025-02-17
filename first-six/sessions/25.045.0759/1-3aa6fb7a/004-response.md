# 25.045.0759 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
Identify all contiguous vertical blocks of azure color (8). Order these blocks from left to right based on their column index. For the leftmost block, locate the topmost cell of color azure. Change the color of the cell immediately to its right to blue (1). For the next blocks (if any), locate the bottommost cell of color azure. Change the color of the cell at the same position to blue (1).
"""

import collections

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = [row[:] for row in input_grid] # Create a copy to avoid modifying input

    vertical_blocks = collections.defaultdict(list)
    for j in range(cols):
        start_row = -1
        for i in range(rows):
            if input_grid[i][j] == 8:
                if start_row == -1:
                    start_row = i
            else:
                if start_row != -1:
                    vertical_blocks[j].extend(range(start_row, i))
                    start_row = -1
        if start_row != -1:
            vertical_blocks[j].extend(range(start_row, rows))

    ordered_blocks_cols = sorted(vertical_blocks.keys())
    blocks_info = []
    for col_index in ordered_blocks_cols:
        blocks_info.append((col_index, sorted(list(set(vertical_blocks[col_index]))))) # remove duplicates and sort rows

    if not blocks_info:
        return output_grid

    # Process the first block (leftmost)
    first_block_col, first_block_rows = blocks_info[0]
    topmost_row = first_block_rows[0]
    if first_block_col + 1 < cols:
        output_grid[topmost_row][first_block_col + 1] = 1

    if len(blocks_info) > 1:
        # Process the subsequent blocks
        for block_index in range(1, len(blocks_info)):
            block_col, block_rows = blocks_info[block_index]
            bottommost_row = block_rows[-1]
            output_grid[bottommost_row][block_col] = 1

    return output_grid


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 1, 8, 0, 0]
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
