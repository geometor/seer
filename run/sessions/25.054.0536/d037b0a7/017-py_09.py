def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example to gather relevant metrics."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)
    
    rows, cols = input_grid.shape
    
    pixel_diff = np.sum(expected_output != transformed_output)
    
    print(f"  Dimensions: {rows}x{cols}")
    print(f"  Pixels Different: {pixel_diff}")
    
    for j in range(cols):
      top_color = input_grid[0,j]
      print(f" col {j}:")
      print(f"  top color: {top_color}")
      
      for i in range(1,rows):
          print(f"   row {i}: input {input_grid[i,j]}, expected {expected_output[i,j]}, actual {transformed_output[i,j]}")

print("Example 1:")
analyze_example(
    [[0, 0, 6], [0, 4, 0], [3, 0, 0]],
    [[0, 0, 6], [0, 4, 6], [3, 4, 6]],
    [[0, 0, 6], [0, 0, 6], [0, 0, 6]],
)

print("\nExample 2:")
analyze_example(
    [[0, 2, 0], [7, 0, 8], [0, 0, 0]],
    [[0, 2, 0], [7, 2, 8], [7, 2, 8]],
    [[0, 2, 0], [0, 2, 0], [0, 2, 0]],
)

print("\nExample 3:")
analyze_example(
    [[4, 0, 0], [0, 2, 0], [0, 0, 0]],
    [[4, 0, 0], [4, 2, 0], [4, 2, 0]],
    [[4, 0, 0], [4, 0, 0], [4, 0, 0]],
)
