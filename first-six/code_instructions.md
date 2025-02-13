**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- The primary function should be named `transform`, which takes the input grid (represented as a Python list of lists) and returns the transformed output grid (also a Python list of lists).
- Include a docstring at the top of the module that contains the natural language description of the transformation rule.
- Use comments to describe the workflow.
- All major math, science and analysis libraries are available to you.
- Include an `if __name__ == '__main__':` block that:
    - Defines the input grid.
    - Defines the expected output grid.
    - Calls the `transform` function with the input grid.
    - Asserts that the transformed output matches the expected output. Print a clear message indicating success or failure.

- if your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Skeleton Template**

```python
"""
{{ natural language description of the transformation rule }}
"""

{{ allowed imports that support the transform }}

input = {input_grid_rows}

expected_output = {expected_output_grid_rows}

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."

```
