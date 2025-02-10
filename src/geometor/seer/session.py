from pathlib import Path
from datetime import datetime
import json

from geometor.seer.seer import Seer


class Session:
    def __init__(self, config: dict, tasks: list):
        self.config = config
        self.tasks = tasks

        self.output_dir = Path(config["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.timestamp = datetime.now().strftime("%y.%j.%H%M%S")  # Generate timestamp

        self.session_dir = self.output_dir / self.timestamp
        self.session_dir.mkdir(parents=True, exist_ok=True)

        # Write system and task context to files
        self._write_context_files(config["system_context_file"], config["task_context_file"])

        self.image_registry = {}

        self.seer = Seer(
            config=config,
            session=self,
        )

        # Log the configuration
        with open(self.session_dir / "config.json", "w") as f:
            json.dump(config, f, indent=2)

    def _write_context_files(self, system_context_file: str, task_context_file: str):
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

    def save_grid_image(self, grid_image, prompt_count: int, context: str) -> Path:
        """
        Save a grid image with deduplication.
        """
        # Use image content as key for deduplication
        image_bytes = grid_image.tobytes()

        if image_bytes in self.image_registry:
            return self.image_registry[image_bytes]

        # Create new file if image hasn't been saved before
        filename = f"{prompt_count:03d}-{context}.png"
        image_path = self.task_dir / filename
        grid_image.save(image_path)

        # Store relative path for RST references
        rel_path = image_path.relative_to(self.task_dir)
        self.image_registry[image_bytes] = rel_path

        return rel_path

    def log_prompt(self, prompt: list, instructions: list, prompt_count: int, description: str = ""):
        prompt_file = self.task_dir / f"{prompt_count:03d}-prompt.md"
        with open(prompt_file, "w") as f:
            f.write(f"[{datetime.now().isoformat()}] PROMPT: ")
            if description:
                f.write(f"Description: {description}\n")
            f.write("-" * 80)
            f.write("\n")
            for part in prompt:
                f.write(str(part))
            f.write("\n")
            f.write("=" * 80)
            f.write("\n")
            for part in instructions:
                f.write(str(part))
            f.write("\n")

    def log_response(self, response, prompt_count: int):
        response_start = datetime.now()  # Capture start time
        response_file = self.task_dir / f"{prompt_count:03d}-response.json"

        # Get token counts and update totals
        metadata = response.to_dict().get("usage_metadata", {})
        self.seer.token_counts["prompt"] += metadata.get("prompt_token_count", 0)
        self.seer.token_counts["candidates"] += metadata.get("candidates_token_count", 0)
        self.seer.token_counts["total"] += metadata.get("total_token_count", 0)
        self.seer.token_counts["cached"] += metadata.get("cached_content_token_count", 0)

        response_end = datetime.now()  # Capture end time
        response_time = (response_end - response_start).total_seconds()
        total_elapsed = (response_end - self.seer.start_time).total_seconds()
        self.seer.response_times.append(response_time)

        # Prepare the response data dictionary
        response_data = response.to_dict()
        response_data["token_totals"] = self.seer.token_counts.copy()
        response_data["timing"] = {
            "response_time": response_time,
            "total_elapsed": total_elapsed,
            "response_times": self.seer.response_times.copy(),
        }

        with open(response_file, "w") as f:
            json.dump(response_data, f, indent=2)

        # Unpack the response and write elements to a markdown file
        response_md_file = self.task_dir / f"{prompt_count:03d}-response.md"
        with open(response_md_file, "w") as f:
            f.write(f"[{datetime.now().isoformat()}] RESPONSE:\n")
            f.write("-" * 80 + "\n")

            if "candidates" in response_:
                for candidate in response_data["candidates"]:
                    if "content" in candidate:
                        if "parts" in candidate["content"]:
                            for part in candidate["content"]["parts"]:
                                if "text" in part:
                                    f.write(part["text"] + "\n")
                                if "function_call" in part:
                                    f.write("Function Call:\n")
                                    f.write(
                                        f"`{part['function_call']['name']}({json.dumps(part['function_call']['args'])})`\n"
                                    )
                                if "executable_code" in part:
                                    f.write("Executable Code:\n")
                                    f.write(f"```python\n{part['executable_code']['code']}\n```\n")
                                if "code_execution_result" in part:
                                    f.write("Code Execution Result:\n")
                                    f.write(f"Outcome: {part['code_execution_result']['outcome']}\n")
                                    f.write(f"```\n{part['code_execution_result']['output']}\n```\n")

            f.write("\n")

            # Include token totals and timing information
            if "token_totals" in response_:
                f.write("Token Totals:\n")
                f.write(f"  Prompt: {response_data['token_totals']['prompt']}\n")
                f.write(f"  Candidates: {response_data['token_totals']['candidates']}\n")
                f.write(f"  Total: {response_data['token_totals']['total']}\n")
                f.write(f"  Cached: {response_data['token_totals']['cached']}\n")
            if "timing" in response_:
                f.write("Timing:\n")
                f.write(f"  Response Time: {response_data['timing']['response_time']}s\n")
                f.write(f"  Total Elapsed: {response_data['timing']['total_elapsed']}s\n")

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
            f.write(f"[{datetime.now().isoformat()}] ERROR: {error_message}\n")
            if context:
                f.write(f"Context: {context}\n")
            f.write("\n")
