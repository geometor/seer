# TASK CONTEXT

Your goal is to analyze and transform grid-based puzzles from ARC-AGI. Each task provides example input and output grids. The grids are 2D arrays (sizes ranging from 1×1 to 30×30) where each cell holds an integer (0–9) representing a color. Use the following color mapping:

```
0: white (238,238,238)
1: blue (30,147,255)
2: red (220,50,40)
3: green (79,204,48)
4: yellow (230,200,0)
5: gray (85,85,85)
6: magenta (229,58,163)
7: orange (230,120,20)
8: azure (135,216,241)
9: maroon (146,18,49)
```

**Task Overview**

- **Observation and Documentation:**
  + Examine the input and output grids.
  + Identify objects (contiguous blocks of
    the same color), count color occurrences, and note geometric properties
    (size, shape, position).
  + Summarize your findings in a YAML block.

- **Determining the Transformation Rule:**
  + Describe in natural language the step-by-step transformation observed.
  + objects, predicates and actions

- **Python Implementation:**
  + Using your natural language description, develop a Python function that
    transforms any given input grid into the correct output grid.
  + Leverage common libraries (e.g., numpy, sympy) if needed, and ensure your
    code covers all edge cases as per the transformation rule.

**Key Concepts and Priors**

- **Objectness:**
  + Objects are contiguous regions or patterns of the same color. 

  + Objects persist and cannot appear or disappear without reason. Objects can interact or not depending on the circumstances.

- **Goal-Directedness:**
  + Some objects may have specific roles or “intentions.”
Objects can be animate or inanimate. Some objects are "agents" - they have intentions and they pursue goals.

- **Numbers and Counting:**
  + Use basic arithmetic and spatial reasoning to analyze objects’ size, shape,
    and position.
  + Objects can be counted or sorted by their shape, appearance, or movement using basic mathematics like addition, subtraction, and comparison.

- **Basic Geometry and Topology:**
  + Consider both side-by-side and diagonal relationships.
  + Objects can be shapes like rectangles, triangles, and circles which can be mirrored, rotated, translated, deformed, combined, repeated, etc. Differences in distances can be detected.