"""
For each row in the input grid, perform the following steps:

1. **Locate the First '8':** Identify the index of the first occurrence of the number 8 in the current row, scanning from left to right.
2. **Modify Right Cell (if applicable):** If an '8' is found, examine the cell immediately to its right within the same row. If this cell exists within the row boundaries and its value is 0, change its value to 1 in the output grid.
3. **Locate the Last '8':** Identify the index of the last occurrence of the number 8 in the same row, scanning from right to left.
4. **Modify Left Cell (if applicable):** If an '8' is found, examine the cell immediately to its left within the same row. If this cell exists within the row boundaries and its value is 0, change its value to 1 in the output grid.
5. **Unchanged Rows:** If no '8' is found in the current row, leave the entire row unchanged in the output grid.

Repeat these steps for every row in the input grid to generate the complete output grid.
"""

input_grid = [
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

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = [row[:] for row in input_grid]

    # Iterate through each row of the input grid
    for row_index in range(len(input_grid)):
        row = input_grid[row_index]

        # 1. Locate the First '8'
        try:
            first_eight_index = row.index(8)
            # 2. Modify Right Cell (if applicable)
            if first_eight_index + 1 < len(row) and row[first_eight_index + 1] == 0:
                output_grid[row_index][first_eight_index + 1] = 1
        except ValueError:
            # '8' is not found in this row, continue to the next row
            pass

        # 3. Locate the Last '8'
        last_eight_index = -1
        for i in range(len(row) - 1, -1, -1): # Iterate from right to left to find the last '8'
            if row[i] == 8:
                last_eight_index = i
                break # Stop after finding the last '8'

        # 4. Modify Left Cell (if applicable)
        if last_eight_index != -1:
            if last_eight_index - 1 >= 0 and row[last_eight_index - 1] == 0:
                output_grid[row_index][last_eight_index - 1] = 1

    return output_grid


if __name__ == '__main__':

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."