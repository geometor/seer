"""
summary report functions
"""
import json
from rich.markdown import Markdown
from rich.table import Table
from rich.console import Console

def summarize_session(session):
    """
    Creates a session-level summary report by aggregating task summary reports.
    """
    session_summary = []

    for task_dir in sorted(session.session_dir.iterdir()):
        if not task_dir.is_dir():
            continue

        summary_report_json_path = task_dir / "summary_report.json"

        try:
            with open(summary_report_json_path, "r") as f:
                task_summary = json.load(f)
                task_id = task_dir.name

                task_total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
                task_total_response_time = 0
                for response in task_summary.get("response_report", []):
                    task_total_tokens["prompt"] += response["token_usage"].get("prompt", 0)
                    task_total_tokens["candidates"] += response["token_usage"].get("candidates", 0)
                    task_total_tokens["total"] += response["token_usage"].get("total", 0)
                    task_total_tokens["cached"] += response["token_usage"].get("cached", 0)
                    task_total_response_time += response["response_time"]

                # --- Get data from task summary ---
                best_train_results = task_summary.get("best_train_results", {"passed": 0, "total": 0})
                best_test_results = task_summary.get("best_test_results", {"passed": 0, "total": 0})
                test_solved = task_summary.get("test_solved", False)

                session_summary.append(
                    {
                        "task_id": task_id,
                        "total_tokens": task_total_tokens,
                        "total_response_time": task_total_response_time,
                        "best_train_results": best_train_results,  # Add to session summary
                        "best_test_results": best_test_results,    # Add to session summary
                        "test_solved": test_solved,                # Add to session summary
                    }
                )
        except (IOError, json.JSONDecodeError) as e:
            print(
                f"Error reading or parsing {summary_report_json_path}: {e}"
            )
            session.log_error(
                f"Error reading or parsing {summary_report_json_path}: {e}"
            )

    summary_table = _create_session_summary_table(session_summary)

    console = Console(record=True)
    console.print(Markdown("# Session Summary"))
    console.print(summary_table)

    session_summary_report_md = console.export_text()
    session_summary_report_md_file = "session_summary_report.md"
    _write_to_file_session(
        session.session_dir, session_summary_report_md_file, session_summary_report_md
    )

    session_summary_report = {
        "summary": session_summary,
    }
    session_summary_report_json_file = "session_summary_report.json"
    _write_to_file_session(
        session.session_dir,
        session_summary_report_json_file,
        json.dumps(session_summary_report, indent=2),
    )



def _create_session_summary_table(session_summary):
    """Creates a rich table for the session-level summary."""
    table = Table(title="Session Summary")
    table.add_column("task", style="cyan", no_wrap=True)
    table.add_column("prompt", justify="right")
    table.add_column("candidate", justify="right")
    table.add_column("total", justify="right")
    table.add_column("cached", justify="right")
    table.add_column("time (s)", justify="right")
    table.add_column("Train Score", justify="center")  # Add train score
    table.add_column("Test Score", justify="center")   # Add test score
    table.add_column("Solved", justify="center")       # Add solved column


    for task_summary in session_summary:
        table.add_row(
            task_summary["task_id"],
            str(task_summary["total_tokens"]["prompt"]),
            str(task_summary["total_tokens"]["candidates"]),
            str(task_summary["total_tokens"]["total"]),
            str(task_summary["total_tokens"]["cached"]),
            f"{task_summary['total_response_time']:.4f}",
            f"{task_summary['best_train_results']['passed']}/{task_summary['best_train_results']['total']}",  # Display best train score
            f"{task_summary['best_test_results']['passed']}/{task_summary['best_test_results']['total']}",    # Display best test score
            "✅" if task_summary["test_solved"] else "❌",  # Solved status
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
    """Creates a summary report (Markdown and JSON) and returns a summary dict."""

    resplist = gather_response(task_dir, log_error)
    response_table = _create_response_table(resplist)

    grouped_test_results = {}
    for py_file in sorted(task_dir.glob("*-py_*.json")):
        try:
            with open(py_file, "r") as f:
                test_results = json.load(f)
                file_index = py_file.stem
                grouped_test_results[file_index] = test_results
        except Exception as e:
            print(f"Failed to load test results from {py_file}: {e}")
            log_error(f"Failed to load test results from {py_file}: {e}")

    sorted_grouped_test_results = dict(sorted(grouped_test_results.items()))
    test_tables = _create_test_table(sorted_grouped_test_results)

    # --- Calculate Best Train and Test Results ---
    best_train_results = {"passed": 0, "total": 0}
    best_test_results = {"passed": 0, "total": 0}
    test_solved = False

    for file_index, results in sorted_grouped_test_results.items():
        if file_index.endswith("-train"):
            passed_count = sum(1 for res in results if res.get("match") is True)
            if results:  # Check if results is not empty
                total_count = len(results)
                if passed_count > best_train_results["passed"]:
                    best_train_results["passed"] = passed_count
                    best_train_results["total"] = total_count

        elif file_index.endswith("-test"):
            passed_count = sum(1 for res in results if res.get("match") is True)
            if results:  # Check if results is not empty
                total_count = len(results)
                if passed_count > best_test_results["passed"]:
                    best_test_results["passed"] = passed_count
                    best_test_results["total"] = total_count

    if best_test_results["total"] > 0 and best_test_results["passed"] == best_test_results["total"]:
        test_solved = True


    console = Console(record=True)
    console.print(Markdown("# Task Summary"))
    console.print(response_table)
    for table in test_tables.values():
        console.print(table)

    report_md = console.export_text()
    report_md_file = "summary_report.md"
    _write_to_file_task(task_dir, report_md_file, report_md, log_error)

    # --- JSON Report ---
    response_report_json = []
    for data in sorted(resplist, key=lambda x: x.get("response_file", "")):
        response_report_json.append({
            "response_file": data.get("response_file", "N/A"),
            "token_usage": {
                "prompt": data["usage_metadata"].get("prompt_token_count", 0),
                "candidates": data["usage_metadata"].get("candidates_token_count", 0),
                "total": data["usage_metadata"].get("total_token_count", 0),
                "cached": data["usage_metadata"].get("cached_token_count", 0)
            },
            "response_time": data["response_time"]
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
                        "match": result["match"],
                        "size_correct": result.get("size_correct", "N/A"),
                        "color_palette_correct": result.get(
                            "color_palette_correct", "N/A"
                        ),
                        "correct_pixel_counts": result.get(
                            "correct_pixel_counts", "N/A"
                        ),
                        "pixels_off": result.get("pixels_off", "N/A"),
                        "percent_correct": result.get("percent_correct", "N/A"),
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
        "best_train_results": best_train_results,  # Add to JSON
        "best_test_results": best_test_results,    # Add to JSON
        "test_solved": test_solved,                # Add to JSON
    }
    report_json_file = "summary_report.json"
    _write_to_file_task(task_dir, report_json_file, json.dumps(report_json, indent=2), log_error)

    return {  # Return the summary data
        "best_train_results": best_train_results,
        "best_test_results": best_test_results,
        "test_solved": test_solved,
    }

def gather_response(task_dir, log_error):
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

    total_tokens = {"prompt": 0, "candidates": 0, "total": 0, "cached": 0}
    total_response_time = 0

    sorted_resplist = sorted(resplist, key=lambda x: x.get("response_file", ""))

    for data in sorted_resplist:
        table.add_row(
            data.get("response_file", "N/A"),
            str(data["usage_metadata"].get("prompt_token_count", 0)),
            str(data["usage_metadata"].get("candidates_token_count", 0)),
            str(data["usage_metadata"].get("cached_token_count", 0)),
            str(data["usage_metadata"].get("total_token_count", 0)),
            f"{data['response_time']:.4f}",
        )

        total_tokens["prompt"] += data["usage_metadata"].get("prompt_token_count", 0)
        total_tokens["candidates"] += data["usage_metadata"].get("candidates_token_count", 0)
        total_tokens["total"] += data["usage_metadata"].get("total_token_count", 0)
        total_tokens["cached"] += data["usage_metadata"].get("cached_token_count", 0)
        total_response_time += data.get("response_time", 0) # handle missing

    # Add a summary row
    table.add_row(
        "TOTAL",
        str(total_tokens["prompt"]),
        str(total_tokens["candidates"]),
        str(total_tokens["cached"]),
        str(total_tokens["total"]),
        f"{total_response_time:.4f}",
        style="bold",
    )
    return table

def _get_status_emoji(status):
    """Returns an emoji based on the status."""
    if status is True:
        return "✅"
    elif status is False:
        return "❌"
    else:
        return "N/A"


def _create_test_table(grouped_test_results):
    """Creates a rich.table.Table for the test report."""
    tables = {}
    for file_index, test_results in grouped_test_results.items():
        table = Table(title=f"Code File: {file_index}")
        table.add_column("Example", style="cyan")
        table.add_column("match")
        table.add_column("size")
        table.add_column("palette")
        table.add_column("color count")
        table.add_column("diff pixels")
        table.add_column("%")

        for result in test_results:
            if "example" in result:
                # --- Emoji Logic ---
                match = _get_status_emoji(result.get("match"))
                size_correct = _get_status_emoji(result.get("size_correct"))
                palette_correct = _get_status_emoji(result.get("color_palette_correct"))
                color_count_correct = _get_status_emoji(result.get("correct_pixel_counts"))

                pixels_off = str(result.get("pixels_off", "N/A"))
                percent_correct = float(result.get("percent_correct", 0))

                table.add_row(
                    str(result["example"]),
                    match,
                    size_correct,
                    palette_correct,
                    color_count_correct,
                    pixels_off,
                    f"{percent_correct:.2f}"
                )
            elif "captured_output" in result:
                table.add_row("Captured Output", result["captured_output"])
            elif "code_execution_error" in result:
                table.add_row("Code Execution Error", result["code_execution_error"])
        tables[file_index] = table
    return tables

def _write_to_file_task(task_dir, file_name, content, log_error):
    """Writes content to a file in the task directory."""
    file_path = task_dir / file_name  # Use task_dir
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except (IOError, PermissionError) as e:
        print(f"Error writing to file {file_name}: {e}")
        log_error(f"Error writing to file {file_name}: {e}")

