import numpy as np

input_grid = np.array([
    [0, 0, 1, 5, 0, 0, 0],
    [1, 1, 0, 5, 1, 0, 1],
    [0, 1, 1, 5, 1, 0, 1]
])

output_grid = np.array([
    [0, 0, 0],
    [2, 0, 0],
    [0, 0, 2]
])

print(f"Input grid dimensions: {input_grid.shape}")
print(f"Output grid dimensions: {output_grid.shape}")

def find_pixels(grid, color):
    return np.argwhere(grid == color)

print("Input Pixels:")
for color in np.unique(input_grid):
    print(f"  Color {color}: {find_pixels(input_grid, color)}")
    
print("Output Pixels:")
for color in np.unique(output_grid):
    print(f"  Color {color}: {find_pixels(output_grid, color)}")