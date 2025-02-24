import numpy as np

def find_objects(grid):
    # Find distinct objects in the grid.
    objects = []
    visited = set()

    def is_valid(row, col):
        return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

    def dfs(row, col, color, obj):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        # Explore adjacent cells (up, down, left, right)
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row_index, row in enumerate(grid):
        for col_index, cell_value in enumerate(row):
            if (row_index, col_index) not in visited and cell_value != 0:
                obj = []
                dfs(row_index, col_index, cell_value, obj)
                objects.append(obj)
    return objects

def calculate_centroid(coords):
    # Calculate the centroid of a list of coordinates.
    if not coords:
        return None
    sum_row = sum(coord[0] for coord in coords)
    sum_col = sum(coord[1] for coord in coords)
    centroid_row = sum_row // len(coords)
    centroid_col = sum_col // len(coords)
    return (centroid_row, centroid_col)
    
def analyze_example(input_grid, expected_output, transformed_output):
    print(f"--- Example Analysis ---")
    print(f"Input Grid:\n{input_grid}")
    
    input_objects = find_objects(input_grid)
    print(f"\nInput Objects Found: {len(input_objects)}")
    for i, obj in enumerate(input_objects):
        print(f"  Object {i+1}:")
        print(f"    Coordinates: {obj}")
        centroid = calculate_centroid(obj)
        print(f"    Centroid: {centroid}")
        min_row = min(coord[0] for coord in obj)
        max_row = max(coord[0] for coord in obj)
        min_col = min(coord[1] for coord in obj)
        max_col = max(coord[1] for coord in obj)
        print(f"    Bounding Box: ({min_row}, {min_col}) to ({max_row}, {max_col})")


    print(f"\nExpected Output:\n{expected_output}")
    print(f"\nTransformed Output:\n{transformed_output}")

    diff = expected_output - transformed_output
    print(f"\nDifferences (Expected - Transformed):\n{diff}")
    
    print("--- End Example ---")


# Example data (as numpy arrays)
input1 = np.array([
    [0, 6, 6, 6, 0, 0, 0, 0],
    [0, 6, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 6, 6],
    [0, 0, 0, 0, 0, 6, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])
expected1 = np.array([
    [0, 6, 6, 6, 0, 0, 0, 0],
    [0, 6, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 6, 6],
    [0, 0, 0, 0, 0, 6, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 4, 0]
])
transformed1 = transform(input1)

input2 = np.array([
    [0, 3, 3, 3, 0],
    [0, 3, 0, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])
expected2 = np.array([
    [0, 3, 3, 3, 0],
    [0, 3, 0, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0]
])
transformed2 = transform(input2)


input3 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 8, 8, 0, 0, 0],
    [0, 8, 0, 8, 6, 6, 6],
    [0, 0, 0, 0, 6, 0, 6],
    [0, 0, 0, 0, 0, 0, 0]
])
expected3 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 8, 8, 0, 0, 0],
    [0, 8, 0, 8, 6, 6, 6],
    [0, 0, 0, 0, 6, 0, 6],
    [0, 0, 4, 0, 0, 4, 0]
])
transformed3 = transform(input3)

analyze_example(input1, expected1, transformed1)
analyze_example(input2, expected2, transformed2)
analyze_example(input3, expected3, transformed3)
