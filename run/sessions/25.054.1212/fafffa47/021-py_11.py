import numpy as np

def analyze_example(input_grid, expected_output_grid):
    input_grid = np.array(input_grid)
    expected_output_grid = np.array(expected_output_grid)

    input_height, input_width = input_grid.shape
    output_height, output_width = expected_output_grid.shape

    input_maroon_positions = []
    for r in range(input_height):
        for c in range(input_width):
            if input_grid[r, c] == 9:
                input_maroon_positions.append((r, c))

    output_red_positions = []
    for r in range(output_height):
        for c in range(output_width):
            if expected_output_grid[r, c] == 2:
                output_red_positions.append((r, c))

    print(f"  Input Dimensions: {input_height}x{input_width}")
    print(f"  Output Dimensions: {output_height}x{output_width}")
    print(f"  Input Maroon (9) Positions: {input_maroon_positions}")
    print(f"  Output Red (2) Positions: {output_red_positions}")

print("Example 1:")
analyze_example([
    [0, 9, 9],
    [0, 9, 9],
    [9, 9, 9],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
], [
    [2, 0, 0],
    [2, 0, 0],
    [0, 0, 0]
])

print("\nExample 2:")
analyze_example([
    [9, 0, 9],
    [0, 9, 9],
    [0, 0, 9],
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 0]
], [
    [0, 2, 0],
    [0, 0, 0],
    [0, 2, 0]
])

print("\nExample 3:")
analyze_example([
    [0, 9, 0],
    [9, 0, 9],
    [9, 0, 0],
    [0, 0, 0],
    [0, 0, 1],
    [1, 0, 0]
], [
    [2, 0, 2],
    [0, 2, 0],
    [0, 2, 0]
])

print("\nExample 4:")
analyze_example([
    [0, 0, 9],
    [9, 9, 9],
    [0, 9, 0],
    [1, 0, 0],
    [0, 1, 1],
    [0, 0, 1]
], [
    [0, 2, 0],
    [0, 0, 0],
    [2, 0, 0]
])

print("\nExample 5:")
analyze_example([
    [0, 9, 0],
    [0, 9, 9],
    [0, 9, 9],
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 1]
], [
    [2, 0, 2],
    [0, 0, 0],
    [0, 0, 0]
])