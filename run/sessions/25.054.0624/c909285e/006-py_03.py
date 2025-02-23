"""
1.  **Identify Repeating Pattern:** For each training example, find the smallest rectangular subgrid that repeats both horizontally and vertically to fully cover the *input* grid.
2.  **Extract Pattern:** Store one instance of this repeating subgrid.
3.  **Learn Color Mapping:**  Create a dictionary to store the mapping between the top-left color of the repeating pattern in the input and the top-left color of the corresponding output.  For each training example, add/update this mapping.
4. **Apply to Input:** For the given input grid, identify the repeating pattern using the same logic as in step 1.
5. **Transform:** Using the learned color mapping, replace the top-left color of the identified repeating pattern in the *input* grid with its corresponding mapped color from the color mapping dictionary, and create new output.
6.  **Output:** The transformed subgrid is the output.

"""

import numpy as np

def find_repeating_pattern(grid):
    # Find the smallest repeating pattern in the grid
    rows, cols = grid.shape
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if rows % i == 0 and cols % j == 0:
                pattern = grid[:i, :j]
                valid_pattern = True
                for row_mult in range(rows // i):
                    for col_mult in range(cols // j):
                        if not np.array_equal(grid[row_mult*i:(row_mult+1)*i, col_mult*j:(col_mult+1)*j], pattern):
                            valid_pattern = False
                            break
                    if not valid_pattern:
                        break
                if valid_pattern:
                    return pattern
    return None #should never occur as 1x1 is always a repeating unit


def transform(input_grid, train_grids=None):
    # Convert the input grid to a NumPy array
    input_grid = np.array(input_grid)

    # Create color map if training grids provided
    color_map = {}

    if train_grids:
        for inp, out in train_grids:
            inp_np = np.array(inp)
            out_np = np.array(out)

            pattern = find_repeating_pattern(inp_np)
            if pattern is not None: # will always execute
                input_top_left_color = pattern[0, 0]
                output_top_left_color = out_np[0, 0]
                color_map[input_top_left_color] = output_top_left_color

    # Find the repeating pattern in input
    pattern = find_repeating_pattern(input_grid)
    if pattern is None: return input_grid #should not occur

    # Identify top-left colors
    input_top_left_color = pattern[0, 0]
    
    # Apply color mapping. If no map, return input.
    output_top_left_color = color_map.get(input_top_left_color)
    if output_top_left_color is None:
        return input_grid.tolist()

    # Create a copy of the pattern to modify
    output_grid = pattern.copy()

    # Replace the color in the extracted pattern
    output_grid = np.where(output_grid == input_top_left_color, output_top_left_color, output_grid)
    

    return output_grid.tolist()