from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geometor.seer.seer import Seer
    from geometor.seer.session import SessionTask
    from geometor.seer.tasks import Task


class WorkflowBase(ABC):
    """Abstract base class for different task-solving workflows."""

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
