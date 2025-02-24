# bd4472b8 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
3 2 1 4
5 5 5 5
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC47F93C70>

**output:**
```
3 2 1 4
5 5 5 5
3 3 3 3
2 2 2 2
1 1 1 1
4 4 4 4
3 3 3 3
2 2 2 2
1 1 1 1
4 4 4 4
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC4757C580>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves transforming a grid of single-digit integers (representing colors) into another grid of integers. The input grid appears to have two distinct regions: a top region with varied non-zero digits, and a bottom region filled entirely with zeros. The output grid retains the top two rows of the input, replaces the zero region with a repeating pattern based on the first row of the input.

**YAML Fact Documentation:**


```yaml
facts:
  - observation: |
      The input grid is a 2D array of integers, each representing a color.
  - object: InputGrid
    properties:
      - dimensions: 10 rows x 4 columns
      - top_region:  Rows 1-2 contains a variety of non-zero digits.
      - bottom_region: Rows 3-10 are all zeros.
  - object: OutputGrid
    properties:
      - dimensions: 10 rows x 4 columns
      - top_region: Identical to InputGrid's top_region (Rows 1 and 2)
      - bottom_region: Contains repetitions of the first row of InputGrid.
  - action: Copy
    details: Rows 1 and 2 of InputGrid are copied directly to OutputGrid.
  - action: Repeat
    details: The sequence of digits in the first row of InputGrid is repeated to form the bottom part of OutputGrid.
  - relationship: |
     The OutputGrid's bottom region (rows 3-10) is constructed by repeating InputGrid's first row four times each 2 rows.
```


**Natural Language Program:**

1.  **Copy:** Copy the first two rows of the input grid directly to the output grid.
2.  **Repeat:** Take the first row of the input grid.
3. **Fill Bottom:** Starting from the third row of the output grid, fill all subsequent rows by repeating the sequence of digits from the first row. Repeat the first row sequence four times in total to fill the output. The rows created are 4 * 2 = 8 rows.


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
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
