import numpy as np

def find_bounding_pixels(input_grid):
    """Finds the outermost non-background pixels."""
    rows, cols = input_grid.shape
    non_bg_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_bg_pixels.append((r, c))
    return non_bg_pixels

def analyze_example(input_grid, expected_output):
    """Analyzes a single example."""
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    bounding_pixels = find_bounding_pixels(input_grid)
    min_row = min(r for r, c in bounding_pixels) if bounding_pixels else -1
    max_row = max(r for r, c in bounding_pixels) if bounding_pixels else -1
    min_col = min(c for r, c in bounding_pixels) if bounding_pixels else -1
    max_col = max(c for r, c in bounding_pixels) if bounding_pixels else -1
    height = max_row - min_row + 1 if bounding_pixels else 0
    width = max_col - min_col + 1 if bounding_pixels else 0

    print(f"  Bounding Pixels: {bounding_pixels}")
    print(f"  Min Row: {min_row}, Max Row: {max_row}, Height: {height}")
    print(f"  Min Col: {min_col}, Max Col: {max_col}, Width: {width}")
    print(f"  Expected Output Shape: {expected_output.shape}")

print("Example 1:")
analyze_example([
    [0, 8, 0, 0, 0, 8, 0],
    [8, 8, 0, 0, 0, 8, 8],
    [0, 0, 0, 0, 0, 0, 0],
    [8, 8, 0, 0, 0, 8, 8],
    [0, 8, 0, 0, 0, 8, 0]
], [
    [0, 8, 0],
    [8, 8, 8],
    [0, 8, 0]
])

print("\nExample 2:")
analyze_example([
    [2, 2, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 2, 0],
    [2, 0, 0, 0, 0, 0, 2]
], [
    [2, 2, 2],
    [0, 2, 2],
    [2, 0, 2]
])

print("\nExample 3:")
analyze_example([
    [4, 4, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 4]
], [
    [4, 4, 0],
    [0, 4, 4],
    [4, 0, 4]
])
print("\nExample 4:")

analyze_example([
    [4, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 4, 4]

],
    [
        [4, 0, 4],
        [0, 0, 0],
        [4, 4, 4]
])

print("\nExample 5:")
analyze_example([
   [0, 3, 0, 0, 0, 3, 0],
    [3, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3]
], [
    [0, 3, 0],
    [3, 0, 3],
    [0, 0, 3]
])