"""
summary report functions
"""
import json
from rich.markdown import Markdown
from rich.table import Table
from rich.console import Console


def summarize_session(session_dir, log_error, display_response):
    """
    Creates a session-level summary report by aggregating task summary reports.
    """
    session_summary_data = []

    # Iterate through each task directory
    for task_dir in session_dir.iterdir():
        if task_dir.is_dir():
            summary_report_json_path = task_dir / "summary_report.json"
            if summary_report_json_path.exists():
                try:
                    with open(summary_report_json_path, "r") as f:
                        task_summary = json.load(f)
                        task_id = task_dir.name

                        # Calculate task totals
                        task_total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
                        task_total_response_time = 0
                        for response in task_summary.get("response_report", []):
                            for key in task_total_tokens:
                                task_total_tokens[key] += response["token_usage"].get(key, 0)
                            task_total_response_time += response["timing"]["response_time"]

                        # Aggregate data into a single dictionary
                        session_summary_data.append(
                            {
                                "task_id": task_id,
                                "total_tokens": task_total_tokens,
                                "total_response_time": task_total_response_time,
                                "test_report": task_summary.get("test_report", {}),  # Keep test report for drill-down if needed
                            }
                        )
                except (IOError, json.JSONDecodeError) as e:
                    print(
                        f"Error reading or parsing {summary_report_json_path}: {e}"
                    )
                    log_error(
                        f"Error reading or parsing {summary_report_json_path}: {e}"
                    )

    summary_table = _create_session_summary_table(session_summary_data)

    console = Console(record=True)
    console.print(Markdown("# Session Summary"))
    console.print(summary_table)

    session_summary_report_md = console.export_text()
    session_summary_report_md_file = "session_summary_report.md"
    _write_to_file_session(
        session_dir, session_summary_report_md_file, session_summary_report_md
    )

    # --- JSON report ---
    session_summary_report = {
        "summary_data": session_summary_data,  # Use the aggregated data
    }
    session_summary_report_json_file = "session_summary_report.json"
    _write_to_file_session(
        session_dir,
        session_summary_report_json_file,
        json.dumps(session_summary_report, indent=2),
    )


def _create_session_summary_table(session_summary_data):
    """Creates a rich table for the session-level summary."""
    table = Table(title="Session Summary")
    table.add_column("task", style="cyan", no_wrap=True)
    table.add_column("prompt", justify="right")
    table.add_column("candidate", justify="right")
    table.add_column("total", justify="right")
    table.add_column("cached", justify="right")
    table.add_column("time (s)", justify="right")

    for task_data in session_summary_data:
        table.add_row(
            task_data["task_id"],
            str(task_data["total_tokens"]["prompt"]),
            str(task_data["total_tokens"]["candidates"]),
            str(task_data["total_tokens"]["total"]),
            str(task_data["total_tokens"]["cached"]),
            f"{task_data['total_response_time']:.4f}",
        )
    return table


def _write_to_file_session(session_dir, file_name, content):
    """
    Writes content to a file in the session directory.
    Distinct from _write_to_file, which writes to task directory.
    """
    file_path = session_dir / file_name
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except (IOError, PermissionError) as e:
        print(f"Error writing to file {file_name}: {e}")
        #  log_error(f"Error writing to file {file_name}: {e}")
        # can't call log error here
        raise
