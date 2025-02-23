"""
Transforms an input grid by applying a refined one-to-one color mapping,
where some colors are changed and others remain the same.
"""

def transform(input_grid):
    """
    Transforms the input grid according to the specified mapping.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = [row[:] for row in input_grid]

    # Define the refined color mapping
    mapping = {
        1: 5,
        5: 1,
    }

    # Iterate through the grid and apply the transformation
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Change output pixels based on mapping
            if input_grid[i][j] in mapping:
                output_grid[i][j] = mapping[input_grid[i][j]]
            # else:  implicitly keep the original color, by doing nothing, since output_grid is the copy

    return output_grid