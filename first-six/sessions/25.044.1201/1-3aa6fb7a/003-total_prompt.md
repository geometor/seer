# 25.044.1201 • 1-3aa6fb7a • 003 example_2 - NLP

---

```
example_1_input = [[0, 0, 0, 0, 0, 0, 0],
[0, 8, 0, 0, 0, 0, 0],
[0, 8, 8, 0, 0, 0, 0],
[0, 0, 0, 0, 8, 8, 0],
[0, 0, 0, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]]

example_1_output = [[0, 0, 0, 0, 0, 0, 0],
[0, 8, 1, 0, 0, 0, 0],
[0, 8, 8, 0, 0, 0, 0],
[0, 0, 0, 0, 8, 8, 0],
[0, 0, 0, 0, 1, 8, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]]
```

input
<PIL.Image.Image image mode=RGB size=448x448 at 0x7EAA56105F60>
output
<PIL.Image.Image image mode=RGB size=448x448 at 0x7EAA561061D0>

*text:*
Okay, here's a natural language description of the transformation observed between the input and output grids:

**Natural Language Program:**

1.  **Identify Objects:** Find all instances of the number 8 in the input grid.

2.  **Check Neighbors:** For each instance of the number 8, examine its immediate neighbors (up, down, left, and right).

3.  **Conditional Replacement:**
    *   If an 8 has only one other immediate neighbours that is an 8, change this 8 to the number 1.
    *   If not leave that 8 unchaged.

**In essence, the transformation identifies isolated 8 and converts it to 1.**


*text:*
Okay, here's the Python module with the `transform` function, docstring, and test case, designed to implement the described transformation:



*text:*
```python
"""
1.  **Identify Objects:** Find all instances of the number 8 in the input grid.

2.  **Check Neighbors:** For each instance of the number 8, examine its immediate neighbors (up, down, left, and right).

3.  **Conditional Replacement:**
    *   If an 8 has only one other immediate neighbours that is an 8, change this 8 to the number 1.
    *   If not leave that 8 unchaged.

**In essence, the transformation identifies isolated 8 and converts it to 1.**
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    output_array = np.copy(input_array)

    for r in range(rows):
        for c in range(cols):
            if input_array[r, c] == 8:
                neighbors = []
                # Check up
                if r > 0:
                    neighbors.append(input_array[r-1, c])
                # Check down
                if r < rows - 1:
                    neighbors.append(input_array[r+1, c])
                # Check left
                if c > 0:
                    neighbors.append(input_array[r, c-1])
                # Check right
                if c < cols - 1:
                    neighbors.append(input_array[r, c+1])

                # Count the number of neighboring 8s.
                neighboring_8s = neighbors.count(8)

                if neighboring_8s == 1:
                    output_array[r, c] = 1

    return output_array.tolist()

if __name__ == '__main__':
    input_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input_grid)

    if output == expected_output:
        print("[bold green]SUCCESS![/]")
    else:
        print("[bold red]FAILED![/]")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    assert output == expected_output, "Transformed output does not match expected output."
```

```
example_2_input = [[0, 0, 0, 0, 8, 8, 0],
[0, 0, 0, 0, 0, 8, 0],
[0, 0, 8, 0, 0, 0, 0],
[0, 0, 8, 8, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 8, 0, 0],
[0, 0, 0, 8, 8, 0, 0]]

example_2_output = [[0, 0, 0, 0, 8, 8, 0],
[0, 0, 0, 0, 1, 8, 0],
[0, 0, 8, 1, 0, 0, 0],
[0, 0, 8, 8, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 8, 0, 0],
[0, 0, 0, 8, 8, 0, 0]]
```

input
<PIL.Image.Image image mode=RGB size=448x448 at 0x7EAA56106170>
output
<PIL.Image.Image image mode=RGB size=448x448 at 0x7EAA56106140>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
