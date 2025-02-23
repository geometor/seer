import numpy as np

input_grid = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])

output_grid = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])

def find_pixel_coordinates(grid, color_code):
    coordinates = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel == color_code:
                coordinates.append((row_index, col_index))
    return coordinates

input_azure_pixels = find_pixel_coordinates(input_grid, 8)
output_azure_pixels = find_pixel_coordinates(output_grid, 8)
output_blue_pixels = find_pixel_coordinates(output_grid, 1)

print(f'{input_azure_pixels=}')
print(f'{output_azure_pixels=}')
print(f'{output_blue_pixels=}')