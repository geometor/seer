25.043.202845 • 1-3aa6fb7a • example_1 - CODE
--------------------------------------------------------------------------------
Okay, let's analyze the transformation from the input grid to the output grid.

Here's a step-by-step description of the observed transformation:

**Natural Language Program:**

1.  **Identify Target Pixels:** Find all pixels in the input grid with the value '8'.

2.  **Check neighbors and Find a pattern:**
    *   The output value '1' appears when the input value is '8' and is vertically or horizontally adjacent to at most one other '8'.

3.  **Apply the change based on the context:**
    - If an '8' pixel is next to at most one other '8', change the pixel color value from 8 to 1.
    - If the '8' pixel matches more than one another '8', then keep value as 8.
    - Keep the '0' in the same places.

**In summary:** The transformation identifies '8' pixels, examines the number of immediate adjacent neighbor with '8', and those that are "alone" or has one neighbor changes that to '1' in the output grid. Other pixels remain unchanged.

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

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':
    input = [
        {{ Input grid rows }}
    ]

    expected_output = [
        {{ expected output grid rows }}
    ]

    output = transform(input)

    if output == expected_output:
        print("[bold green]SUCCESS![/]")
    else:
        print("[bold red]FAILED![/]")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    assert output == expected_output, "Transformed output does not match expected output."

```
