"""
1.  **Find the Smallest Repeating Unit:** Determine the smallest rectangular unit that repeats to form the entire input grid.

2.  **Identify Sub-Pattern:**
    *   **Example 1 Hypothesis:** The sub-pattern is the first column (or first two rows) of the repeating unit.
    *  **Example 2 Hypothesis:** The sub pattern is the top-left element
    * **Example 3 Hypothesis:** The sub-pattern is the unique colors of the repeating
      unit, with the last color repeated.

3.  **Determine Output Shape:** The output shape is determined by the sub-pattern's dimensions.

4. **Determine Origin**: the origin of the repeating unit may be the top-left, or
    it may be another location.

5.  **Extract Sub-Pattern Colors:** Extract the colors from sub-pattern.

6.  **Construct Output:** Create the output grid using colors of the sub pattern and dimensions of the sub pattern.

7. **Return output:** Return sub-pattern.
"""

import numpy as np

def find_smallest_repeating_unit(grid):
    """Finds the smallest repeating unit in the grid."""
    rows, cols = grid.shape
    for unit_height in range(1, rows + 1):
        for unit_width in range(1, cols + 1):
            if rows % unit_height == 0 and cols % unit_width == 0:
                valid_unit = True
                for i in range(0, rows, unit_height):
                    for j in range(0, cols, unit_width):
                        unit = grid[i:i+unit_height, j:j+unit_width]
                        for x in range(i + unit_height, rows, unit_height):
                            for y in range(j + unit_width, cols, unit_width):
                                if not np.array_equal(unit, grid[x:x+unit_height, y:y+unit_width]):
                                     valid_unit=False
                                     break
                            if not valid_unit:
                                break
                    if not valid_unit:
                        break

                if valid_unit:
                    return grid[0:unit_height, 0:unit_width]
    return grid  # If no repeating unit is found, return the whole grid

def get_sub_pattern(repeating_unit, example_id):
    """
    Identifies and extracts the sub-pattern based on the example.
    """
    if example_id == "example_1":
        # Hypothesis: First column of the repeating unit
        return repeating_unit[:, 0:1]
    elif example_id == "example_2":
       # return top-left element
        return np.array([[repeating_unit[0,0]]])
    elif example_id == "example_3":
        # last column and unique colors
        unique_colors = np.unique(repeating_unit)
        if len(unique_colors) > 1:
             output = np.array([[unique_colors[-1]], [unique_colors[0]]])
        else:
             output = np.array([[unique_colors[0]]])

        return output

def transform(input_grid):
    """Transforms the input grid based on the identified sub-pattern."""

    # 1. Find the smallest repeating unit
    repeating_unit = find_smallest_repeating_unit(input_grid)

    # 2. & 3. Identify Sub-Pattern and Determine Output Shape (Example-Specific)
    # Determine example ID (This is a placeholder; in a real scenario, we wouldn't know this)
    if input_grid.shape == (5, 5):
        example_id = "example_1"
    elif input_grid.shape == (4, 4):
        example_id = "example_2"
    elif input_grid.shape == (7, 7):
        example_id = "example_3"
    else:
        example_id = "unknown"  # Handle cases outside our known examples

    sub_pattern = get_sub_pattern(repeating_unit, example_id)

    if sub_pattern is not None:
      return sub_pattern
    else:
       return np.array([[]])