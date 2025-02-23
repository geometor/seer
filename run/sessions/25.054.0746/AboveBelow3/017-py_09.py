import numpy as np

def describe_grid(grid):
    rows, cols = grid.shape
    print(f"  Dimensions: {rows}x{cols}")
    unique, counts = np.unique(grid, return_counts=True)
    for color, count in zip(unique, counts):
        print(f"  Color {color}: {count} pixels")


def find_top_rectangle(grid):
    """Finds the top-most horizontal rectangle in the grid."""
    rows, cols = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    top_rectangle = None
    top_row = rows  # Initialize with a row number that's beyond the grid

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                width = 0
                # Check for horizontal rectangle
                c_temp = c
                while c_temp < cols and grid[r, c_temp] == color:
                    width += 1
                    c_temp += 1

                if width > 0: # is it a rectangle?
                    # check if all rows below until color changes are same
                    height = 1
                    r_temp = r + 1
                    valid_rect = True
                    while r_temp < rows and grid[r_temp,c] == color:
                        for i in range(width):
                            if c + i >= cols or grid[r_temp, c+i] != color:
                                valid_rect = False
                                break
                        if not valid_rect:
                            break

                        height += 1
                        r_temp += 1

                    if valid_rect: # we found a rectangle, now check to mark it as visited.
                        for i in range(r, r + height):
                            for j in range(c, c + width):
                                visited[i,j] = True

                        if r < top_row: # is this the top most?
                            top_row = r
                            top_rectangle = ((r, c), (width, height), color)


    return top_rectangle

def analyze_example(input_grid, expected_output, transformed_output):
    print("Input Grid:")
    describe_grid(input_grid)
    input_top_rect = find_top_rectangle(input_grid)
    if input_top_rect:
      print(f"  Top Rectangle: Start={input_top_rect[0]}, Size={input_top_rect[1]}, Color={input_top_rect[2]}")

    print("\nExpected Output Grid:")
    describe_grid(expected_output)
    expected_top_rect = find_top_rectangle(expected_output)
    if expected_top_rect:
      print(f"  Top Rectangle: Start={expected_top_rect[0]}, Size={expected_top_rect[1]}, Color={expected_top_rect[2]}")

    print("\nTransformed Output Grid:")
    describe_grid(transformed_output)
    transformed_top_rect = find_top_rectangle(transformed_output)
    if transformed_top_rect:
      print(f"  Top Rectangle: Start={transformed_top_rect[0]}, Size={transformed_top_rect[1]}, Color={transformed_top_rect[2]}")


input_grid_1 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 3, 3],
    [0, 0, 3, 3, 3, 0, 0, 0]
])
expected_output_1 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 3, 3],
    [0, 0, 3, 3, 3, 0, 0, 0]
])
transformed_output_1 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 3, 3],
    [0, 0, 3, 3, 3, 0, 0, 0]
])

input_grid_2 = np.array([
    [0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0]
])
expected_output_2 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0]
])
transformed_output_2 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [0, 0, 6, 6, 6, 6, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0]
])

input_grid_3 = np.array([
    [0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
expected_output_3 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 4, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
transformed_output_3 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 4, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

analyze_example(input_grid_1, expected_output_1, transformed_output_1)
print("-" * 20)
analyze_example(input_grid_2, expected_output_2, transformed_output_2)
print("-" * 20)
analyze_example(input_grid_3, expected_output_3, transformed_output_3)