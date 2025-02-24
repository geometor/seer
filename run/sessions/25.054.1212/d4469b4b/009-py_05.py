import numpy as np

def simplified_transform(input_grid):
    #copy central pixel
    output_grid = np.zeros((3,3),dtype=int)
    output_grid[1,1] = input_grid[2,2]
    # check colors
    for x in range(0,5):
        for y in range(0,5):
            if input_grid[x,y] != 0 and not( x > 0 and x < 4 and y > 0 and y < 4):
                if x == 0 or x == 4: output_grid[2,1] = 5
                if y == 0 or y == 4: output_grid[0,1] = 5
    return output_grid

def analyze_example(input_str, expected_str):
    input_grid = np.array([list(map(int, row.split())) for row in input_str.split('\n')])
    expected_grid = np.array([list(map(int, row.split())) for row in expected_str.split('\n')])
    transformed_grid = simplified_transform(input_grid)

    print("Input:")
    print(input_grid)
    print("Expected Output:")
    print(expected_grid)
    print("Transformed Output (Simplified):")
    print(transformed_grid)
    print("Matches Expected:", np.array_equal(transformed_grid, expected_grid))
    print("---")
    return transformed_grid


# Example Data (as strings)
examples = [
    (
        """2 0 0 0 0
0 2 0 0 2
2 0 0 2 0
0 0 0 2 2
0 0 2 2 0""",
        """5 5 5
0 5 0
0 5 0"""
    ),
    (
        """0 0 0 0 0
0 0 1 1 1
0 1 0 1 1
0 1 0 1 0
0 0 0 0 1""",
        """0 5 0
5 5 5
0 5 0"""
    ),
    (
        """3 0 0 0 0
0 0 0 3 3
0 3 3 0 0
0 3 0 3 0
3 0 3 3 0""",
        """0 5 0
0 5 5
0 5 0"""
    ),
    (
        """1 0 1 0 0
1 0 0 1 1
1 1 0 1 0
0 1 0 1 0
1 0 0 0 1""",
        """0 5 0
5 5 5
0 5 0"""
    ),
     (
        """2 0 2 0 2
2 0 0 0 2
2 2 0 0 0
2 0 0 2 2
2 2 2 0 2""",
        """5 5 5
0 5 0
0 5 0"""
    ),
      (
        """0 2 0 2 0
0 2 2 2 0
0 2 2 0 2
2 2 2 0 0
0 0 2 0 2""",
        """5 5 5
0 5 0
0 5 0"""
    ),
     (
        """0 3 0 3 0
3 3 0 0 0
0 3 0 0 0
0 0 3 0 0
3 3 3 0 0""",
        """0 5 0
0 5 5
0 5 0"""
    ),
]

# Analyze each example
for input_str, expected_str in examples:
    analyze_example(input_str, expected_str)