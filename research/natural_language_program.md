## Best Practices for Developing Natural Language Programs

> notes from the LARC project
> https://github.com/samacqua/LARC

When developing coaching for SEER's system instructions to help it discern well-crafted natural language programs for puzzle descriptions, consider the following aspects highlighted in the sources:

- **Scope and Diversity of Concepts:**
  
  Human describers utilize a wide range of concepts, from general algorithmic
  ones like loops and logic to domain-specific ones like flood-fill [1-4]. SEER
  needs to be able to recognize and interpret this diverse set of concepts.
  Coaching should focus on exposing SEER to a variety of concepts and their
  linguistic expressions within the context of puzzle descriptions.

- **Framing and Context Setting:**

  Describers often use framing statements to set up the problem and define
  objects that will be referred to later [5, 6]. This helps to establish a
  shared understanding between the describer and the builder. SEER should be
  trained to identify these framing statements and utilize them to build a
  coherent mental model of the puzzle. Coaching could involve providing SEER
  with examples of effective framing statements and their impact on the
  interpretation of the instructions.

- **Validation and Clarification:**

  Natural language programs often contain validation checks and clarifications
  to ensure precise interpretation [7]. SEER should be trained to recognize
  these elements and use them to verify its understanding of the instructions.
  Coaching could involve training SEER to identify potential ambiguities and to
  seek clarification when necessary. For example, prompting SEER with questions
  like, "Are there any parts of the instructions that could be interpreted in
  multiple ways?" could be beneficial.

- **Communicative Strategies Beyond Executable Code:** 

  Natural programs leverage various communicative strategies beyond directly
  executable procedures, such as examples, metaphors, and analogies [5, 8, 9].
  SEER should be equipped to handle these strategies to extract the full meaning
  of the instructions. Coaching should include exposure to diverse communicative
  styles and strategies used in puzzle descriptions.

- **Importance of Input-Output Examples:** 

  While language is crucial, input-output examples provide valuable grounding
  and validation for program synthesis [10, 11]. SEER should be trained to
  effectively utilize these examples in conjunction with the natural language
  instructions. Coaching could involve presenting SEER with tasks where it must
  infer the underlying program from both language and input-output examples.

