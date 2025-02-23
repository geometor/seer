import numpy as np

def compare_grids(output_grid, expected_grid):
    """Compares two grids and returns metrics."""
    output_grid = np.array(output_grid)
    expected_grid = np.array(expected_grid)
    if output_grid.shape != expected_grid.shape:
        size_correct = False
        pixels_off = None # cannot compute meaningfully if size is different
    else:
        size_correct = True
        diff_grid = output_grid != expected_grid
        pixels_off = np.sum(diff_grid)

    color_palette_output = set(np.unique(output_grid))
    color_palette_expected = set(np.unique(expected_grid))
    color_palette_correct = (color_palette_output == color_palette_expected)

    output_counts = {}
    expected_counts = {}
    for color in range(10): # Assuming colors 0-9
        output_counts[color] = np.sum(output_grid == color)
        expected_counts[color] = np.sum(expected_grid == color)
    correct_pixel_counts = (output_counts == expected_counts)

    diff_locations = []
    if size_correct:
        for r in range(output_grid.shape[0]):
            for c in range(output_grid.shape[1]):
                if output_grid[r, c] != expected_grid[r, c]:
                    diff_locations.append(((r, c), output_grid[r,c], expected_grid[r,c]))


    return {
        "match": size_correct and pixels_off == 0,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "diff_locations": diff_locations,
        "output_counts": output_counts,
        "expected_counts": expected_counts
    }

# Example 1 data
input_grid_1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                           [0, 8, 0, 0, 0, 0, 0],
                           [0, 8, 8, 0, 0, 0, 0],
                           [0, 0, 0, 0, 8, 8, 0],
                           [0, 0, 0, 0, 0, 8, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]])
expected_output_1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                              [0, 8, 1, 0, 0, 0, 0],
                              [0, 8, 8, 0, 0, 0, 0],
                              [0, 0, 0, 0, 8, 8, 0],
                              [0, 0, 0, 0, 1, 8, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0]])
transformed_output_1 = transform(input_grid_1)


# Example 2 data
input_grid_2 = np.array([[0, 0, 0, 0, 8, 8, 0],
                           [0, 0, 0, 0, 0, 8, 0],
                           [0, 0, 8, 0, 0, 0, 0],
                           [0, 0, 8, 8, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 8, 0, 0],
                           [0, 0, 0, 8, 8, 0, 0]])
expected_output_2 = np.array([[0, 0, 0, 0, 8, 8, 0],
                              [0, 0, 0, 0, 1, 8, 0],
                              [0, 0, 8, 1, 0, 0, 0],
                              [0, 0, 8, 8, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 1, 8, 0, 0],
                              [0, 0, 0, 8, 8, 0, 0]])
transformed_output_2 = transform(input_grid_2)


report1 = compare_grids(transformed_output_1, expected_output_1)
report2 = compare_grids(transformed_output_2, expected_output_2)

print("Example 1 Report:", report1)
print("Example 2 Report:", report2)