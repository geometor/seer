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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

Here's a YAML block summarizing the initial observations:

```yaml
observations:
  input_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (3, 2)
        shape: single cell
      - color: 1 (blue)
        position: (6, 6)
        shape: single cell
    background_color: 0 (white)
  output_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (3, 2)
        shape: single cell
      - color: 1 (blue)
        position: (6, 6)
        shape: single cell
      - color: 4 (yellow)
        positions: [(2, 1), (2, 3), (4, 1), (4, 3)]
        shape: single cells forming a cross pattern, centered around the red object
      - color: 7 (orange)
        positions: [(5,6), (6, 5), (6, 7), (7, 6)]
        shape: single cells, surrounding the blue object
    background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the step-by-step transformation:

1.  **Identify Key Objects:** Locate the single red (color 2) and single blue (color 1) cells in the input grid. These are our pivotal objects.

2.  **Yellow Cross Creation:** Around the red cell, create a cross pattern using yellow (color 4) cells. The cross extends one cell above, below, to the left and to the right. Place yellow cells such that if the red cell were at the origin (0,0), the yellow cells would be in coordinates (-1,0), (1, 0), (0,1) and (0,-1). Notice we must apply a translation to the red dot coordinates to achieve this.

3.  **Orange Surround:** Around the blue cell, place orange (color 7) cells. Create surrounding cells on every cardinal and diagonal positions. Place orange cells such that if the blue cell was at the origin (0,0) the orange cells would be in coordinates (-1,0), (1,0), (0,-1), (0, 1). Notice we must apply a translation to the blue dot coordinates to achieve this. In the actual case, only 4 orange cells are surrounding the blue cell in the positions corresponding to the cardinal directions.

4.  **Preserve original cells**: maintain the red cell and blue cell in their original positions.

**Natural Language Program**

The transformation can be described as a "decoration" rule centered around the initial red and blue cells. The red cell gets a yellow cross, the blue cells are sorrounded by orange cells in the four cardinal directions.

1. Copy the red and blue cells from the input grid.

2. Create a yellow cross centered on the position of the red cell from the input grid, extending one cell in each cardinal direction.

3. Create a set of four orange cells surrounding the blue cell in the input grid, one cell away in each cardinal direction.

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
