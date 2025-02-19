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

    for task_data in session_summary_
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

def summarize_task(task_dir, log_error):
    """Creates a summary report (Markdown and JSON) using rich.table.Table."""

    # Gather response data and create summary report
    resplist = gather_response_data(task_dir, log_error)

    # Response Report
    response_table = _create_response_table(resplist)

    # Test Report
    grouped_test_results = {}
    for py_file in sorted(task_dir.glob("*-py_*.json")):
        try:
            with open(py_file, "r") as f:
                test_results = json.load(f)
                file_index = py_file.stem.split("-")[0]
                grouped_test_results[file_index] = test_results
        except Exception as e:
            print(f"Failed to load test results from {py_file}: {e}")
            log_error(f"Failed to load test results from {py_file}: {e}")

    sorted_grouped_test_results = dict(sorted(grouped_test_results.items()))
    test_tables = _create_test_table(sorted_grouped_test_results)

    console = Console(record=True)  # Use record=True to capture output
    console.print(Markdown("# Task Summary"))
    console.print(response_table)
    for table in test_tables.values():
        console.print(table)

    report_md = console.export_text()  # Export captured output as plain text
    report_md_file = "summary_report.md"
    _write_to_file_task(task_dir, report_md_file, report_md)

    # --- JSON Report (Keep as before, but use sorted data) ---
    response_report_json = []
    for data in sorted(resplist, key=lambda x: x.get("response_file", "")):
        response_report_json.append({
            "response_file": data.get("response_file", "N/A"),
            "token_usage": data["token_totals"],
            "timing": data["timing"],
        })

    test_report_json = {}
    for file_index, test_results in sorted_grouped_test_results.items():
        test_report_json[file_index] = []
        for result in test_results:
            if "example" in result:
                test_report_json[file_index].append(
                    {
                        "example": result["example"],
                        "input": result["input"],
                        "expected_output": result["expected_output"],
                        "transformed_output": result.get("transformed_output", ""),
                        "status": result["status"],
                        "size_correct": result.get("size_correct", "N/A"),
                        "color_palette_correct": result.get(
                            "color_palette_correct", "N/A"
                        ),
                        "correct_pixel_counts": result.get(
                            "correct_pixel_counts", "N/A"
                        ),
                        "pixels_off": result.get("pixels_off", "N/A"),
                    }
                )
            elif "captured_output" in result:
                test_report_json[file_index].append(
                    {"captured_output": result["captured_output"]}
                )
            elif "code_execution_error" in result:
                test_report_json[file_index].append(
                    {"code_execution_error": result["code_execution_error"]}
                )

    report_json = {
        "response_report": response_report_json,
        "test_report": test_report_json,
    }
    report_json_file = "summary_report.json"
    _write_to_file_task(task_dir, report_json_file, json.dumps(report_json, indent=2))

def gather_response_data(task_dir, log_error):
    """Gathers data from all response.json files in the task directory."""
    resplist = []
    for respfile in task_dir.glob("*-response.json"):
        try:
            with open(respfile, "r") as f:
                data = json.load(f)
                resplist.append(data)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading or parsing {respfile}: {e}")
            log_error(f"Error reading or parsing {respfile}: {e}")
    return resplist


def _create_response_table(resplist):
    """Creates a rich.table.Table for the response report."""
    table = Table(title="Task Responses")
    table.add_column("file", style="cyan", no_wrap=True)
    table.add_column("prompt", justify="right")
    table.add_column("candidate", justify="right")
    table.add_column("cached", justify="right")
    table.add_column("total", justify="right")
    table.add_column("Time (s)", justify="right")
    table.add_column("Elapsed (s)", justify="right")

    total_tokens = {"prompt_total_tokens": 0, "candidates_total_tokens": 0, "total_total_tokens": 0, "cached_total_tokens": 0}
    total_response_time = 0

    sorted_resplist = sorted(resplist, key=lambda x: x.get("response_file", ""))

    for data in sorted_resplist:
        table.add_row(
            data.get("response_file", "N/A"),
            str(data["usage_metadata"].get("prompt_token_count", 0)),
            str(data["usage_metadata"].get("candidates_token_count", 0)),
            str(data["usage_metadata"].get("cached_token_count", 0)),
            str(data["usage_metadata"].get("total_token_count", 0)),
            f"{data['timing']['response_time']:.4f}",
            f"{data['timing']['total_elapsed']:.4f}",
        )

        for key in total_tokens:
            total_tokens[key] += data["usage_metadata"].get(key, 0)
        total_response_time += data["timing"]["response_time"]

    # Add a summary row
    table.add_row(
        "TOTAL",
        str(total_tokens["prompt_total_tokens"]),
        str(total_tokens["candidates_total_tokens"]),
        str(total_tokens["cached_total_tokens"]),
        str(total_tokens["total_total_tokens"]),
        f"{total_response_time:.4f}",
        "",
        style="bold",
    )
    return table


def _create_test_table(grouped_test_results):
    """Creates a rich.table.Table for the test report."""
    tables = {}
    for file_index, test_results in grouped_test_results.items():
        table = Table(title=f"Code File: {file_index}")
        table.add_column("Example", style="cyan")
        table.add_column("Status")
        table.add_column("size")
        table.add_column("palette")
        table.add_column("color count")
        table.add_column("diff pixels")

        for result in test_results:
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
                table.add_row("Captured Output", result["captured_output"])
            elif "code_execution_error" in result:
                table.add_row("Code Execution Error", result["code_execution_error"])
        tables[file_index] = table
    return tables

def _write_to_file_task(task_dir, file_name, content):
    """Writes content to a file in the task directory."""
    file_path = task_dir / file_name  # Use task_dir
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except (IOError, PermissionError) as e:
        print(f"Error writing to file {file_name}: {e}")
        log_error(f"Error writing to file {file_name}: {e}")
