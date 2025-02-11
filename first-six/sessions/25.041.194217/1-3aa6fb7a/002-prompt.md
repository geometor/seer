[2025-02-10T19:42:45.430413] PROMPT: Description: example_1_code
--------------------------------------------------------------------------------

```python
example_1_input = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

example_1_output = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
```

**images**

input:
<PIL.Image.Image image mode=RGB size=448x448 at 0x707213FBDA20>
output:
<PIL.Image.Image image mode=RGB size=448x448 at 0x707213FBDC60>

**Generate Code**

**NLP:**
["**Natural Language Program:**\n\nThe transformation process is as follows:\nIterate through each cell of the input grid.\nIf a cell's value is 0, examine its four immediate neighbors (up, down, left, right) in the input grid.\nCount how many of these neighbors have a value of 8 in the input grid.\nIf this count is exactly 2, then change the value of the cell in the output grid to 1.\nIf the cell's value in the input grid is 8, then keep its value as 8 in the output grid.\nIf the cell's value in the input grid is 0 and the count of neighboring 8s is not exactly 2, then keep its value as 0 in the output grid.\nApply this rule to every cell to generate the output grid.\n"]

================================================================================
**Python Code Instructions**

- Generate a complete Python module.
- The primary function should be named `transform`, which takes the input grid (represented as a Python list of lists) and returns the transformed output grid (also a Python list of lists).
- Include a docstring at the top of the `transform` function that contains the natural language description of the transformation rule.
- Break logic into sub-functions for clarity - particularly identifying objects and properties.
- Use comments to describe the workflow.
- All major math, science and analysis libraries are available to you.
- Include an `if __name__ == '__main__':` block that:
    - Defines the input grid.
    - Defines the expected output grid.
    - Calls the `transform` function with the input grid.
    - Asserts that the transformed output matches the expected output. Print a clear message indicating success or failure.

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

def helper_function_1(grid): # if needed
    # ...
    pass

def helper_function_2(grid): # if needed
    # ...
    pass

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
