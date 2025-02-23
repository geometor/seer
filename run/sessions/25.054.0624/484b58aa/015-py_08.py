import numpy as np
from collections import Counter

def analyze_grid_diff(input_grid, expected_output_grid):
    """
    Analyzes the differences between the input and expected output grids.
    
    Args:
      input_grid: numpy array
      expected_output_grid: numpy array

    Returns:
      a dict with differences
    """

    input_grid = np.array(input_grid)
    expected_output_grid = np.array(expected_output_grid)

    # Check if the shapes are the same
    if input_grid.shape != expected_output_grid.shape:
      return {
            "match": f"ERROR: shapes are different input {input_grid.shape} output {expected_output_grid.shape}",
            "pixels_off": None,
            "size_correct": False,
            "color_palette_correct": None,
            "correct_pixel_counts": None,
        }


    diff = input_grid == expected_output_grid
    pixels_off = np.sum(~diff)  # Count where they are NOT equal
    size_correct = input_grid.size == expected_output_grid.size
    
    input_colors = Counter(input_grid.flatten())
    output_colors = Counter(expected_output_grid.flatten())
    color_palette_correct = set(input_colors.keys()) == set(output_colors.keys())    
    correct_pixel_counts = input_colors == output_colors

    return {
        "match": pixels_off == 0,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts
    }


def calculate_metrics(examples):
    results = []
    for i, (input_grid, expected_output_grid) in enumerate(examples):
        # Convert to numpy arrays
        input_grid = np.array(input_grid)
        expected_output_grid = np.array(expected_output_grid)
        # Compare shapes to determine if a reshape error will occur
        if input_grid.shape != expected_output_grid.shape:
            # Calculate size difference assuming removal of a color
            size_difference = input_grid.size - expected_output_grid.size
            reshape_possible = False
            error_message = f"ERROR: cannot reshape array of size {expected_output_grid.size} into shape {input_grid.shape}"
        else:
           size_difference = 0
           reshape_possible = True # Assuming same shape indicates correct removal
           error_message = None

        analysis = analyze_grid_diff(input_grid, expected_output_grid)

        result = {
            "example_index": i + 1,
            "input_shape": input_grid.shape,
            "expected_output_shape": expected_output_grid.shape,
            "match": analysis['match'],
            "pixels_off": analysis['pixels_off'],
            "size_correct": analysis['size_correct'],
            "color_palette_correct":analysis['color_palette_correct'],
            "correct_pixel_counts": analysis['correct_pixel_counts'],
            "size_difference": size_difference,
            "reshape_possible": reshape_possible,
            "error_message": error_message,
        }
        results.append(result)
    return results