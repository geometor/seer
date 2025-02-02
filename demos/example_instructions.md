
# INSTRUCTIONS

below is a pair of example input and output grids 

- document your initial observations and impressions. 
  begin with a verbal description of your perception of the elements of the grids - objects, colors, relationships, and if possible, the transformation rule

- focus your analysis on aspects like:

    - Counting the occurrences of each color.
    - How to identify the coordinates of pixels that have changed color or position.
    - Determining if the dimensions of the grid have changed.
    - Analyzing the count, size, shape, and relative positions of objects (contiguous
      blocks of the same color).

use a yaml block to capture details that may be useful (examples):

```yaml
input:
  width: X
  height: Y
  colors:
    - N: (count)
  objects:
    - size, position and color - desc
```

```yaml
differences:
  cells_changed: N
  colors_changed: desc
  transformation:
    - speculate on transformation rules
```

- propose code that can help identify objects patterns and relationships
- use what you learn to develop a natural language program of the
  transformation rule.
- review your findings and try to determine the natural language description of
  the transformation rule. How does the information captured in the YAML block
  inform your understanding of the transformation?


the natural language program should be sufficient for an intelligent agent to
perform the operation of generating an output grid from the input, without the
benefit of seeing the examples. So be sure that the provide 

For example, it might state: 

- copy input to working output
- identify sets of pixels in blue (1) rectangles in working grid
- identify to largest rectangle
- set the largest rectangle's pixels to red (2)

But remember - any information that describe the story of the transformations is
desired. Be flexible and creative. 

when the natural language program is complete, use it to develop a python
function to transform the input into the output

