import numpy as np

def analyze_transformation(input_grid, expected_output_grid):
    input_np = np.array(input_grid)
    expected_output_np = np.array(expected_output_grid)

    input_height, input_width = input_np.shape
    output_height, output_width = expected_output_np.shape
    
    print(f"  Input Dimensions: {input_height}x{input_width}")
    print(f"  Output Dimensions: {output_height}x{output_width}")

    if input_np.shape == expected_output_np.shape[::-1]:
      print("  Shape Relationship: Flipped dimensions (rotation or similar).")
    else:
      print("  Shape Relationship: Not a simple rotation.")

    # Pixel-wise comparison
    print("  Pixel Comparison:")
    total_pixels = input_height * input_width
    matching_pixels = 0
    changed_pixels = [] #list of tuples: ((input_row, input_col), input_val, expected_output_val)

    for row in range(max(input_height, output_height)):
        for col in range(max(input_width, output_width)):
            # Handle cases where input and output dimensions differ.
            if row < input_height and col < input_width:
                input_val = input_np[row, col]
            else:
                input_val = None

            if row < output_height and col < output_width:
                output_val = expected_output_np[row, col]
            else:
                output_val = None


            if input_val == output_val and input_val is not None:
                matching_pixels += 1
            elif input_val is not None and output_val is not None:
               changed_pixels.append( ((row,col), input_val, output_val) )

    print(f"    Matching Pixels: {matching_pixels}/{total_pixels}")
    print(f"    Changed Pixels: {len(changed_pixels)}/{total_pixels}")
    for change in changed_pixels:
        print( "    " + str(change) )

    # check for a 90 degree rotation with a swap.
    rotated_input = np.rot90(input_np, k=-1)  # Rotate 90 degrees clockwise

    if np.array_equal(rotated_input, expected_output_np):
      print("  Transformation: 90 degree clockwise rotation.")
    else:
      print( "  Transformation: Not a simple 90 degree rotation")
      rotated_matching = 0
      for row in range(output_height):
        for col in range(output_width):
          if rotated_input[row,col] == expected_output_np[row,col]:
            rotated_matching += 1

      print( f"    Rotated Matching Pixels: {rotated_matching}/{total_pixels}" )

examples = [
    {
        "input": [[2, 2, 1], [2, 1, 2], [2, 8, 1]],
        "expected_output": [[2, 2, 2], [8, 1, 2], [1, 2, 1]],
        "transformed_output": [[2, 2, 2], [8, 1, 2], [1, 2, 1]]
    },
    {
        "input": [[9, 2, 4], [2, 4, 4], [2, 9, 2]],
        "expected_output": [[2, 9, 2], [4, 4, 2], [4, 2, 9]],
        "transformed_output": [[2, 2, 9], [9, 4, 2], [2, 4, 4]]

    },
    {
        "input": [[8, 8, 8], [5, 5, 8], [8, 5, 5]],
        "expected_output": [[8, 5, 8], [5, 5, 8], [5, 8, 8]],
        "transformed_output": [[8, 5, 8], [5, 5, 8], [5, 8, 8]]
    },
    {
        "input": [[3, 2, 9], [9, 9, 9], [2, 3, 3]],
        "expected_output": [[2, 3, 3], [9, 9, 9], [3, 2, 9]],
        "transformed_output": [[2, 9, 3], [3, 9, 2], [3, 9, 9]]
    }
]

for i, example in enumerate(examples):
    print(f"Example {i + 1}:")
    analyze_transformation(example["input"], example["expected_output"])
    print("-" * 20)