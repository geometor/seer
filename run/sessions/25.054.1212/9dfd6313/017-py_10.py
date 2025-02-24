import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    input_objects = find_objects(input_grid)
    expected_objects = find_objects(expected_output)
    transformed_objects = find_objects(transformed_output)

    print("Input Objects:", input_objects)
    print("Expected Objects:", expected_objects)
    print("Transformed Objects:", transformed_objects)

    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape == transformed_output.shape
    color_palette_correct = set(input_grid.flatten()) == set(expected_output.flatten()) == set(transformed_output.flatten())

    # Count occurrences of each color
    input_color_counts = {color: np.sum(input_grid == color) for color in np.unique(input_grid)}
    expected_color_counts = {color: np.sum(expected_output == color) for color in np.unique(expected_output)}
    transformed_color_counts = {color: np.sum(transformed_output == color) for color in np.unique(transformed_output)}

    correct_pixel_counts = input_color_counts == expected_color_counts == transformed_color_counts


    print("Pixels Off:", pixels_off)
    print("Size Correct:", size_correct)
    print("Color Palette Correct:", color_palette_correct)
    print("Correct Pixel Counts:", correct_pixel_counts)
    print("-" * 20)

# Example Data (from the prompt)
example1_input = [[5, 0, 0], [3, 5, 0], [0, 0, 5]]
example1_expected = [[5, 3, 0], [0, 5, 0], [0, 0, 5]]
example1_transformed = [[0, 0, 0], [5, 0, 0], [3, 5, 0]]

example2_input = [[5, 0, 0, 0], [0, 5, 0, 0], [6, 0, 5, 0], [6, 0, 4, 5]]
example2_expected = [[5, 0, 6, 6], [0, 5, 0, 0], [0, 0, 5, 4], [0, 0, 0, 5]]
example2_transformed = [[0, 0, 0, 0], [5, 0, 0, 0], [0, 5, 0, 0], [6, 0, 5, 0]]

example3_input = [[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [8, 8, 5, 0, 0], [0, 2, 0, 5, 0], [0, 2, 0, 1, 5]]
example3_expected = [[5, 0, 8, 0, 0], [0, 5, 8, 2, 2], [0, 0, 5, 0, 0], [0, 0, 0, 5, 1], [0, 0, 0, 0, 5]]
example3_transformed = [[0, 0, 0, 0, 0], [5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 5, 0]]

# Find Objects Function (from the prompt)

def find_objects(grid):
    """Identifies distinct objects in the grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, color, current_object)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c]:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r, c], current_object))  # Store color and object pixels
    return objects

analyze_example(example1_input, example1_expected, example1_transformed)
analyze_example(example2_input, example2_expected, example2_transformed)
analyze_example(example3_input, example3_expected, example3_transformed)