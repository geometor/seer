# 2-0ca9ddb6 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x79D1212133A0>

**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x79D121211F00>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 2  # Red
      position: (3, 2)
      shape: single cell
    - color: 1  # Blue
      position: (6, 6)
      shape: single cell
  grid_size: (9, 9)

output_grid:
  objects:
    - color: 2  # Red
      position: (3, 2)
      shape: single cell
    - color: 1  # Blue
      position: (6, 6)
      shape: single cell
    - color: 4 # Yellow
      positions: [(2,1), (2,3), (4,1), (4,3)]
      shape: cross shape, centered around red object, distance of 1 cell in cardinal directions.
    - color: 7 # Orange
      positions: [(5,6), (6,5), (6,7), (7,6)]
      shape: cross shape, centered around blue object, distance of 1 cell in cardinal directions.
  grid_size: (9, 9)

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Key Objects:** Locate the single red (color 2) cell and the single blue (color 1) cell in the input grid. These are our primary objects.

2.  **Preserve Key Objects:** The red and blue cells remain unchanged in their original positions in the output grid.

3.  **Create Yellow Cross:** For the red cell:
    *   Place a yellow (color 4) cell one position above.
    *   Place a yellow (color 4) cell one position below.
    *   Place a yellow (color 4) cell one position to the left.
    *   Place a yellow (color 4) cell one position to the right.

4.  **Create Orange Cross:** For the blue cell:
    *   Place an orange (color 7) cell one position above.
    *   Place an orange (color 7) cell one position below.
    *   Place an orange (color 7) cell one position to the left.
    *   Place an orange (color 7) cell one position to the right.

5. **Fill the remaining cells:** keep them as color 0 (white, background)

In essence, the transformation creates a cross-shaped pattern of a specific color around each of the initially present, single-cell colored objects (red and blue), while keeping the original cells unchanged. The surrounding colors are different for red and blue.

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
