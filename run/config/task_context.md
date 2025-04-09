
# TASK

Our tasks are from ARC-AGI (Abstraction and Reasoning Corpus)
Each task contains a set input-output examples.
SEER will analyze the examples to derive a natural language description of the
context and transformations, then use this to develop a python function to
perform the transformation.
We will verify the function on all the example input-output pairs, if
successful, we will use the function to transform the test input into the final
output. 

ARC inputs and outputs are grids (2d arrays) where each cell is a value of
the integers 0-9.
A grid can be any height or width between 1 x 1 and 30 x 30.
Grid values represent colors using this mapping:

```
COLOR_MAP = {
    0: (238, 238, 238),  # white
    1: (30, 147, 255),  # blue
    2: (220, 50, 40),  # red
    3: (79, 204, 48),  # green
    4: (230, 200, 0),  # yellow
    5: (85, 85, 85),  # gray
    6: (229, 58, 163),  # magenta
    7: (230, 120, 20),  # orange
    8: (135, 216, 241),  # azure
    9: (146, 18, 49),  # maroon
}
```

We will refer to cells as pixels.
Use the color name when referring to the value.

# Priors
ARC-AGI is explicitly designed to compare artificial intelligence with human
intelligence. To do this, ARC-AGI explicitly lists the priors knowledge human
have to provide a fair ground for comparing AI systems. These core knowledge
priors are ones that humans naturally possess, even in childhood.

## Objectness
- Objects persist and cannot appear or disappear without reason. 
- An object can be considered a contiguous block of one or more pixels of the same color.
- Objects can interact or not depending on the circumstances.

## Goal-directedness
- Objects can be animate or inanimate.
- Some objects are "agents" - they have intentions and they pursue goals.  

## Numbers & counting
- Objects can be counted or sorted by their shape, appearance, or movement using
  basic mathematics like addition, subtraction, and comparison.

## Basic geometry & topology
- Objects can be shapes like rectangles, triangles, and circles which can be
  mirrored, rotated, translated, deformed, combined, repeated, etc. Differences
  in distances can be detected.
- Adjacency is very important - side by side and diagonal

ARC-AGI avoids a reliance on any information that isn't part of these priors,
for example acquired or cultural knowledge, like language.
