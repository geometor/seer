"""
summary report functions
"""
import json
from rich.markdown import Markdown
from rich.table import Table
from rich.console import Console


def create_session_summary_report(session_dir, log_error, display_response):
    """
    Creates a session-level summary report by aggregating task summary reports.
    """
    session_response_report_json = []
    session_test_report_json = {}

    # Iterate through each task directory
    for task_dir in session_dir.iterdir():
        if task_dir.is_dir():
            summary_report_json_path = task_dir / "summary_report.json"
            if summary_report_json_path.exists():
                try:
                    with open(summary_report_json_path, "r") as f:
                        task_summary = json.load(f)
                        # Aggregate response reports
                        session_response_report_json.extend(
                            task_summary.get("response_report", [])
                        )
                        # Aggregate test reports, keyed by task ID
                        task_id = task_dir.name
                        session_test_report_json[task_id] = task_summary.get(
                            "test_report", {}
                        )
                except (IOError, json.JSONDecodeError) as e:
                    print(
                        f"Error reading or parsing {summary_report_json_path}: {e}"
                    )
                    log_error(
                        f"Error reading or parsing {summary_report_json_path}: {e}"
                    )

    # --- Create Markdown Report ---
    # Response Report
    response_table = _create_session_response_table(
        session_response_report_json
    )

    # Test Report
    test_tables = _create_session_test_table(session_test_report_json)

    # Combine and output using Console
    console = Console(record=True)
    console.print(Markdown("# Session Summary"))
    console.print(response_table)
    for task_tables in test_tables.values():
        for table in task_tables.values():
            console.print(table)

    session_summary_report_md = console.export_text()
    session_summary_report_md_file = "session_summary_report.md"
    _write_to_file_session(
        session_dir, session_summary_report_md_file, session_summary_report_md
    )

    # --- JSON report (keep structure) ---
    session_summary_report = {
        "response_report": session_response_report_json,
        "test_report": session_test_report_json,
    }
    session_summary_report_json_file = "session_summary_report.json"
    _write_to_file_session(
        session_dir,
        session_summary_report_json_file,
        json.dumps(session_summary_report, indent=2),
    )

    # Display report
    #  display_response(
        #  [session_summary_report_md],
        #  0,
        #  "Session Summary",
        #  {},
    #  )


def _create_session_response_table(session_response_report_json):
    """Creates a rich table for the session-level response summary."""
    table = Table(title="Session Response Summary")
    table.add_column("Task", style="cyan", no_wrap=True)
    table.add_column("File", style="cyan", no_wrap=True)
    table.add_column("Prompt", justify="right")
    table.add_column("Candidate", justify="right")
    table.add_column("Total", justify="right")
    table.add_column("Cached", justify="right")
    table.add_column("Resp Time", justify="right")
    table.add_column("Elapsed", justify="right")

    total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
    total_response_time = 0

    for response in session_response_report_json:
        task_id = response.get("response_file", "N/A").split("-")[0]
        table.add_row(
            task_id,
            response.get("response_file", "N/A"),
            str(response["token_usage"].get("prompt", 0)),
            str(response["token_usage"].get("candidates", 0)),
            str(response["token_usage"].get("total", 0)),
            str(response["token_usage"].get("cached", 0)),
            f"{response['timing']['response_time']:.4f}",
            f"{response['timing']['total_elapsed']:.4f}",
        )
        for key in total_tokens:
            total_tokens[key] += response["token_usage"].get(key, 0)
        total_response_time += response["timing"]["response_time"]

    table.add_row(
        "Total",
        "",
        str(total_tokens["prompt"]),
        str(total_tokens["candidates"]),
        str(total_tokens["total"]),
        str(total_tokens["cached"]),
        f"{total_response_time:.4f}",
        "",
        style="bold",
    )
    return table


def _create_session_test_table(session_test_report_json):
    """Creates rich tables for the session-level test summary."""
    all_tables = {}
    for task_id, test_report in session_test_report_json.items():
        task_tables = {}
        for file_index, file_results in test_report.items():
            table = Table(title=f"Task: {task_id}, Code File: {file_index}")
            table.add_column("Example", style="cyan")
            table.add_column("Stat")
            table.add_column("size")
            table.add_column("palette")
            table.add_column("colors")
            table.add_column("diff")

            for result in file_results:
                if "example" in result:
                    table.add_row(
                        str(result["example"]),
                        str(result["status"]),
                        str(result.get("size_correct", "N/A")),
                        str(result.get("color_palette_correct", "N/A")),
                        str(result.get("correct_pixel_counts", "N/A")),
                        str(result.get("pixels_off", "N/A")),
                    )
                elif "captured_output" in result:
                    table.add_row("Captured Output", str(result["captured_output"]))
                elif "code_execution_error" in result:
                    table.add_row(
                        "Code Execution Error", str(result["code_execution_error"])
                    )
            task_tables[file_index] = table
        all_tables[task_id] = task_tables
    return all_tables


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
