# seer

The next generation of ARC challenge investigations.

![seer](./seer_resized.png)

**seer** is an artificial intelligence entity focused on perception and discernment, building upon our
previous work with the Abstraction and Reasoning Corpus (ARC) challenge. It aims
to provide a flexible and extensible framework for exploring geometric reasoning
and problem-solving.


- understand the nature of problem based on the context or requirements
- be able to describe the problem and the process through it in natural language
- convert natural langauge program to executable code
- facilitation and coaching


using multi-modal models capable of reasoning and code execution

Gemini

> the first task is not to reason
>
> it's to build a reasonable context

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

## Facilitation - Chain of Thought

> from Meta Chain of Thought paper
> https://arxiv.org/pdf/2501.04682

- Classical CoT Shortcomings: Standard CoT relies on prompting LLMs to generate a sequence of reasoning steps leading to a solution. However, for complex problems, LLMs often fail to produce coherent or accurate chains of thought. The paper argues that this is due to the implicit nature of CoT, where the underlying reasoning process remains unaddressed.
- Meta-CoT as a Generative Process: Meta-CoT views reasoning as a latent generative process. It posits that the final answer and CoT steps are jointly conditioned on this underlying process. This is illustrated with the example of the "windmill" problem from the International Mathematics Olympiad 2011.

### Bootstrapping

Bootstrapping in the context of machine learning, particularly with large language models (LLMs), is a technique for iteratively improving a model's reasoning abilities by **generating and refining its own training data**. The core idea is to leverage the model's existing capabilities to create synthetic examples that enhance its performance on tasks requiring complex reasoning.

Here's a breakdown of the bootstrapping process, as described in the sources:

1. **Initial Rationale Generation:** The model is prompted to generate rationales (step-by-step reasoning) and answers for a given set of questions. This initial data may contain errors or inconsistencies. 
2. **Filtering and Dataset Creation:** The generated rationales are filtered, retaining only those leading to correct answers. This filtered data, along with the corresponding questions and answers, forms a new dataset.
3. **Supervised Fine-tuning:** The model is then fine-tuned using this newly created dataset. This process helps the model learn from its successful reasoning attempts and refine its ability to generate accurate rationales. 
4. **Iteration:** Steps 1-3 are repeated over multiple iterations, with the model continuously generating, filtering, and learning from its own refined outputs. This iterative process allows the model to progressively improve its reasoning capabilities. 

The sources highlight two specific bootstrapping methods:

* **Self-Taught Reasoner (STaR):**  STaR focuses on training models to generate and refine rationales for complex reasoning tasks. It relies on a dataset of questions and answers, without requiring access to ground-truth rationales. 
* **Meta-STaR:** This method extends the STaR concept to the idea of Meta Chain-of-Thought (Meta-CoT), which involves explicitly modeling the underlying "thinking" process. Meta-STaR uses a base policy and search procedure to generate synthetic search data and trains the model to internalize these reasoning strategies.

The sources emphasize that bootstrapping is particularly relevant for **complex reasoning problems** where the true data-generating process is not readily available in existing datasets. By generating and refining its own training data, the model can learn to approximate this complex process and improve its performance on challenging reasoning tasks. 

### Oracle Verifier

An **oracle verifier**, in the context of the sources, refers to a method or system that can **definitively determine the correctness of a solution or reasoning process** without any uncertainty or ambiguity. It acts as a ground truth reference for evaluating the model's outputs.

Here's how the concept of an oracle verifier is discussed and utilized within the sources:

* **Evaluating Reasoning Steps and Solutions:** The sources mention the use of oracle verifiers in the context of **inference-time compute**, where the model is allowed to generate multiple candidate solutions, and the oracle verifier is used to select the correct one. This helps assess the model's reasoning ability beyond simply generating a single answer.
* **Training Process Reward Models (PRMs):** Oracle verifiers are crucial for **training PRMs**, which are models designed to estimate the quality or correctness of individual reasoning steps. By providing accurate feedback during training, the oracle verifier helps the PRM learn to distinguish between good and bad reasoning paths.
* **Generating Synthetic Training Data:** The sources describe using oracle verifiers in conjunction with search algorithms like Monte Carlo Tree Search (MCTS) and Astar to generate **synthetic training data** that includes both reasoning steps and associated correctness labels. This synthetic data is then used to train the LLM to perform more complex reasoning.

**Limitations and Alternatives:**

* **Computational Cost:** While highly accurate, using oracle verifiers for training can be **computationally expensive**, especially for complex problems that require extensive search or simulation.
* **Applicability to Open-Ended Problems:** Oracle verifiers are most effective for problems with **clearly defined solutions** that can be definitively verified. For open-ended tasks like proofs or scientific derivations, where multiple valid solutions might exist, relying solely on an oracle verifier may be limiting.

The sources explore **alternative approaches** to address these limitations, such as training PRMs using human annotations or leveraging **"generative verifiers"** that can provide more nuanced evaluations of reasoning chains.

### Reasoning Styles

The phrase "reasoning style" refers to the **observable patterns and characteristics in a language model's output when it attempts to solve reasoning problems.** While the sources do not explicitly define "reasoning style," they offer insights into how it manifests and the factors that influence it.

Here's an expanded explanation based on the sources and our previous conversation:

* **Explicit Instruction:** The sources show that prompting strategies explicitly designed to encourage specific reasoning behaviors significantly impact the model's output style. For instance, prompting a model to "think step-by-step" will likely result in a more structured and verbose output, even if the model doesn't possess a genuine understanding of the underlying reasoning process.
* **Mimicking Training Data:** Language models tend to replicate patterns observed in their training data. If a model is trained on data generated using a specific search algorithm (like MCTS), its output might exhibit characteristics similar to that algorithm, even when not explicitly instructed to do so. This suggests that the model's reasoning style can be influenced by the training data's inherent structure and characteristics.
* **Faking Mistakes:** The sources raise concerns about models potentially **"faking mistakes"** to match the desired reasoning style presented in the prompt or training data. This highlights a potential pitfall, where models might prioritize matching surface-level patterns over demonstrating true understanding or problem-solving ability.
* **Impact of Model Scale:** The scale of the language model also appears to influence its reasoning style. Larger models, when prompted to engage in meta-cognitive behaviors like self-correction, tend to exhibit those behaviors more frequently than smaller models. This suggests that larger models might be more capable of adapting their reasoning style based on instructions.

**Key Takeaway:**

"Reasoning style" is distinct from genuine reasoning ability. While prompting and training strategies can influence a model's output to resemble human-like reasoning, this doesn't necessarily guarantee that the model understands the underlying concepts or can generalize to new problems. The sources emphasize the need to distinguish between **superficial stylistic imitation** and **true reasoning proficiency** when evaluating language models.


## Dependencies

**seer** depends on the following Python packages:

TODO: read from pyproject.toml

## Contributing

Contributions are welcome! Please see our [GitHub issues](https://github.com/geometor/seer/issues) for ways to contribute.

## License

**seer** is licensed under the MIT License. See the `LICENSE` file for more details.
