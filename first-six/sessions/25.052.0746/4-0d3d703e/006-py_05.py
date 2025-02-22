# Example 1
input_grid_1 = np.array([[3, 1, 2], [3, 1, 2], [3, 1, 2]])
color_map_1 = {3: 4, 1: 5, 2: 6}
output_grid_1 = transform(input_grid_1, color_map_1)
print(output_grid_1)

# Example 2
input_grid_2 = np.array([[2, 3, 8], [2, 3, 8], [2, 3, 8]])
color_map_2 = {2: 6, 3: 4, 8: 9}
output_grid_2 = transform(input_grid_2, color_map_2)
print(output_grid_2)