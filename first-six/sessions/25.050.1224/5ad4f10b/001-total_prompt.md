# 5ad4f10b • 001 • example_1 - NLP

---

**input**
```
0 0 0 0 0 0 0 0 0 8 8 0 0 0 0 0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 0 0 8 0 0 0 0 0 0 0 0 0 0 8 0 0
0 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 0 8 0 0 0
0 0 0 4 4 4 4 8 0 0 0 4 4 4 4 0 0 0 0 0 0 8 0 0
0 0 0 4 4 4 4 0 0 0 0 4 4 4 4 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 4 4 4 4 0 0 8 0 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 4 4 4 4 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 4 4 4 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 4 4 4 0 0 0 0 8 0 0 8 0 0 0 0 0
0 0 0 0 0 0 0 4 4 4 4 8 0 0 0 0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 4 4 4 4 0 0 0 0 8 0 0 0 0 0 0 0 0
0 0 0 4 4 4 4 4 4 4 4 4 4 4 4 0 0 0 0 8 8 0 8 0
0 0 0 4 4 4 4 4 4 4 4 4 4 4 4 0 0 8 0 0 0 0 0 0
0 0 0 4 4 4 4 4 4 4 4 4 4 4 4 0 0 0 0 8 0 0 0 0
8 0 0 4 4 4 4 4 4 4 4 4 4 4 4 0 0 8 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 8 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 8 0 0 0 8 0 0 0 8 0 8 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
8 8 0 8 0 8 0 0 0 0 8 0 0 0 0 0 0 0 8 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1536x1280 at 0x79CABB63BA60>

**output**
```
8 0 8
0 8 0
8 8 8
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x79CABB63B520>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
