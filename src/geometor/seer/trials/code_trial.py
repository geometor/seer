from geometor.seer.trials import verifier
from geometor.seer.tasks.tasks import Task


class CodeTrial:
    """
    trial for one code and task
    """
    def __init__(
        self,
        task_step,
        code_filename: str,
        code,
        task: Task,
    ):
        #  self.task_step = task_step
        self.code_filename = code_filename
        self.code = code
        self.task = task
        self.train_results = None  # Initialize
        self.test_results = None   # Initialize
        self.task_step = task_step # store

    def execute_and_save_results(self):
        """Executes the trial and saves results (image and JSON)."""
        self.train_results = self.run_trial(self.code, self.task.train)
        self.test_results = []

        if self.train_passed:
            self.test_results = self.run_trial(self.code, self.task.test)

        show_test = bool(self.test_results)
        results_image = self.task.to_image(
            train_results=self.train_results,
            test_results=self.test_results,
            show_test=show_test,
        )
        png_file = self.task_step.dir / f"{self.code_filename}.trial.png"
        results_image.save(png_file)

        json_file = self.code_filename + ".trial.json"
        results_json = {
            "train": self.train_results,
            "test": self.test_results,
        }
        self.task_step._write_to_json(json_file, results_json)


    def run_trial(self, code, task_pairs) -> dict:

        code_results = verifier.test_code_with_timeout(
            code,
            task_pairs,
        )

        return code_results  # return the results

    @property
    def train_passed(self) -> bool:
        return self.train_results and all(
            r.get("match", False) for r in self.train_results.get("trials", [])
        )

    @property
    def test_passed(self) -> bool:
        return self.test_results and all(
            r.get("match", False) for r in self.test_results.get("trials", [])
        )

    def generate_report(self) -> str:
        report = f"Results for {self.code_filename}:\n"

        if self.train_results:
            report += "\nTrain Set Results:\n"
            for i, result in enumerate(self.train_results.get("trials", [])):
                report += f"\n## Example {i+1}:\n"
                report += f"Input:\n```\n{result.get('input')}\n```\n"
                report += (
                    f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"
                )
                if "transformed_output" in result:
                    report += f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    # Add images - construct filename based on task and step
                    image_filename = f"{self.task.id}-{i+1}.png"  # simplified name
                    report += f"![Transformed Image]({image_filename})\n"

                report += f"match: {result.get('match')}\n"
                report += f"pixels_off: {result.get('pixels_off')}\n"
                report += f"size_correct: {result.get('size_correct')}\n"
                report += (
                    f"color_palette_correct: {result.get('color_palette_correct')}\n"
                )
                report += (
                    f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"
                )

        if self.test_results:
            report += "\nTest Set Results:\n"
            # ... (Similar formatting for test results, if available) ...
            for i, result in enumerate(self.test_results.get("trials", [])):
                report += f"\n## Example {i+1}:\n"
                report += f"Input:\n```\n{result.get('input')}\n```\n"
                if "transformed_output" in result:
                    report += f"Transformed Output:\n```\n{result.get('transformed_output')}\n```\n"
                    # Add images - construct filename based on task and step
                    image_filename = f"{self.task.id}-{i+1}.png"  # simplified name
                    report += f"![Transformed Image]({image_filename})\n"
                if result.get("expected_output"):
                    report += (
                        f"Expected Output:\n```\n{result.get('expected_output')}\n```\n"
                    )

                report += f"match: {result.get('match')}\n"
                report += f"pixels_off: {result.get('pixels_off')}\n"
                report += f"size_correct: {result.get('size_correct')}\n"
                report += (
                    f"color_palette_correct: {result.get('color_palette_correct')}\n"
                )
                report += (
                    f"correct_pixel_counts: {result.get('correct_pixel_counts')}\n"
                )

        return report
