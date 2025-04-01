
## Program Synthesis

> Notes from Chollet Interview
> https://youtu.be/w9WE1aOPjHc

> **life long distributed learning**

- **Focus on Object Relationships and Properties:** 

  The program should identify and describe the objects within the input grid,
  along with their properties (e.g., shape, color, position) and relationships
  with each other (e.g., adjacency, containment). [1] This focus on
  object-centric representation aligns with how humans perceive and understand
  visual scenes.

- **Emphasize Causal Relationships:** 

  Go beyond simply listing object properties and relationships by focusing on
  the causal relationships between them. [1] For example, if an object changes
  color when it moves next to another object, this causal relationship should be
  captured in the program. This aspect helps in understanding the underlying
  rules and transformations within the puzzle.

- **Iterative Program Construction:** 

  The process of building the program should be iterative, similar to how humans
  solve puzzles. [1-3] Start with an initial perception of the scene and
  gradually refine the program as you uncover more patterns and rules through
  observation and reasoning.

- **Deep Learning Guidance:** 

  Deep learning models, particularly LLMs, can play a crucial role in guiding
  the program construction process. [2-4] LLMs can offer "guesses" or
  suggestions about object relationships, properties, and potential
  transformations based on their vast knowledge base. However, it's important to
  treat these suggestions as guidance rather than definitive answers, as LLMs
  can sometimes be unreliable. [5]

- **Verification through Discrete Search:** 

  Once a candidate natural language program is generated, it should be
  translated into a discrete, executable program (e.g., a graph of operators).
  [1, 4] This program can then be run on the input grid to verify if it produces
  the desired output. The ability to execute and verify the program provides a
  crucial check on the accuracy of the perceived "story" and the effectiveness
  of the solution.

