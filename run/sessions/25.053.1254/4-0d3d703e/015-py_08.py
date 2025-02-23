def analyze_mapping(input_grid, output_grid):
    """
    Analyzes the color mapping between input and output grids.
    """
    mapping = {}
    reverse_mapping = {} # added to check for consistent one to one
    consistent = True

    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            input_color = input_grid[i][j]
            output_color = output_grid[i][j]
            if input_color not in mapping:
                mapping[input_color] = output_color
            elif mapping[input_color] != output_color:
                consistent = False
                print(f"Inconsistency: Input color {input_color} maps to both {mapping[input_color]} and {output_color}")

            if output_color not in reverse_mapping:
                reverse_mapping[output_color] = input_color
            elif reverse_mapping[output_color] != input_color:
                consistent = False
                print(f"Inconsistency: Output color {output_color} maps to both {reverse_mapping[output_color]} and {input_color}")

    return mapping, consistent

# Example Usage (using your provided examples as strings)
examples = [
    (
        [[3, 5, 2], [3, 5, 2], [3, 5, 2]],
        [[4, 1, 6], [4, 1, 6], [4, 1, 6]]
    ),
    (
        [[2, 3, 8], [2, 3, 8], [2, 3, 8]],
        [[6, 4, 9], [6, 4, 9], [6, 4, 9]]
    ),
    (
        [[1, 8, 2], [1, 8, 2], [1, 8, 2]],
        [[1, 9, 2], [1, 9, 2], [1, 9, 2]]
    ),
    (
        [[8, 3, 2], [8, 3, 2], [8, 3, 2]],
        [[8, 3, 6], [8, 3, 6], [8, 3, 6]]
    ),
]

for idx, (input_grid, output_grid) in enumerate(examples):
    mapping, consistent = analyze_mapping(input_grid, output_grid)
    print(f"Example {idx + 1}:")
    print(f"  Mapping: {mapping}")
    print(f"Consistent one-to-one: {consistent}")
