# d5d6de2d • 001 • example_1 • investigate_dreamer

---


## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 2 0 2 0 0 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 2 0 0
0 0 0 0 2 0 0 2 0 0
0 0 0 0 2 0 0 2 0 0
0 0 0 0 2 0 0 2 0 0
0 0 0 0 2 2 2 2 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0F9F6A0>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 3 0 0 0
0 0 0 0 0 3 3 0 0 0
0 0 0 0 0 3 3 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0F9C340>

**INSTRUCTIONS**

above is an example pair for a task

this is your opportunity to perceive the underlying logic that transforms the
input into the output

respond with the following deliverables:

- your perception of the elements of the task
- a YAML block documenting facts - Focus on identifying objects, their properties, actions performed on them, and the relationships between them
- a natural language program - Be as clear and concise as possible, providing a complete description of the transformation rule.


your responses should be considered as information in a report - not a conversation
