# seer

The next generation of ARC challenge investigations.

![seer](./seer_resized.png)

**seer** is an artificial intelligence entity focused on perception and
discernment, building upon our previous work with the Abstraction and Reasoning
Corpus (ARC) challenge. 

It aims to provide a flexible and extensible framework for exploring geometric
reasoning and problem-solving, using multi-modal models capable of reasoning
and code execution (like Gemini). Key goals include understanding the nature
of problems, describing the problem-solving process in natural language, and
converting those descriptions into executable code.


## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/geometor/seer.git
    cd seer
    ```

2.  **Install the package:**
    It's recommended to install the package in a virtual environment.
    ```bash
    # Create and activate a virtual environment (example using venv)
    python -m venv .venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`

    # Install the package and its dependencies
    pip install .
    ```
    For development, you might prefer an editable install:
    ```bash
    pip install -e .
    ```

## Dependencies

**seer** requires Python 3.7+ and the following packages:

*   google-genai
*   google-api-core
*   google-generativeai
*   numpy
*   scipy
*   scikit-learn
*   pillow
*   rich
*   jinja2

These dependencies will be installed automatically when you install `geometor-seer` using pip.

## Usage

**seer** relies on a configuration directory that defines roles, instructions, and context for the AI models. See the `Config` class (`src/geometor/seer/config.py`) for details on the expected structure (e.g., an `index.yaml` file).

### Rebuilding Indexes (Command-Line)

The repository includes a script to rebuild summary indexes for session outputs:

```bash
seer_rebuild_indexes --session_dir path/to/your/session/output
```
Use `seer_rebuild_indexes --help` for more options.

### Running the Seer (Library Usage - Example)

While a primary command-line interface is under development, the core `Seer` orchestrator can be used as a library. Here's a basic conceptual example:

```python
from pathlib import Path
from geometor.seer import Seer
from geometor.seer.config import Config
from geometor.seer.tasks import Tasks # Or however tasks are loaded

# 1. Load Configuration
config_dir = Path("path/to/your/config")
config = Config(config_dir)

# 2. Load Tasks (Replace with actual task loading mechanism)
# Example: tasks = Tasks.load_from_some_source("path/to/tasks")
tasks_to_run = Tasks(...) # Load specific tasks you want to process

# 3. Initialize Seer
seer_instance = Seer(config)

# 4. Define Output Directory and Description
output_dir = Path("path/to/session/output")
session_description = "My first seer run"

# 5. Run the Seer process
seer_instance.run(
    tasks=tasks_to_run,
    output_dir=output_dir,
    description=session_description
)

print(f"Seer session finished. Output saved to: {output_dir}")
```
*(Note: You will need to adapt task loading and configuration paths based on your specific setup.)*

## Contributing

Contributions are welcome! Please see our [GitHub issues](https://github.com/geometor/seer/issues) for ways to contribute.

## License

**seer** is licensed under the MIT License. See the `LICENSE` file for more details.
