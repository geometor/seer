**Python Code Instructions**

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
\"\"\"
Natural language description of the transformation rule goes here.
\"\"\"

# Imports (e.g., numpy, sympy)

def transform(input_grid):
    \"\"\"
    Transforms the input grid according to the rule.
    \"\"\"
    # Implementation goes here


if __name__ == '__main__':
    input_grid = [
        # ... Input grid data ...
    ]

    expected_output = [
        # ... Expected output grid data ...
    ]

    transformed_grid = transform(input_grid)

    if transformed_grid == expected_output:
        print("Transformation successful!")
    else:
        print("Transformation failed.")
        print("Expected Output:", expected_output)
        print("Transformed Output:", transformed_grid)

    assert transformed_grid == expected_output, "Transformed output does not match expected output."

```
