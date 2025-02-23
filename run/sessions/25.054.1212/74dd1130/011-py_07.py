# Example 1:
input_grid = [[2, 1, 1], [1, 5, 1], [5, 2, 2]]
expected_output = [[2, 1, 5], [2, 5, 2], [1, 1, 2]]

# 1. Check _sort_rows (should be unnecessary)
print(f"Sorted Rows: {_sort_rows(input_grid)}") # will be incorrect

# 2. Check _transpose
print(f"Transposed Grid: {_transpose(input_grid)}")

# 3. Check the mapping process (this is where the core error is):
transposed_grid = _transpose(input_grid)
sorted_rows = _sort_rows(input_grid) #Incorrect application
output_grid = np.zeros_like(transposed_grid)
for i in range(len(transposed_grid)):
    for j in range(len(transposed_grid[0])):
        print(f"Transposed[{i}][{j}] = {transposed_grid[i][j]}, SortedRows[{i}][{j}] = {sorted_rows[i][j] if j < len(sorted_rows[i]) else 'N/A'}")
        if j < len(sorted_rows[i]): # avoid out of index error
            output_grid[i][j] = sorted_rows[i][j]

print(f"Output Grid (Incorrect): {output_grid.tolist()}")