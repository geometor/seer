def execute_and_capture(code_string):
    """
    Executes a string of Python code and captures its output.

    Args:
      code_string: The Python code to execute.

    Returns:
      A string containing the captured standard output.
    """
    import io, sys

    # Redirect stdout to a string buffer
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    try:
        # Execute the code
        exec(code_string)
    except Exception as e:
        return str(e)  # Return any error as a string
    finally:
        # Restore stdout
        sys.stdout = old_stdout

    # Get the captured output value
    return captured_output.getvalue()


code = """
import copy
import json

input_grid = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

expected_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

def transform(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(grid)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 8:
                if (r > 0 and grid[r-1][c] == 0) and (c+1 < cols and grid[r][c+1] == 8):
                    output_grid[r][c] = 1
                if (r+1 < rows and grid[r+1][c] == 0) and (c > 0 and grid[r][c-1] == 8):
                    output_grid[r][c] = 1

    return output_grid

transformed_grid = transform(input_grid)

if transformed_grid == expected_output:
    print("SUCCESS!\\n")
else:
    print("FAILED!\\n")
    print("Expected Output:\\n", expected_output)
    print("\\nTransformed Output:\\n", transformed_grid)
"""

captured_output = execute_and_capture(code)
print(captured_output)

