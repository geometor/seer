import numpy as np

def get_diagonal_neighbors(grid, row, col):
    """Gets only the diagonal neighbors of a cell"""
    neighbors = []
    rows, cols = grid.shape
    for i in range(-1,2,2):
        for j in range(-1,2,2):
          if 0 <= row + i < rows and 0 <= col + j < cols:
                neighbors.append(grid[row+i, col+j])

    return neighbors

def analyze_green_pixels(input_grid, expected_output, transformed_output):
    rows, cols = input_grid.shape
    green_pixel_data = {
        "total_green": 0,
        "changed_correctly": 0,
        "changed_incorrectly": 0,
        "missed": 0,
        "diagonal_counts": {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
        "neighboring_non_green_or_black": 0 # count how many green pixels have a neighbor that is not green, black, or out of bounds
    }

    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 3:
                green_pixel_data["total_green"] += 1
                
                # Check neighboring pixels
                neighbor_values = []
                for x in range(max(0, row-1), min(rows, row + 2)):
                    for y in range(max(0, col-1), min(cols, col + 2)):
                        if (x,y) != (row,col):
                          neighbor_values.append(input_grid[x,y])
                          
                if any(neighbor != 3 and neighbor != 0 for neighbor in neighbor_values):
                  green_pixel_data["neighboring_non_green_or_black"] +=1

                diagonal_neighbors = get_diagonal_neighbors(input_grid, row, col)
                count_green = sum(1 for dn in diagonal_neighbors if dn == 3)
                green_pixel_data["diagonal_counts"][count_green] += 1

                if transformed_output[row, col] == 4 and expected_output[row, col] == 4:
                    green_pixel_data["changed_correctly"] += 1
                elif transformed_output[row, col] == 4 and expected_output[row, col] == 3:
                    green_pixel_data["changed_incorrectly"] += 1
                elif transformed_output[row, col] == 3 and expected_output[row, col] == 4:
                    green_pixel_data["missed"] += 1

    return green_pixel_data

# run on each of the examples
for i in range(1,6):
  input_str = f"034-py_17-train-example_{i}.npy"
  expected_str = f"034-py_17-train-example_{i}_out.npy"
  transformed_str = f"034-py_17-train-example_{i}.png.npy"

  input_grid = np.load(input_str)
  expected_output = np.load(expected_str)
  transformed_output = np.load(transformed_str)

  print(f'example {i}:')
  print(analyze_green_pixels(input_grid, expected_output, transformed_output))