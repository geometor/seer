def analyze_example(input_grid, expected_output, transformed_output):
    import numpy as np

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)
    
    input_non_zero = np.count_nonzero(input_grid)
    input_colors = set(np.unique(input_grid)) - {0}    
    
    expected_non_zero = np.count_nonzero(expected_output)
    expected_colors = set(np.unique(expected_output)) - {0}
    
    transformed_non_zero = np.count_nonzero(transformed_output)
    transformed_colors = set(np.unique(transformed_output)) - {0}
        

    report = {
        "input_grid_shape": input_grid.shape,
        "expected_output_shape": expected_output.shape,
        "transformed_output_shape": transformed_output.shape,        
        "input_non_zero_count": input_non_zero,
        "input_colors": list(input_colors),
        "expected_non_zero_count": expected_non_zero,        
        "expected_colors": list(expected_colors),
        "transformed_non_zero_count": transformed_non_zero,        
        "transformed_colors": list(transformed_colors),
    }
    return report