# 5-150deff5 • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 0 0 0
0 0 0 0 5 5 0 0 0
0 0 0 5 0 0 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x512 at 0x7745ED0170A0>

**output:**
```
0 0 0 0 0 0 0 0 0
0 2 2 2 8 8 0 0 0
0 0 0 0 8 8 0 0 0
0 0 0 2 0 0 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x512 at 0x7745ED0170D0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a 2D grid of single-digit integers (representing colors) into another 2D grid of the same dimensions. The primary element is a shape formed by the color gray (5) in the input grid. This shape seems to be getting decomposed and recolored in the output grid. The surrounding white pixels (0) remain unchanged. The gray (5) shape appears to be split into two new shapes: a red (2) shape and an azure (8) shape. The red shape maintains the leftmost outline of the original, and the azure extends from red to the rightmost outline.

**YAML Fact Block:**


```yaml
facts:
  - observation: Input and output grids have the same dimensions.
  - observation: Background color (0 - white) remains unchanged.
  - object:      GrayShape
    color:       5 (gray)
    property:    Contiguous block of pixels.
    action:      Decomposed into two new shapes.
  - object:      RedShape
    color:       2 (red)
    property:    Forms the left outline of the original GrayShape.
  - object:      AzureShape
    color:       8 (azure)
    property:    Extends to the right outline from the RedShape and takes the same shape, but shifted.

```


**Natural Language Program:**

1.  **Identify** the contiguous shape formed by gray (5) pixels in the input grid.
2.  **Preserve** all pixels with the color white (0) in their original positions in the output grid.
3.  **Create** a new shape, colored red (2). This shape will be the leftmost vertical line of the original gray.
4.  **Create** a second shape, colored azure(8). This starts from the immediate right of the red shape and extends the same shape, but shifted.
5. **Place** these new color shapes in the output.


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
