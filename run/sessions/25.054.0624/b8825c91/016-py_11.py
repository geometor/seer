def grid_to_string(grid):
    return '\n'.join([' '.join(map(str, row)) for row in grid])

def analyze_results(examples):
    results = []
    for i, (input_grid, expected_output_grid) in enumerate(examples):
        input_str = grid_to_string(input_grid)
        expected_output_str = grid_to_string(expected_output_grid)
        
        color_changes = analyze_example(input_grid, expected_output_grid)
        results.append(
          {
              "example_number": i + 1,
              "input_grid": input_str,
              "expected_output_grid": expected_output_str,
              "color_changes": color_changes,
          }
        )
    return results
examples_results = analyze_results(examples)
for ex in examples_results:
    print(f"example: {ex['example_number']}")
    print(f"color changes:\n {ex['color_changes']}")
