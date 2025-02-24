import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    input_objects = {}
    
    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            pixel = input_grid[r,c]
            if pixel != 0:
                if pixel not in input_objects:
                    input_objects[pixel] = []
                input_objects[pixel].append((r,c))
    
    
    # Check for differences between expected and transformed
    differences = np.where(expected_output != transformed_output)
    difference_coordinates = list(zip(differences[0], differences[1]))
    num_differences = len(difference_coordinates)

    print(f"  - Input Objects: {input_objects}")
    print(f"  - Number of differences: {num_differences}")
    print(f"  - Difference coordinates: {difference_coordinates}")

print("Example 1:")
analyze_example(
    [[0, 0, 0, 0], [0, 5, 0, 0]],
    [[8, 0, 8, 0, 8, 0, 8, 0], [0, 5, 0, 0, 0, 5, 0, 0], [8, 0, 8, 0, 8, 0, 8, 0], [0, 5, 0, 0, 0, 5, 0, 0]],
    [[0, 8, 0, 0, 0, 8, 0, 0], [8, 5, 8, 0, 8, 5, 8, 0], [0, 8, 0, 0, 0, 8, 0, 0], [8, 5, 8, 0, 8, 5, 8, 0]]
)

print("\nExample 2:")
analyze_example(
    [[0, 0, 6, 0], [0, 0, 0, 0], [0, 6, 0, 0]],
    [[0, 0, 6, 0, 0, 0, 6, 0], [8, 8, 8, 8, 8, 8, 8, 8], [0, 6, 0, 8, 0, 6, 0, 8], [8, 0, 6, 0, 8, 0, 6, 0], [8, 8, 8, 8, 8, 8, 8, 8], [0, 6, 0, 0, 0, 6, 0, 0]],
    [[0, 8, 6, 8, 0, 8, 6, 8], [0, 8, 8, 0, 0, 8, 8, 0], [8, 6, 8, 0, 8, 6, 8, 0], [0, 8, 6, 8, 0, 8, 6, 8], [0, 8, 8, 0, 0, 8, 8, 0], [8, 6, 8, 0, 8, 6, 8, 0]]
)

print("\nExample 3:")
analyze_example(
    [[0, 0, 0], [0, 4, 0], [0, 0, 0], [0, 0, 0], [4, 0, 0]],
    [[8, 0, 8, 8, 0, 8], [0, 4, 0, 0, 4, 0], [8, 0, 8, 8, 0, 8], [0, 8, 8, 0, 8, 0], [4, 0, 0, 4, 0, 0], [8, 8, 8, 8, 8, 8], [0, 4, 0, 0, 4, 0], [8, 0, 8, 8, 0, 8], [0, 8, 8, 0, 8, 0], [4, 0, 0, 4, 0, 0]],
    [[0, 8, 0, 0, 8, 0], [8, 4, 8, 8, 4, 8], [0, 8, 0, 0, 8, 0], [8, 0, 0, 8, 0, 0], [4, 8, 8, 4, 8, 0], [8, 8, 0, 8, 8, 0], [8, 4, 8, 8, 4, 8], [0, 8, 0, 0, 8, 0], [8, 0, 0, 8, 0, 0], [4, 8, 8, 4, 8, 0]]
)

print("\nExample 4:")
analyze_example(
    [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[8, 0, 8, 0, 8, 0, 8, 0], [0, 2, 0, 0, 0, 2, 0, 0], [8, 0, 8, 0, 8, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0], [8, 0, 8, 0, 8, 0, 8, 0], [0, 2, 0, 0, 0, 2, 0, 0], [8, 0, 8, 0, 8, 0, 8, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 8, 0, 0, 0, 8, 0, 0], [8, 2, 8, 0, 8, 2, 8, 0], [0, 8, 0, 0, 0, 8, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 8, 0, 0, 0, 8, 0, 0], [8, 2, 8, 0, 8, 2, 8, 0], [0, 8, 0, 0, 0, 8, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
)