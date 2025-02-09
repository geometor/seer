from pathlib import Path
from datetime import datetime
import json

from geometor.seer.seer import Seer
#  from markdown2 import convert


class Session:
    def __init__(self, config: dict, tasks: list):
        self.config = config
        self.tasks = tasks

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M%S") # Generate timestamp

        self.session_dir = self.output_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)

        # Write system and task context to files
        self._write_context_files(config["system_context_file"], config["task_context_file"])

        #  self.images_dir = self.task_dir / "_images"
        #  self.images_dir.mkdir(parents=True, exist_ok=True)
        #  self.responses_dir = self.task_dir / "_responses"
        #  self.responses_dir.mkdir(parents=True, exist_ok=True)

        self.image_registry = {}

        self.seer = Seer(
            config=config,
            session=self,
        )

    def _write_context_files(self, system_context_file: str, task_context_file: str):
        """Write system and task context to files in the session directory."""
        with open(system_context_file, "r") as f:
            system_context = f.read().strip()
        with open(task_context_file, "r") as f:
            task_context = f.read().strip()

        (self.session_dir / "system_context.md").write_text(system_context)
        (self.session_dir / "task_context.md").write_text(task_context)

    def run(self):

        for task in self.tasks.puzzles:
            self.task_dir = self.session_dir / task.id
            self.task_dir.mkdir(parents=True, exist_ok=True)
            self.seer.solve_task(task)


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
        image_path = self.task_dir / filename
        grid_image.save(image_path)

        # Store relative path for RST references
        rel_path = image_path.relative_to(self.task_dir)
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
            task_id=self.task_id,
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
        log_file = self.task_dir / f"{call_count:03d}-{log_type}.rst"
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
