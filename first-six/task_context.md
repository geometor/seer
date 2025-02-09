**ARC-AGI Transformation Task**

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
  + Objects are contiguous regions of the same color. They persist unless transformed.

- **Goal-Directedness:** 
  + Some objects may have specific roles or “intentions.”

- **Counting & Geometry:** 
  + Use basic arithmetic and spatial reasoning to analyze objects’ size, shape,
    and position.

- **Adjacency:** 
  + Consider both side-by-side and diagonal relationships.

**Your Deliverables**

- A YAML summary of your observations.
- A clear natural language description (a “natural language program”) detailing the transformation rule.
- A Python module that implements this transformation
  + place the natural language description in the top docstring
  + break logic into sub-functions for clarity - particularly identifying objects and properties
  + use comments to describe the workflow
  + all major math, science and analysis libraries are available to you


