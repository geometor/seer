"""
1.  **Identify Significant Object:** Find the most prominent object in the input grid based on a combination of size, connectivity, and potentially its color (Azure in Example 1, Blue in Example 2, red in example 3). "Prominence" is still not precisely defined and needs further refinement. It might be the *largest* connected region of a specific color.

2.  **Find Rightmost/Leftmost Vertical Edge (Stripe):** Determine the rightmost/leftmost continuous vertical edge (a "stripe" in the current code's terminology, but better understood as an *edge*) of this significant object.

3.  **Define Transformation Region:**  The region to be colored green starts one column to the *right* of this edge and extends to the right edge of the grid. Or, if the edge found in the previous step is the left-most, define a region up to a change in the color (in this case, black).

4.  **Color Transformation:**  Change all pixels within the defined transformation region to green (color code 3). Pixels outside this region remain unchanged.
"""

import numpy as np
from scipy.ndimage import measurements

def find_largest_object(grid, color):
    """
    Finds the largest connected region of a specific color in the grid.

    Args:
        grid: The input grid (numpy array).
        color: The color to search for.

    Returns:
        A mask representing the largest object of the given color, or None if no object of that color is found.
    """
    colored_pixels = (grid == color)  # Create a boolean mask for the specified color
    labeled_array, num_features = measurements.label(colored_pixels)
    
    if num_features == 0:
        return None  # No objects of the specified color found

    # Find the size of each labeled object
    object_sizes = measurements.sum(colored_pixels, labeled_array, index=range(1, num_features + 1))

    # Find the label of the largest object
    largest_object_label = np.argmax(object_sizes) + 1

    # Create a mask for the largest object
    largest_object_mask = (labeled_array == largest_object_label)
    
    return largest_object_mask

def find_rightmost_edge(mask):
    """
    Finds the rightmost column index of a boolean mask.

    Args:
        mask: A boolean mask (numpy array).

    Returns:
        The column index of the rightmost edge, or -1 if the mask is empty.
    """
    if not np.any(mask):
        return -1
    
    return np.max(np.where(mask)[1])

def find_leftmost_edge(mask):
    """
    Find the leftmost column index of a boolean mask
    """
    if not np.any(mask):
      return -1

    return np.min(np.where(mask)[1])

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find the largest object for different target colors
    largest_azure_object = find_largest_object(input_grid, 8)  # Azure
    largest_blue_object = find_largest_object(input_grid, 1)  # Blue
    largest_red_object = find_largest_object(input_grid, 2) # Red

    # determine which object and edge to use
    if largest_azure_object is not None:
        rightmost_column = find_rightmost_edge(largest_azure_object)
        start_column = rightmost_column + 1
        end_column = output_grid.shape[1] - 1
    elif largest_blue_object is not None:
        rightmost_column = find_rightmost_edge(largest_blue_object)
        start_column = rightmost_column + 1
        end_column = output_grid.shape[1] - 1
    elif largest_red_object is not None:
      leftmost_column = find_leftmost_edge(largest_red_object)
      # find first black pixel
      for col_index in range(leftmost_column+1, input_grid.shape[1]):
        if np.any(input_grid[:, col_index] == 0):
          end_column = col_index - 1
          break
        else:
          end_column = input_grid.shape[1]-1
      start_column = leftmost_column
    else:
      return output_grid


    # color transformation
    if largest_azure_object is not None or largest_blue_object is not None:
      for row_index in range(output_grid.shape[0]):
          for col_index in range(start_column, end_column + 1):  # Inclusive range
              output_grid[row_index, col_index] = 3
    elif largest_red_object is not None:
      for row_index in range(output_grid.shape[0]):
          for col_index in range(start_column, end_column + 1):
            output_grid[row_index, col_index] = 3
    
    return output_grid