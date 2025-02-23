def calculate_correct_mapping(examples):
    """Calculates and prints the mapping of input values to output values."""
    mapping = {}
    for input_grid, output_grid in examples:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                input_val = input_grid[i, j]
                output_val = output_grid[i, j]
                #mapping[input_val] = output_val # wrong - overwrites previous
                mapping[(i,j,input_val)] = output_val # tuple key includes position
    return mapping

correct_mapping = calculate_correct_mapping(examples)
print(correct_mapping)