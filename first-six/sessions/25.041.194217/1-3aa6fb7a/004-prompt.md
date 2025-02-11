[2025-02-10T19:42:54.426130] PROMPT: Description: example_2_code
--------------------------------------------------------------------------------

```python
example_2_input = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
]

example_2_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0],
]
```

**images**

input:
<PIL.Image.Image image mode=RGB size=448x448 at 0x707213E1B9D0>
output:
<PIL.Image.Image image mode=RGB size=448x448 at 0x707213E1BE80>

**Generate Code**

**NLP:**
["**Natural Language Program:**\n\nThe transformation process operates on each cell of the input grid to produce the output grid. For each cell in the input grid, we check its value. If the cell's value is 0, we then examine its immediate neighbors - the cells directly above, below, to the left, and to the right. We count how many of these neighboring cells in the input grid have a value of 8. If this count is exactly two, the corresponding cell in the output grid is set to 1. If the original cell in the input grid has a value of 8, then the corresponding cell in the output grid retains the value 8. In all other cases for cells with initial value 0 (meaning the count of neighboring 8s is not exactly two), the corresponding cell in the output grid remains 0.  This process is repeated for every cell in the input grid to construct the complete output grid.\n"]

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
