import numpy as np

def analyze_transformation(input_grid, expected_output_grid):
    """
    Analyzes the transformation between an input grid and its expected output.

    Args:
        input_grid: A 3x3 numpy array representing the input grid.
        expected_output_grid: A 3x3 numpy array representing the expected output grid.

    Returns:
        A dictionary containing the mapping of input coordinates to output coordinates
        and a list of mismatched pixels.
    """
    input_grid = np.array(input_grid)
    expected_output_grid = np.array(expected_output_grid)

    coordinate_mapping = {}
    mismatched_pixels = []

    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_value = input_grid[i, j]
            output_coordinates = np.argwhere(expected_output_grid == input_value)
            
            #find the correct output
            found = False
            for coords in output_coordinates:
                
                coords_tuple = tuple(coords)
                
                already_mapped_to = False
                for k,v in coordinate_mapping.items():
                    if v == coords_tuple:
                        already_mapped_to = True
                        break
                
                if not already_mapped_to:
                    coordinate_mapping[(i, j)] = coords_tuple
                    found = True
                    break
            
            if not found:
                coordinate_mapping[(i, j)] = "not found"

            if not np.any(np.all([i, j] == output_coordinates, axis=1)):
              
                mismatched_pixels.append(((i,j), input_grid[i,j], expected_output_grid[i,j]))


    return coordinate_mapping, mismatched_pixels


# Example data (replace with your actual data)
examples = [
    (
        [[2, 2, 1], [1, 5, 1], [5, 2, 2]],
        [[2, 1, 5], [2, 5, 2], [1, 1, 2]],
    ),
    (
        [[2, 2, 5], [6, 2, 2], [5, 5, 5]],
        [[2, 6, 5], [2, 2, 5], [5, 2, 5]],
    ),
    (
        [[9, 9, 5], [5, 5, 8], [5, 8, 9]],
        [[9, 5, 5], [9, 5, 8], [5, 8, 9]],
    ),
    (
        [[2, 6, 6], [2, 1, 1], [2, 6, 2]],
        [[2, 2, 2], [6, 1, 6], [6, 1, 2]],
    ),
]

for example_num, (input_grid, expected_output_grid) in enumerate(examples):
    mapping, mismatches = analyze_transformation(input_grid, expected_output_grid)
    print(f"Example {example_num + 1}:")
    print("Coordinate Mapping (Input -> Output):")
    for input_coord, output_coord in mapping.items():
        print(f"  {input_coord} -> {output_coord}")
    print("Mismatched Pixels (Input Coord, Input Value, Expected Output Value):")
    for mismatch in mismatches:
        print(f"  {mismatch}")
    print("-" * 30)
