# Conceptual Code - for demonstration, cannot be directly executed

def detailed_analysis(examples):
    results = []
    for ex in examples:
        input_grid = ex['input']
        output_grid = ex['output']
        example_id = ex['id']

        # Basic analysis (already in provided code)
        input_analysis = analyze_grid(input_grid, example_id + "_input")
        output_analysis = analyze_grid(output_grid, example_id + "_output")
       
        # 1. Color Mapping Analysis
        color_mapping = {} #input color -> output color
        for out_row_idx in range(output_grid.shape[0]):
          for in_row_idx, row in enumerate(input_grid):
            if in_row_idx == out_row_idx:
              unique_colors = np.unique(row)
              for color in unique_colors:
                if color != 5 and color != 0:
                    if color not in color_mapping:
                      color_mapping[color]= output_grid[out_row_idx][0]

        results.append({
            'example_id': example_id,
            'input_analysis': input_analysis,
            'output_analysis': output_analysis,
            'color_mapping': color_mapping,

        })
    return results

conceptual_results = detailed_analysis(examples)
print(conceptual_results)
