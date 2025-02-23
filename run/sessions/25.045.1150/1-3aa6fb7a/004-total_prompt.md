# 25.045.1150 • 1-3aa6fb7a • 004 example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x73C43A81DCC0>

**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x73C43A81E0E0>

*text:*
**Natural Language Program: Transformation Rule**

1. **Identify 'Azure' (color 8) Objects:** Locate all contiguous blocks of cells containing the color 'azure' (8) in the input grid. These blocks are considered as objects.
2. **Examine Neighbors of 'Azure' Objects:** For each cell that is part of an 'azure' object, inspect its immediate neighboring cells (up, down, left, right).
3. **Conditional Color Change:** If a neighboring cell of an 'azure' object has the color 'white' (0), change the color of this neighboring cell to 'blue' (1) in the output grid.
4. **Maintain Unaffected Cells:**  All cells in the input grid that are not neighbors of an 'azure' object (and are 'white') or are already part of an 'azure' object, retain their original color in the output grid. In essence, only 'white' cells directly adjacent to 'azure' objects are transformed to 'blue'.

*text:*
```python
"""
Identifies 'Azure' (color 8) objects in the input grid.
For each cell in an 'azure' object, it checks its immediate neighbors (up, down, left, right).
If a neighboring cell is 'white' (0), it changes the color of this neighbor to 'blue' (1) in the output grid.
All other cells remain unchanged.
"""

import copy

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8:  # Identify 'Azure' objects
                # Examine Neighbors
                neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols: # Check bounds
                        if input_grid[nr][nc] == 0: # Conditional Color Change
                            output_grid[nr][nc] = 1
    return output_grid


if __name__ == '__main__':

    input = [
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

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x73C43A81DFF0>

**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x73C43A81E4D0>

*text:*
**Natural Language Program: Transformation Rule**

1. **Identify 'Azure' (color 8) Objects:** Locate all contiguous blocks of cells containing the color 'azure' (8) in the input grid. These blocks are considered as objects.
2. **Examine Neighbors of 'Azure' Objects:** For each cell that is part of an 'azure' object, inspect its immediate neighboring cells (up, down, left, right).
3. **Conditional Color Change:** If a neighboring cell of an 'azure' object has the color 'white' (0), change the color of this neighboring cell to 'blue' (1) in the output grid.
4. **Maintain Unaffected Cells:**  All cells in the input grid that are not neighbors of an 'azure' object (and are 'white') or are already part of an 'azure' object, retain their original color in the output grid. In essence, only 'white' cells directly adjacent to 'azure' objects are transformed to 'blue'.
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- Follow the template below
- If your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Transform Template:**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

    input = [
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
