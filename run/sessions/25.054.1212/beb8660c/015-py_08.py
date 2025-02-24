import numpy as np

def analyze_example(input_grid, output_grid):
    input_grid = np.array(input_grid)
    output_grid = np.array(output_grid)

    changed_pixels = []
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r,c] != output_grid[r,c]:
                changed_pixels.append( ((r,c), input_grid[r,c], output_grid[r,c]) )


    print(f"  Changed Pixels: {changed_pixels}")
    print(f"  Input Shape: {input_grid.shape}")
    print(f"  Output Shape: {output_grid.shape}")

print("Example 1:")
analyze_example([
    [0, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0],
    [8, 8, 8, 8, 8, 8, 8]
], [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 6, 6, 6, 6, 6],
    [0, 0, 0, 4, 4, 4, 4],
    [0, 5, 5, 5, 5, 5, 5],
    [8, 8, 8, 8, 8, 8, 8]
])

print("\nExample 2:")
analyze_example([
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 0, 0, 0],
    [0, 3, 3, 0],
    [0, 0, 0, 0],
    [8, 8, 8, 8]
], [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 3, 3],
    [0, 2, 2, 2],
    [8, 8, 8, 8]
])

print("\nExample 3:")
analyze_example([
    [2, 2, 0],
    [0, 4, 0],
    [8, 8, 8]
], [
    [0, 0, 4],
    [0, 2, 2],
    [8, 8, 8]
])