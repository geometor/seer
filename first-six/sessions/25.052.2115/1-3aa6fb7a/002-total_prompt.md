# 1-3aa6fb7a • 002 • example_1 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze this transformation. Here's a breakdown of my observations and the deduced transformation rule:


```yaml
facts:
  input_grid_size: 7x7
  output_grid_size: 7x7
  colors_present_input: [0, 8] # white, azure
  colors_present_output: [0, 1, 8] # white, blue, azure
  objects_input: 
    - shape: rectangle
      color: azure
      size: 2x1
      position: (1,1)
    - shape: rectangle
      color: azure
      size: 2x2
      position: (2,1)
    - shape: rectangle
          color: azure
          size: 2x2
          position: (3,4)
    - shape: rectangle
      color: azure
      size: 1x2
      position: (4,4)
  objects_output:
      - shape: rectangle
        color: azure
        size: 2x1
        position: (1,1)
      - shape: rectangle
        color: azure
        size: 2x2
        position: (2,1)
      - shape: rectangle
          color: azure
          size: 2x2
          position: (3,4)
      - shape: rectangle
        color: azure
        size: 1x1
        position: (4,5)
      - shape: rectangle
        color: blue
        size: 1x1
        position: (4,4)          
```


**Natural Language Program:**

1.  **Identify Azure Objects:** Locate all contiguous blocks (objects) of azure (8) pixels in the input grid. These includes the objects of size 2x1, 2x2 and 1x2.

2.  **Preserve most objects.** Copy those objects into the output grid in exactly the same locations and shapes

3.  **Focus on lower right Azure Object.** The object in the lower right part of the grid has a 1x2 shape.

4.  **Split into single pixels**: Divide the object into two objects of size 1 x 1.

5. **Recolor Left Pixel**: Change the color of the left pixel of azure object to blue (1).
6.  **Keep Right Pixel Unchanged**: The azure pixel remains azure.
7. **Output Grid**: The result is placed in the output grid, keeping all other cells as white (0).

In essence, the transformation preserves the azure colored object except lower right objects, it splits the last azure 1x2 shape, and changes the first pixel of splitted shape to blue, keeping the rest azure. All other cells in the grid remain unchanged.

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
