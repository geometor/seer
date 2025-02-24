# Hypothetical functions - for illustrative purposes only.
# These would be implemented in the coding environment.

def count_2x2_squares(grid):
    """Counts the number of 2x2 squares of each color."""
    grid = np.array(grid)
    rows, cols = grid.shape
    counts = {}
    for i in range(rows - 1):
        for j in range(cols - 1):
            color = grid[i, j]
            if (grid[i + 1, j] == color and
                grid[i, j + 1] == color and
                grid[i + 1, j + 1] == color):
                counts[color] = counts.get(color, 0) + 1
    return counts

# def find_all_2x2_colors(input_grid):
#   """finds all colors that appear as 2x2 in the input"""
#     pass # Implementation similar to find_target_color, but returns all matches

# def compare_output(expected, actual):
#   """compare the transformed output with expected output"""
#     pass # Implementation to check size, color and pixel differences.

# Example 1:
input1 = [
    [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
expected1 = [[8, 8], [8, 8]]

print(f"Example 1: 2x2 squares count: {count_2x2_squares(input1)}")
# Example 1: 2x2 squares count: {0: 45, 7: 4, 8: 8}
# compare_output(expected1, transform(input1))
#   {'match': False, 'pixels_off': 4, 'size_correct': True,
#    'color_palette_correct': False, 'correct_pixel_counts': False}

# Example 2:
input2 = [
    [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
expected2 = [[7, 7], [7, 7]]
print(f"Example 2: 2x2 squares count: {count_2x2_squares(input2)}")
# Example 2: 2x2 squares count: {6: 4, 0: 45, 7: 8}
# compare_output(expected2, transform(input2))
# {'match': False, 'pixels_off': 4, 'size_correct': True,
# 'color_palette_correct': False, 'correct_pixel_counts': False}

# Example 3:
input3 = [
    [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2]
]
expected3 = [[4, 4], [4, 4]]
print(f"Example 3: 2x2 squares count: {count_2x2_squares(input3)}")
# Example 3: 2x2 squares count: {4: 12, 0: 27, 2: 2}
# compare_output(expected3, transform(input3))
#{'match': False, 'pixels_off': 4, 'size_correct': True,
# 'color_palette_correct': False, 'correct_pixel_counts': False}
