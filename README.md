# seer

The next generation of ARC challenge investigations.

![seer](./seer_resized.png)

**seer** is a project focused on perception and discernment, building upon our previous work with the Abstraction and Reasoning Corpus (ARC) challenge. It aims to provide a flexible and extensible framework for exploring geometric reasoning and problem-solving.

## Features

*   **Abstraction and Reasoning:** Tools for analyzing and understanding abstract patterns and relationships.
*   **Geometric Perception:** Capabilities for perceiving and interpreting geometric structures.
*   **Extensible Framework:** A modular design that allows for easy addition of new features and algorithms.
*   **Integration with LLMs:** Designed to work with Large Language Models for enhanced reasoning and problem-solving.

## Installation

You can install **seer** using pip:

```bash
   pip install geometor-seer
```

## Usage

```python
   from rich import print
   from datetime import datetime
   from pathlib import Path
   import json
   import os

   from geometor.seer.app import Seer


   def run():
       seer = Seer()
       print(f"Seer initialized")


   if __name__ == "__main__":
       run()
```

TODO: list arguments and usage examples

## Dependencies

**seer** depends on the following Python packages:

TODO: read from pyproject.toml

## Contributing

Contributions are welcome! Please see our [GitHub issues](https://github.com/geometor/seer/issues) for ways to contribute.

## License

**seer** is licensed under the MIT License. See the `LICENSE` file for more details.
