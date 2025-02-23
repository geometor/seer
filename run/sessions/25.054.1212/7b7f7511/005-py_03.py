def analyze_dimensions(input_grid, output_grid):
    input_height = len(input_grid)
    input_width = len(input_grid[0])
    output_height = len(output_grid)
    output_width = len(output_grid[0])
    print(f"Input: {input_height}x{input_width}, Output: {output_height}x{output_width}")

#Example data copied here to run locally
examples = [
    (
        [[1, 1, 3, 2, 1, 1, 3, 2], [1, 1, 3, 3, 1, 1, 3, 3], [3, 3, 1, 1, 3, 3, 1, 1], [2, 3, 1, 1, 2, 3, 1, 1]],
        [[1, 1, 3, 2], [1, 1, 3, 3], [3, 3, 1, 1], [2, 3, 1, 1]]
    ),
    (
        [[4, 4, 4, 4, 4, 4], [6, 4, 8, 6, 4, 8], [6, 6, 8, 6, 6, 8]],
        [[4, 4, 4], [6, 4, 8], [6, 6, 8]]
    ),
    (
        [[2, 3], [3, 2], [4, 4], [2, 3], [3, 2], [4, 4]],
        [[2, 3], [3, 2], [4, 4]]
    )
]

for input_grid, output_grid in examples:
    analyze_dimensions(input_grid, output_grid)
