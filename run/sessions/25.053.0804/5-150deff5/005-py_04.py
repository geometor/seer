import numpy as np

input_grid = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 5, 5, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])

output_grid = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 2, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 8, 8, 0, 0, 0],
    [0, 0, 0, 2, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])

def get_object_coordinates(grid, color):
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

input_gray_coords = get_object_coordinates(input_grid, 5)
output_azure_coords = get_object_coordinates(output_grid, 8)
output_red_coords = get_object_coordinates(output_grid, 2)

print(f'{input_gray_coords=}')
print(f'{output_azure_coords=}')
print(f'{output_red_coords=}')
