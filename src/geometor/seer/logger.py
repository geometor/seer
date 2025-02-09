from datetime import datetime
from pathlib import Path
import json
from m2r2 import convert
from jinja2 import Environment, PackageLoader


class Indexer:
    """
    Manages the creation and updating of session, puzzle, and main index files.
    """

    def __init__(self, output_dir: str, puzzle_id: str, timestamp: str):
        self.output_dir = Path(output_dir)
        self.puzzle_id = puzzle_id
        self.timestamp = timestamp

        # Ensure required directories exist
        self._ensure_directory_structure()

        # Set up Jinja environment
        self.env = Environment(
            loader=PackageLoader("geometor.arcprize.solvers", "templates"),
        )

    def _ensure_directory_structure(self):
        """Create required directories if they don't exist."""
        self.sessions_dir = self.output_dir / "sessions"
        self.session_dir = self.sessions_dir / self.timestamp
        self.puzzle_dir = self.session_dir / self.puzzle_id

        self.sessions_dir.mkdir(parents=True, exist_ok=True)
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self.puzzle_dir.mkdir(parents=True, exist_ok=True)
        (self.puzzle_dir / "_images").mkdir(parents=True, exist_ok=True)
        (self.puzzle_dir / "_responses").mkdir(parents=True, exist_ok=True)

    def update_session_results(self):
        """Generate and update session results summary."""
        puzzles = []

        for puzzle_dir in sorted(self.session_dir.iterdir()):
            if puzzle_dir.is_dir():
                puzzle_data = {
                    "id": puzzle_dir.name,
                    "submitted": False,
                    "size_correct": "",
                    "colors_correct": "",
                    "color_diff": "",
                    "pixel_accuracy": "",
                }

                # Look for submission files
                submission_files = list(puzzle_dir.glob("*-submission.rst"))
                if submission_files:
                    puzzle_data["submitted"] = True
                    with open(submission_files[0]) as f:
                        content = f.read()

                        # Extract metrics using regex
                        import re

                        size_match = re.search(r":Size Correct: (True|False)", content)
                        colors_match = re.search(
                            r":Colors Correct: (True|False)", content
                        )
                        diff_match = re.search(
                            r":Unique Color Count Diff: (\{.*?\})", content
                        )
                        accuracy_match = re.search(
                            r":Pixel Accuracy: ([\d\.]+)%", content
                        )

                        puzzle_data.update(
                            {
                                "size_correct": size_match.group(1)
                                if size_match
                                else "",
                                "colors_correct": colors_match.group(1)
                                if colors_match
                                else "",
                                "color_diff": diff_match.group(1) if diff_match else "",
                                "pixel_accuracy": f"{accuracy_match.group(1)}%"
                                if accuracy_match
                                else "",
                            }
                        )

                puzzles.append(puzzle_data)

        # Render template
        template = self.env.get_template("session_results.j2")
        content = template.render(
            title=f"Session Results: {self.timestamp}", puzzles=puzzles
        )

        # Write results file
        results_path = self.session_dir / "results.rst"
        with open(results_path, "w") as f:
            f.write(content)

    def update_indices(self):
        """Update all indices including results summary."""
        self._write_sessions_index()
        self._write_session_index()
        self._write_puzzle_index()
        self.update_session_results()

    def _write_sessions_index(self):
        """Regenerate the main sessions index using Jinja2."""
        index_path = self.sessions_dir / "index.rst"
        template = self.env.get_template("sessions_index.j2")
        session_list = [
            {"session_name": session_dir.name}
            for session_dir in sorted(self.sessions_dir.iterdir())
            if session_dir.is_dir()
        ]
        content = template.render(title="sessions", sessions=session_list)

        with open(index_path, "w") as f:
            f.write(content)

    def _write_session_index(self):
        """Regenerate the session index using Jinja2."""
        index_path = self.session_dir / "index.rst"
        puzzle_list = []
        total_time = 0
        total_tokens = 0
        total_steps = 0

        for puzzle_dir in sorted(self.session_dir.iterdir()):
            if puzzle_dir.is_dir():
                puzzle_id = puzzle_dir.name
                response_dir = puzzle_dir / "_responses"

                if response_dir.exists():
                    responses = sorted(response_dir.glob("*-response.json"))
                    steps = len(responses)
                    time = sum(
                        json.load(open(resp_file))
                        .get("timing", {})
                        .get("response_time", 0)
                        for resp_file in responses
                    )
                    tokens = (
                        json.load(open(responses[-1]))
                        .get("token_totals", {})
                        .get("total", 0)
                        if responses
                        else 0
                    )

                    puzzle_list.append(
                        {
                            "puzzle_id": puzzle_id,
                            "steps": steps,
                            "total_time": f"{time:.2f}s",
                            "total_tokens": f"{tokens:,}",
                        }
                    )

                    total_steps += steps
                    total_time += time
                    total_tokens += tokens

        template = self.env.get_template("session_index.j2")
        content = template.render(
            title=f"{self.timestamp}",
            puzzles=puzzle_list,
            total_steps=total_steps,
            total_time=f"{total_time:.2f}s",
            total_tokens=f"{total_tokens:,}",
        )

        with open(index_path, "w") as f:
            f.write(content)

    def _write_puzzle_index(self):
        """Regenerate the puzzle index using Jinja2."""
        index_path = self.puzzle_dir / "index.rst"
        prompt_files = sorted(self.puzzle_dir.glob("[0-9][0-9][0-9]-prompt.rst"))
        submission_files = sorted(self.puzzle_dir.glob("*-submission.rst"))
        steps = []
        total_response_time = 0
        total_tokens = 0

        # Extract step details from prompt and response files
        for prompt_file in prompt_files:
            call_num = prompt_file.stem[:3]
            response_file = self.puzzle_dir / "_responses" / f"{call_num}-response.json"

            if response_file.exists():
                response_data = json.load(open(response_file))
                response_time = response_data.get("timing", {}).get("response_time", 0)
                token_data = response_data.get("token_totals", {}).get("total", 0)
                total_response_time += response_time
                total_tokens += token_data

                # Get description from the prompt file
                with open(prompt_file) as f:
                    content = f.read()
                    description = next(
                        (
                            line.split(":description:")[1].strip()
                            for line in content.split("\n")
                            if line.startswith(":description:")
                        ),
                        "Step",
                    )

                # Append step details for rendering
                steps.append(
                    {
                        "call_num": call_num,
                        "description": description,
                        "response_time": f"{response_time:.2f}s",
                        "tokens_used": f"{token_data:,}",
                    }
                )

        # Add submission entries to the steps list if submission files exist
        for submission_file in submission_files:
            submission_call_num = submission_file.stem.split("-")[0]
            steps.append(
                {
                    "call_num": submission_call_num,
                    "description": "evaluation",
                    "response_time": "N/A",
                    "tokens_used": "N/A",
                }
            )

        # Use Jinja template to render the index content
        template = self.env.get_template("puzzle_index.j2")
        content = template.render(
            title=f"{self.puzzle_id}",
            steps=steps,
            total_response_time=f"{total_response_time:.2f}s",
            total_tokens=f"{total_tokens:,}",
        )

        # Write the rendered content to the index file
        with open(index_path, "w") as f:
            f.write(content)

        # Append toctree entries to include all steps, including the final submission(s)
        with open(index_path, "a") as f:
            f.write("\n.. toctree::\n   :hidden:\n   :maxdepth: 1\n\n")
            for step in steps:
                if "evaluation" in step["description"]:
                    f.write(f"   {step['call_num']}-submission\n")
                #  else:
                #  f.write(f"   {step['call_num']}-prompt\n")


class Logger:
    def __init__(self, output_dir: str, puzzle_id: str, timestamp: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.puzzle_id = puzzle_id
        self.timestamp = timestamp

        self._ensure_directory_structure()

        self.indexer = Indexer(output_dir, puzzle_id, timestamp)
        self.image_registry = {}

    def _ensure_directory_structure(self):
        """Create required directories if they don't exist."""
        # Setup directory structure
        self.sessions_dir = self.output_dir / "sessions"
        self.sessions_dir.mkdir(parents=True, exist_ok=True)

        self.session_dir = self.sessions_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self.puzzle_dir = self.session_dir / self.puzzle_id
        self.images_dir = self.puzzle_dir / "_images"
        self.responses_dir = self.puzzle_dir / "_responses"

        self.puzzle_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.responses_dir.mkdir(parents=True, exist_ok=True)

    def save_response(self, response: dict, call_count: int):
        """Save raw response data as JSON."""
        response_file = self.responses_dir / f"{call_count:03d}-response.json"

        with open(response_file, "w") as f:
            json.dump(response, f, indent=2)

        self.indexer.update_indices()

    def save_grid_image(self, grid_image, call_count: int, context: str) -> Path:
        """
        Save a grid image with deduplication.

        parameters
        ----------
        grid_image :
            PIL Image to save
        call_count :
            Current call number
        context :
            Image context (e.g., 'example_1_input', 'working')

        returns
        -------
        rel_path : Path
            Relative path to the image file
        """
        # Use image content as key for deduplication
        image_bytes = grid_image.tobytes()

        if image_bytes in self.image_registry:
            return self.image_registry[image_bytes]

        # Create new file if image hasn't been saved before
        filename = f"{call_count:03d}-{context}.png"
        image_path = self.images_dir / filename
        grid_image.save(image_path)

        # Store relative path for RST references
        rel_path = image_path.relative_to(self.puzzle_dir)
        self.image_registry[image_bytes] = rel_path

        #  self.indexer.update_indices()
        return rel_path

    def write_rst_log(
        self,
        log_list: list,
        log_type: str,
        call_count: int,
        usage_data=None,
        description="",
    ):
        """Write log as RST file and handle any images.

        parameters
        ----------
        log_list : list
            The list of log content parts (strings, images, etc.)
        log_type : str
            The type of log (e.g., "prompt", "response")
        call_count : int
            The call count for naming the log file
        usage_data : dict, optional
            Data related to model usage (e.g., token counts, timing)
        """
        # Prepare data for the template
        parts = []
        for part in log_list:
            if isinstance(part, str):
                if part.startswith("[["):  # Grid display - preserve as code block
                    parts.append({"type": "code", "content": part})
                else:
                    try:
                        # Convert markdown to RST
                        rst_content = convert(part, escape_html=True)
                        parts.append({"type": "markdown", "content": rst_content})
                    except Exception as e:
                        print(f"Warning: Markdown conversion failed: {str(e)}")
                        parts.append({"type": "markdown", "content": part})

            elif hasattr(part, "save"):  # PIL Image object
                rel_path = self.save_grid_image(
                    part, call_count, f"grid_{len(self.image_registry)}"
                )
                parts.append({"type": "image", "path": str(rel_path)})

            else:
                parts.append({"type": "unknown", "content": f"[{type(part).__name__}]"})

        # Prepare usage data for the template
        timing = None
        token_usage = []

        if usage_data:
            if "timing" in usage_data:
                timing = usage_data["timing"]

            if "current" in usage_data and "totals" in usage_data:
                current = usage_data["current"]
                totals = usage_data["totals"]
                token_usage = [
                    {
                        "label": "Prompt",
                        "current": current["prompt_token_count"],
                        "total": totals["prompt"],
                    },
                    {
                        "label": "Response",
                        "current": current["candidates_token_count"],
                        "total": totals["candidates"],
                    },
                    {
                        "label": "Total",
                        "current": current["total_token_count"],
                        "total": totals["total"],
                    },
                    {
                        "label": "Cached",
                        "current": current["cached_content_token_count"],
                        "total": totals["cached"],
                    },
                ]

        # Render the content with Jinja2
        template = self.indexer.env.get_template("log_entry.j2")
        title = f"{call_count:03d} • {log_type.title()}"
        content = template.render(
            puzzle_id=self.puzzle_id,
            timestamp=self.timestamp,
            call_count=call_count,
            title=title,
            log_list=parts,
            usage_data=usage_data,
            timing=timing,
            token_usage=token_usage,
            description=description,
        )

        # Write the rendered content to the file
        log_file = self.puzzle_dir / f"{call_count:03d}-{log_type}.rst"
        with open(log_file, "w") as f:
            f.write(content)

        # Update indices after writing the log
        self.indexer.update_indices()

    def _get_image_count(self, call_count: int) -> int:
        """
        Get the next available image number for this call.

        parameters
        ----------

        """
        pattern = f"{call_count:03d}-*.png"
        existing_images = list(self.images_dir.glob(pattern))
        return len(existing_images) + 1

    def _add_navigation_links(self, file, log_type: str, call_count: int):
        """Add appropriate navigation links based on log type."""
        file.write("\n.. seealso::\n\n")
        if log_type == "prompt":
            file.write(f"   - :doc:`{call_count:03d}-history`\n")
            file.write(f"   - :doc:`{call_count:03d}-response`\n\n")
        elif log_type == "response":
            file.write(f"   - :doc:`{call_count:03d}-history`\n")
            file.write(f"   - :doc:`{call_count:03d}-prompt`\n\n")
        elif log_type == "history":
            file.write(f"   - :doc:`{call_count:03d}-prompt`\n")
            file.write(f"   - :doc:`{call_count:03d}-response`\n\n")

    def log_error(self, error_message: str, context: str = ""):
        """Log an error message to a file.

        parameters
        ----------
        error_message : str
            The error message to be logged.
        context : str
            Additional context or history information to provide.

        """
        error_log_file = self.session_dir / "error_log.txt"
        with open(error_log_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] ERROR: {error_message}")
            if context:
                f.write(f"Context: {context}")
            f.write(" ")
