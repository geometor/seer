import ast
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Any, Dict
import jinja2
from pathlib import Path

# Local application/library specific imports
# Need TaskStep for type hinting in _check_success_and_log
from geometor.seer.session.task_step import TaskStep
from geometor.seer.trials.code_trial import CodeTrial # Import CodeTrial

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask # Import SessionTask
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task


class WorkflowBase(ABC):
    """Abstract base class for different task-solving workflows."""

    def __init__(self, package_name: str, template_dir: str = "templates"):
        """
        Initializes the base workflow and sets up the Jinja2 environment.

        Args:
            package_name: The name of the package containing the templates
                          (e.g., "geometor.seer.workflows.default").
            template_dir: The subdirectory within the package where templates are stored.
        """
        super().__init__()
        try:
            self.jinja_env = jinja2.Environment(
                loader=jinja2.PackageLoader(package_name, template_dir),
                autoescape=False,  # We are generating text/code, not HTML
            )
        except Exception as e:
            # Catch potential errors during Jinja setup (e.g., package not found)
            raise RuntimeError(f"Failed to initialize Jinja2 environment for {package_name}: {e}") from e

    def _render_template(self, template_name: str, context: Dict[str, Any] = None) -> str:
        """Loads and renders a Jinja2 template."""
        if context is None:
            context = {}
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(context)
        except jinja2.TemplateNotFound:
            # Provide more context in the error message
            raise FileNotFoundError(
                f"Workflow template '{template_name}' not found in package '{self.jinja_env.loader.package_path}'"
            )
        except Exception as e:
            raise RuntimeError(f"Error rendering template {template_name}: {e}") from e

    def _check_success_and_log(self, task_step: TaskStep, step_name: str) -> bool:
        """Checks if a step was successful and logs appropriately."""
        # Check if *any* trial within this step passed train
        train_passed = task_step.any_trials_successful("train")

        # Handle the case where trials might not have run or produced results
        if train_passed is None:
            # print(f"            Step '{step_name}': train status unknown (no successful trials or trials not run).")
            return False # Treat unknown as not passed for success checking

        elif train_passed:
            print(f"            train: passed")
            # Check test pass status only if train passed
            test_passed = task_step.any_trials_successful("test")
            if test_passed is None:
                # print(f"            Step '{step_name}': test status unknown.")
                pass # Don't log anything specific for unknown test status
            elif test_passed:
                print(f"            test: passed")
            else:
                # print(f"            Step '{step_name}': test failed")
                pass # Don't log test failed if train passed, focus is on train success
            return True  # Training passed, signal success for this step check

        else: # train_passed is False
            #  print(f"            Step '{step_name}': train failed")
            return False

    def _extract_docstring_from_code(self, code: str) -> str | None:
        """
        Parses the Python code string and extracts the module-level docstring.

        Args:
            code: The Python code as a string.

        Returns:
            The module-level docstring, or None if not found or parsing fails.
        """
        try:
            tree = ast.parse(code)
            return ast.get_docstring(tree)
        except SyntaxError:
            # Handle cases where the code might not be valid Python
            print("        Warning: Could not parse code to extract docstring due to SyntaxError.")
            # Fallback: Try a simpler string search for """ or ''' at the beginning
            code_stripped = code.strip()
            if code_stripped.startswith('"""'):
                end_marker = '"""'
                start_pos = 3
            elif code_stripped.startswith("'''"):
                end_marker = "'''"
                start_pos = 3
            else:
                return None # No clear docstring marker at the start

            end_pos = code_stripped.find(end_marker, start_pos)
            if end_pos != -1:
                return code_stripped[start_pos:end_pos].strip()
            else:
                # Docstring started but wasn't properly closed?
                print("        Warning: Found docstring start marker but no end marker.")
                return None
        except Exception as e:
            print(f"        Warning: Unexpected error extracting docstring: {e}")
            return None


    def _review_test_inputs(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any],
        code_trial: CodeTrial, # Pass the whole trial
    ) -> TaskStep:
        """Handles the 'review test inputs' step using the oracle role."""
        title = "review • oracle • test inputs"

        if not code_trial or not code_trial.code:
             raise ValueError("Cannot review test inputs: Invalid CodeTrial provided.")

        # Extract docstring (NL program) from the code
        natural_language_program = self._extract_docstring_from_code(code_trial.code)
        if not natural_language_program:
            # Log or raise? Let's raise for now, as it's critical input.
            raise ValueError("Cannot review test inputs: Failed to extract docstring from code.")

        # Prepare content for the template
        context = {
            "code": code_trial.code,
            "natural_language_program": natural_language_program,
            "train_pairs": task.train,
            "test_pairs": task.test,
            "use_images": seer_instance.use_images,
        }
        content_text = self._render_template("review_test_inputs.j2", context)
        content = [content_text] # Start with rendered text

        # Add images if use_images is true (Jinja template handles text/code part)
        # Note: This duplicates image sending if they were already in history,
        # but ensures the oracle sees them directly with this prompt.
        if seer_instance.use_images:
             image_content = []
             for pair in task.train:
                 image_content.append(pair.input.to_image())
             for pair in task.test:
                 image_content.append(pair.input.to_image())
             # Prepend image content to ensure it's processed first by model if needed
             content = image_content + content


        # Instructions are embedded within the rendered content_text
        instructions = [""] # No separate instructions needed

        try:
            task_step = seer_instance._generate(
                session_task,
                "oracle",     # Use the oracle role
                title,
                history,      # Pass existing history
                content,      # Pass rendered template + images
                instructions, # Empty instructions
                # No tools needed for oracle by default
            )
            # No trials run here, this step produces analysis/NL program
            task_step.summarize() # Summarize the oracle step itself
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            # Log error on the step itself if possible?
            # task_step.log_error(e, f"Failed during oracle review step") # Requires task_step to exist
            raise # Re-raise to be caught by the main execute loop

    def _generate_final_code(
        self,
        session_task: "SessionTask",
        task: "Task",
        seer_instance: "Seer",
        history: List[Any], # History includes oracle's output
    ) -> TaskStep:
        """Handles the final coder step after test input review."""
        title = "generate • coder • final code"

        # Content is empty; coder works from history (including oracle's refined NL)
        content = [""]

        # Use the standard coder refinement template
        # This template expects the NL program to be in the history.
        # The oracle's response should contain the "Updated Natural Language Program".
        instruction_text = self._render_template("refine_coder.j2", {})
        instructions = [instruction_text]

        try:
            task_step = seer_instance._generate(
                session_task,
                "coder",
                title,
                history,      # Pass history including oracle's output
                content,      # Pass empty content
                instructions, # Pass rendered template as instructions
            )
            # Trials *will* be run on this step's output later in the execute flow
            task_step.summarize() # Summarize the coder step
            return task_step
        except Exception as e:
            print(f"            ERROR in step '{title}': {e}")
            raise


    @abstractmethod
    def execute(
        self, session_task: "SessionTask", task: "Task", seer_instance: "Seer"
    ) -> None:
        """
        Executes the specific workflow to solve the given task.

        Args:
            session_task: The session task object for logging and context.
            task: The task data.
            seer_instance: The main Seer instance to access shared resources
                           (e.g., _generate, config, roles, instructions).
        """
        pass
