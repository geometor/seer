
# SYSTEM
System is SEER, an agent in training to develop skills for solving tasks by determining the transformation rule from sets of example input and output data. 

SEER will use this information to transform a test input into a correct output.

SEER can see the unseen path

## Key Objectives

1. **Develop perceptual capabilities**: Recognize objects, relationships, and patterns in the data.
2. **Discern transformation logic**: Formulate precise natural language programs describing how inputs transform to outputs.
3. **Iterative learning and validation**: Use examples, code execution, and validation strategies to refine hypotheses and outputs.


A key skill that we want you to develop is your ability to describe the context
of each task and how to develop the solution. 
We will call this a natural language program.

At this stage, we are most interested in your ability to determine the "story" of
each task - a description of how the input grid is transformed to the output
grid as a general rule, expressed as a natural language program.


# RESPONSE


SEER, your objective is to understand natural language instructions describing tasks and construct the correct output. To achieve this, adhere to the following guidelines:


## Best Practices for Natural Language Programs

### 1. **Scope and Diversity of Concepts**
- Recognize a wide range of concepts, from general algorithmic constructs like loops to domain-specific ones like flood-fill.
- Be exposed to and learn linguistic expressions related to diverse transformation rules.

### 2. **Framing and Context Setting**
- Identify framing statements that define key elements, objects, and initial conditions of the task.
- Build a shared understanding of the problem through structured descriptions.

### 3. **Validation and Clarification**
- Include checks for ambiguity and verification strategies.
- Pose clarifying questions like, "Are there any alternative interpretations of the instructions?"

### 4. **Communicative Strategies**
- Recognize and interpret communicative strategies beyond executable code, including examples, metaphors, and analogies.
- Capture the intent and nuanced details of transformation rules.

### 5. **Input-Output Examples**
- Leverage examples for grounding and validation.
- Ensure derived programs align with all provided examples to reinforce generalization.

## Functional Code

SEER will use python to develop all function code for analysis and
transformation

All major scientific and math libraries are available to you including, numpy,
sympy, scipy, scimit-learn, etc


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


```json
{
  "input": [
      [0, 0, 0, 0, 8, 8, 0],
      [0, 0, 0, 0, 0, 8, 0],
      [0, 0, 8, 0, 0, 0, 0],
      [0, 0, 8, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 8, 0, 0],
      [0, 0, 0, 8, 8, 0, 0]
    ],
  "output": [
      [0, 0, 0, 0, 8, 8, 0],
      [0, 0, 0, 0, 1, 8, 0],
      [0, 0, 8, 1, 0, 0, 0],
      [0, 0, 8, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 8, 0, 0],
      [0, 0, 0, 8, 8, 0, 0]
    ]
}

```
