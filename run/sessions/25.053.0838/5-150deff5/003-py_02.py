import numpy as np

input_grid = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

output_grid = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
    [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

def get_object_pixels(grid, color):
    return np.argwhere(grid == color)

def get_neighbors(grid, row, col):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                neighbors.append((nr, nc))
    return neighbors

def peel(grid, object_pixels):
    peeled_pixels = []
    remaining_pixels = []
    
    object_pixels_set = set(map(tuple, object_pixels))

    for row, col in object_pixels_set:
        neighbors = get_neighbors(grid, row, col)
        is_peeled = False
        for nr, nc in neighbors:
            if (nr, nc) not in object_pixels_set:
                is_peeled = True
                break
        if is_peeled:
            peeled_pixels.append((row, col))
        else:
            remaining_pixels.append((row, col))
    return peeled_pixels, remaining_pixels


gray_pixels = get_object_pixels(input_grid, 5)
peeled_pixels, remaining_pixels = peel(input_grid, gray_pixels)
azure_pixels = get_object_pixels(output_grid, 8)
red_pixels = get_object_pixels(output_grid, 2)


print(f"Gray Pixels: {gray_pixels}")
print(f"Number of Gray Pixels: {len(gray_pixels)}")
print(f"Peeled Pixels: {peeled_pixels}")
print(f"Number of Peeled Pixels: {len(peeled_pixels)}")
print(f"Remaining Pixels: {remaining_pixels}")
print(f"Number of Remaining Pixels: {len(remaining_pixels)}")
print(f"Azure Pixels: {azure_pixels}")
print(f"Number of Azure Pixels: {len(azure_pixels)}")
print(f"Red Pixels: {red_pixels}")
print(f"Number of Red Pixels: {len(red_pixels)}")


# Check if peeled pixels match azure pixels and remaining pixels match red pixels
peeled_pixels_set = set(peeled_pixels)
azure_pixels_set = set(map(tuple, azure_pixels))
remaining_pixels_set = set(remaining_pixels)
red_pixels_set = set(map(tuple, red_pixels))

print(f"Peeled pixels match Azure pixels: {peeled_pixels_set == azure_pixels_set}")
print(f"Remaining pixels match Red pixels: {remaining_pixels_set == red_pixels_set}")
