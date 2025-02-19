# 1a07d186 • 002 • example_1 - CODE

---

**input**
```
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 4 0 3 0 0 3 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 4 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 2 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 3 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1216x1152 at 0x79CABB63B520>

**output**
```
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 3 0 0 0 0 0 0 4 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 4 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 3 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1216x1152 at 0x79CABB63BA60>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_observations:
  - object_1:
      color: 3 (green)
      shape: vertical line
      position: column 4
      length: 18
  - object_2:
      color: 4 (yellow)
      shape: vertical line
      position: column 13
      length: 18
  - object_3:
      color: 2 (red)
      shape: single cell
      position: (11,8)
  - object_4:
        color: 4
        shape: single cell
        position: (4,2)
  - object_5:
        color: 3
        shape: single cell
        position: (12, 17)

output_observations:
   - object_1:
      color: 3 (green)
      shape: vertical line
      position: column 4
      length: 18
   - object_2:
      color: 4 (yellow)
      shape: vertical line
      position: column 13
      length: 18
   - object_3:
      color: 3,
      shape: single cell
      position: (4,5)
   - object_4:
      color: 4,
      shape: single cell
      position: (4,14)      
   - object_5:
      color: 4,
      shape: single cell
      position: (8, 12)      
   - object_6:
      color: 3,
      shape: single cell
      position: (12,5)          
```

**Natural Language Program: Transformation Rule**

1.  **Identify Persistent Objects:** There are two primary persistent objects: a green vertical line (color 3) in column 4 and a yellow vertical line (color 4) in column 13. These remain unchanged in terms of shape, color, and position.

2.  **Copy, move and change color**: Every other color, different from 3 and 4 will:

    *   Be deleted if they exist.
    *    If they are green or yellow, two copies of them must be made next to the green and yellow columns respectively, to the right of the green column and to the left of the yellow one.

**Step-by-step explanation based on the example:**

*   The red cell (2) is removed.
*    The single green cell at (12,17) will be moved to (12,5)
*    The single yellow cell at (4,2) will be moved to (4,14) and (8,12).


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
