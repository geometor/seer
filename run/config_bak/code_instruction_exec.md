**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- Follow the template below
- If your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Transform Template:**

```python
"""
{{ natural language description of the transformation rule }}
"""

{{ allowed imports that support the transform }}

def transform(input_grid: list[list[int]]) -> list[list[int]]:
    # initialize output_grid

    # perform transformation 

    return output_grid


if __name__ == '__main__':

    input_grid = {input_grid_rows}

    expected_output_grid = {expected_output_grid_rows}

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output)_grid

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."

```
