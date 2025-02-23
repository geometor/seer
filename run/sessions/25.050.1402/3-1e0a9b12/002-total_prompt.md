# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x778677E1B550>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x778677E19E10>
**Natural Language Program:**

The transformation rule is to move all non-zero numbers in each column to the bottom of the column, filling the empty spaces at the top with zeros.  The order of the non-zero numbers within each column is preserved, although in this example each column contains at most one non-zero number.

**Step-by-step transformation:**

1. **Iterate through each column** of the input grid from left to right.
2. **For each column**, identify and extract all the non-zero numbers, maintaining their original order from top to bottom.
3. **Count the number of non-zero numbers** extracted for the current column. Let's call this count 'N'.
4. **In the corresponding column of the output grid**, fill the bottom 'N' rows with the extracted non-zero numbers, in the same order as they were extracted.
5. **Fill the remaining rows at the top** of the output column with zeros.
6. Repeat steps 2-5 for all columns.

This process effectively "pushes down" all the non-zero numbers in each column to the bottom.
**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
