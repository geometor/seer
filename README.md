# SEER

![SEER](./seer_resized.png)

## Perception and Discernment for Abstraction and Reasoning Challenges

SEER is an AI-driven framework for finding functions to transform inputs to outputs from a set of training datra. It combines natural language understanding, visual reasoning, and code generation to identify patterns and develop algorithmic solutions.



### Key Features

- **Multi-role AI Collaboration**: Utilizes specialized roles ("dreamer" and "coder") to analyze problems and generate solutions
- **Structured Workflows**: Supports different problem-solving approaches (default and incremental)
- **Comprehensive Logging**: Records every step of the reasoning and solution process
- **Visualized Outputs**: Generates rich visual representations of puzzles and solutions
- **Code Generation**: Transforms natural language reasoning into executable Python code
- **Extensible Architecture**: Easily adaptable to different models and reasoning styles

## Architecture

SEER is built around a collaborative AI system where different roles analyze and solve puzzles:

1. **Dreamer**: Analyzes puzzle examples, identifies patterns, and describes transformations in natural language
2. **Coder**: Converts the dreamer's insights into executable code that solves the puzzles
3. **Workflows**: Orchestrate the interaction between roles (e.g., analyze all examples at once or incrementally)
4. **Session Management**: Records all interactions, solutions, and results for analysis

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│     Tasks       │     │      SEER       │     │     Session     │
│  (ARC Puzzles)  │────▶│  Orchestrator   │────▶│    Recording    │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                               ┌─┴─┐                      ▲
                               │   │                      │
                 ┌─────────────┘   └──────────┐          │
                 ▼                            ▼          │
        ┌─────────────────┐          ┌─────────────────┐ │
        │    Dreamer      │          │     Coder       │ │
        │ (Pattern Analysis) ◀───────▶ (Code Generation)│ │
        └─────────────────┘          └─────────────────┘ │
                 │                            │          │
                 └────────────────────────────┘          │
                               │                         │
                               ▼                         │
                  ┌─────────────────────────┐           │
                  │    Solution Testing     │───────────┘
                  │ (Verification & Scoring)│
                  └─────────────────────────┘
```

## Installation

### Prerequisites

- Python 3.7+
- Google API key for Gemini model access

### Standard Installation

```bash
# Clone the repository
git clone https://github.com/geometor/seer.git
cd seer

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install the package
pip install .
```

### Development Installation

```bash
# For development with editable install
pip install -e .
```

## Configuration

SEER requires a configuration directory with an `index.yaml` file that defines:

1. **API Keys**: Authentication for the AI models
2. **Roles**: Instructions and parameters for each AI role
3. **Workflows**: Settings for different problem-solving approaches
4. **Task Context**: Background information about the ARC challenge

Example configuration structure:
```
config/
├── index.yaml           # Main configuration file
├── instructions/        # Role-specific instructions
│   ├── dreamer.md
│   └── coder.md
└── context/             # Background information
    └── arc_context.md
```

Sample `index.yaml`:
```yaml
api_key: "your_gemini_api_key_here"
roles:
  dreamer:
    model: "gemini-1.5-pro"
    temperature: 0.2
    instructions: "instructions/dreamer.md"
  coder:
    model: "gemini-1.5-pro"
    temperature: 0.1
    instructions: "instructions/coder.md"
workflow: "default"  # or "incremental"
task_context: "context/arc_context.md"
max_iterations: 3
use_images: true
```

## Usage

### Running with the Library API

```python
from pathlib import Path
from geometor.seer import Seer
from geometor.seer.config import Config
from geometor.seer.tasks import Tasks

# Load configuration
config_dir = Path("./config")
config = Config(config_dir)

# Initialize Seer
seer_instance = Seer(config)

# Load tasks
tasks = Tasks("./tasks/ARCv2/training")
ordered_tasks = tasks.get_ordered_tasks()

# Run Seer on selected tasks
output_dir = Path("./seer_sessions/")
seer_instance.run(
    tasks=ordered_tasks[0:10],  # First 10 tasks
    output_dir=output_dir,
    description="ARC Training Tasks 0-10"
)
```

### Command-line Tools

Rebuild session indexes:
```bash
seer_rebuild_indexes --session_dir path/to/your/session/output
```

## Workflows

SEER supports multiple problem-solving approaches:

### Default Workflow

Analyzes all training examples simultaneously, then generates a solution.

### Incremental Workflow

Examines one example at a time, building up understanding progressively.

## Output Structure

SEER creates structured session outputs with detailed tracking of each step:
```
seer_sessions/
└── 25.101.1306/                           # Session directory (date-based)
    ├── index.json                         # Session metadata
    ├── 13e47133/                          # Task ID
    │   ├── index.json                     # Task metadata
    │   ├── task.png                       # Visual representation of the task
    │   ├── task.json                      # Task definition and metadata
    │   ├── 000/                           # Numbered step
    │   │   ├── code_00.yaml               # Code from this step
    │   │   ├── index.json                 # Step metadata
    │   │   ├── prompt_content.md          # Main prompt content
    │   │   ├── prompt_history.md          # Conversation history
    │   │   ├── prompt_instructions.md     # Instructions for the model
    │   │   ├── response.json              # Raw model response
    │   │   └── response.md                # Formatted model response
    │   ├── 001/
    │   │   ├── code_00.py                 # Generated Python code
    │   │   ├── code_00.py.trial.json      # Code trial results (JSON)
    │   │   ├── code_00.py.trial.png       # Visualization of trial
    │   │   ├── index.json                 # Step metadata
    │   │   ├── prompt_content.md
    │   │   ├── prompt_history.md
    │   │   ├── prompt_instructions.md
    │   │   ├── response.json
    │   │   └── response.md
    │   ├── 002/
    │   │   └── ...
    ├── summary.md                         # Task summary
    └── submission.json                    # Solutions for submissio
```

## Results Analysis

Session directories contain summarized results and metrics, including:
- Success rates by task
- Code performance analysis
- Visual comparisons of expected vs. generated outputs

## Contributing

Contributions are welcome! Please see our [GitHub issues](https://github.com/geometor/seer/issues) for ways to contribute.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

SEER is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [Abstraction and Reasoning Corpus (ARC)](https://github.com/fchollet/ARC)
- [Google Gemini API](https://ai.google.dev/)
- [Geometor Project](https://geometor.github.io/)
