from __future__ import annotations
from typing import TYPE_CHECKING

from geometor.seer.session.level import Level

if TYPE_CHECKING:
    from geometor.seer.session import Session
    from geometor.seer.tasks.tasks import Task


class SessionTask(Level):
    def __init__(self, session: Session, task: Task):
        super().__init__(session, task.id)
        self.session = session  # parent
        self.task = task
        self.steps = []

        try:
            task_image = task.to_image()
            image_path = self.dir / "task.png"
            task_image.save(image_path)

            task_json_str = task.nice_json_layout()
            self._write_to_file("task.json", task_json_str)

        except Exception as e:
            self.log_error(e)

        print(f"    {task.id}")

    def summarize(self):
        summary = super().summarize()
        summary.update(
            {
                "steps": len(self.steps),
                "trials": None,  # Filled in by TaskStep
                "matches": None,  # Filled in by TaskStep
                "train_passed": self.train_passed,  # Add here
                "test_passed": self.test_passed,  # Add here
            }
        )
        self._write_to_json("task_summary.json", summary)

    def add_step(self, title, history, prompt, instructions):
        from geometor.seer.session import TaskStep

        task_step = TaskStep(title, history, prompt, instructions, self)
        self.steps.append(task_step)
        return task_step

    @property
    def train_passed(self):
        return any(step.train_passed for step in self.steps)

    @property
    def test_passed(self):
        return any(step.test_passed for step in self.steps)

