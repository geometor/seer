from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Any, Dict
import jinja2
from pathlib import Path

# Local application/library specific imports
# Need TaskStep for type hinting in _check_success_and_log
from geometor.seer.session.task_step import TaskStep

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
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
