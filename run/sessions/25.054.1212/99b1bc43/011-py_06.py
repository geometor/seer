import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    rows, cols = input_grid.shape
    row_mid = rows // 2
    col_mid = cols // 2

    quadrants = {
        "Q1": input_grid[0:row_mid, 0:col_mid],
        "Q2": input_grid[0:row_mid, col_mid:cols],
        "Q3": input_grid[row_mid:rows, 0:col_mid],
        "Q4": input_grid[row_mid:rows, col_mid:cols],
    }

    output_quadrants = {
       "Q1": transformed_output[0:2, 0:2],
       "Q2": transformed_output[0:2, 2:4],
       "Q3": transformed_output[2:4, 0:2],
       "Q4": transformed_output[2:4, 2:4],
    }
    
    expected_output_quadrants = {
       "Q1": expected_output[0:2, 0:2],
       "Q2": expected_output[0:2, 2:4],
       "Q3": expected_output[2:4, 0:2],
       "Q4": expected_output[2:4, 2:4],
    }

    report = {
      "input_shape": input_grid.shape,
      "quadrant_data" : {},
      "output_quadrant_data": {},
      "expected_output_quadrant_data": {}
    }
    for q_name, quad in quadrants.items():
      report["quadrant_data"][q_name] = {
          "shape": quad.shape,
          "non_zero_count": np.count_nonzero(quad),
          "unique_colors": np.unique(quad[quad != 0]).tolist(),
      }
    for q_name, quad in output_quadrants.items():
      report["output_quadrant_data"][q_name] = {
          "shape": quad.shape,
          "non_zero_count": np.count_nonzero(quad),
          "unique_colors": np.unique(quad[quad != 0]).tolist(),
      }
    for q_name, quad in expected_output_quadrants.items():
      report["expected_output_quadrant_data"][q_name] = {
          "shape": quad.shape,
          "non_zero_count": np.count_nonzero(quad),
          "unique_colors": np.unique(quad[quad != 0]).tolist(),
      }

    return report

# Example Data
example1_input = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 0, 1], [4, 4, 4, 4], [0, 2, 0, 2], [0, 0, 0, 2], [2, 0, 0, 2], [2, 2, 2, 0]]
example1_expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 3, 3], [3, 3, 3, 3]]
example1_transformed = [[3, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 3]]

example2_input = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [4, 4, 4, 4], [0, 2, 2, 2], [2, 0, 2, 0], [2, 2, 2, 2], [2, 2, 2, 2]]
example2_expected = [[3, 0, 3, 3], [0, 0, 0, 0], [0, 0, 3, 0], [3, 0, 0, 3]]
example2_transformed = [[3, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 3]]

example3_input = [[0, 1, 0, 0], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [4, 4, 4, 4], [0, 0, 0, 0], [0, 2, 0, 2], [2, 2, 0, 2], [0, 2, 0, 0]]
example3_expected = [[0, 3, 0, 0], [3, 3, 3, 0], [0, 0, 3, 3], [3, 0, 3, 0]]
example3_transformed = [[3, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 3]]

example4_input = [[1, 0, 1, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [4, 4, 4, 4], [0, 2, 2, 2], [0, 2, 2, 2], [2, 0, 2, 2], [2, 2, 2, 2]]
example4_expected = [[3, 3, 0, 0], [0, 3, 3, 0], [0, 3, 3, 3], [3, 3, 0, 0]]
example4_transformed = [[3, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 3]]

examples = [
    (example1_input, example1_expected, example1_transformed),
    (example2_input, example2_expected, example2_transformed),
    (example3_input, example3_expected, example3_transformed),
    (example4_input, example4_expected, example4_transformed),
]

reports = [analyze_example(i, e, t) for i, e, t in examples]

for i, report in enumerate(reports):
  print(f"Report for Example {i+1}:")
  print(report)
  print("-" * 20)