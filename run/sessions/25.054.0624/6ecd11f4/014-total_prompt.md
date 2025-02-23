# 6ecd11f4 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 0 0 0 0 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 0 0 0 0 0 0 0 0 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 0 0 0 0 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 0 0 0 0 8 8 8 8 0 0 0 0
0 0 8 8 8 8 0 0 0 0 0 0 0 0 8 8 8 8 0 0 0 0
0 0 8 8 8 8 8 8 8 8 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 8 8 8 8 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 8 8 8 8 8 8 8 8 0 0 0 0 0 0 0 0
0 0 8 8 8 8 8 8 8 8 8 8 8 8 0 0 0 4 1 9 4 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 6 3 6 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 5 7 5 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 4 2 7 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1408x1408 at 0x70FFF01249D0>

**output:**
```
4 0 9 4
6 0 6 0
3 0 0 5
2 4 2 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x70FFF0ECF7F0>
Okay, I'm ready to analyze this example and try to figure out the transformation. Here's my breakdown:

**Perception of Elements:**

*   The input is a large grid (22x22) mostly filled with white pixels (0).
*   There's a large, irregular shape made of azure pixels (8) in the center.
*   There's a smaller, dense 4x4 block of multi-colored pixels at the lower right.
*   The output is a smaller grid (4x4) that seems to correspond to the 4x4 multi-colored block in the input, however the last digit of each row in the block is moved to the beginning.

**YAML Block (Facts):**


```yaml
objects:
  - type: large_grid
    dimensions: 22x22
    dominant_color: white (0)
  - type: irregular_shape
    color: azure (8)
    location: center
  - type: multi_color_block
    dimensions: 4x4
    location: lower_right
    colors: [4,1,9,4,6,3,6,1,3,5,7,5,2,4,2,7]
  - type: output_grid
    dimensions: 4x4
    colors: derived from multi_color_block

actions:
  - type: extraction
    description: The multi-color block is extracted from the input grid.
  - type: circular_shift
    description: moving last element to first position within each row.
    

```


**Natural Language Program:**

1.  **Locate** the 4x4 multi-colored block in the lower right of the input grid.
2.  **Extract** the values from each row from this 4x4 block.
3.  **Circular Shift Right**: For each extracted row, shift the last element of each row and insert to first position.
4.  **Construct** the output grid with these modified rows.

In essence, the program extracts a specific region from the input, then rearranges the elements by rotating each row's to the right, by one.

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
