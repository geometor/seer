
import argparse
import json
import logging
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Constants matching TaskPairTrial metrics ---
# These keys should match what TaskPairTrial.to_dict() produces
# and what TaskStep.summarize() expects for the best trial.
SIZE_CORRECT_KEY = "size_correct"
PALETTE_CORRECT_KEY = "color_palette_correct"
COLOR_COUNT_CORRECT_KEY = "color_count_correct"
PIXELS_OFF_KEY = "pixels_off"
PERCENT_CORRECT_KEY = "percent_correct"
MATCH_KEY = "match" # Key indicating if the trial pair passed

# --- Helper Functions ---

def safe_load_json(file_path: Path) -> Optional[Dict[str, Any]]:
    """Safely loads a JSON file, returning None on error."""
    if not file_path.is_file():
        # logging.debug(f"JSON file not found: {file_path}")
        return None
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in file: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading JSON file {file_path}: {e}")
        return None

def count_errors(level_dir: Path) -> int:
    """Counts error files (error_*.json) in a directory."""
    return len(list(level_dir.glob("error_*.json")))

def get_level_description(level_dir: Path) -> Optional[str]:
    """Attempts to read description from existing index.json."""
    existing_index = safe_load_json(level_dir / "index.json")
    return existing_index.get("description") if existing_index else None

def get_step_title_index(step_dir: Path) -> Tuple[str, str]:
    """Attempts to read title and index from existing index.json or derive index."""
    existing_index = safe_load_json(step_dir / "index.json")
    title = "Unknown Title"
    index = step_dir.name # Default to directory name
    if existing_index:
        title = existing_index.get("title", title)
        index = existing_index.get("index", index)
    # Ensure index looks like a step index
    if not index.isdigit():
        index = step_dir.name # Fallback if format is unexpected
    return title, index

def analyze_step_trials(step_dir: Path) -> Dict[str, Any]:
    """
    Loads trial results from the 'trials' subdirectory of a step,
    analyzes them, and returns aggregated metrics.
    Mimics parts of StepCodeTrials based on saved data.
    """
    trials_dir = step_dir / "trials"
    results = {
        "best_score": None,
        "any_train_passed": False,
        "any_test_passed": False,
        "best_trial_metrics": { # For direct inclusion in step summary
            "size_correct": None,
            "palette_correct": None,
            "colors_correct": None,
            "pixels_off": None,
            "percent_correct": None,
        },
        "all_train_results_summary": {"total": 0, "passed": 0, "failed": 0},
        "all_test_results_summary": {"total": 0, "passed": 0, "failed": 0},
    }
    all_code_trials_data = []

    if not trials_dir.is_dir():
        return results # No trials directory

    # 1. Load all CodeTrial JSONs
    for trial_file in trials_dir.glob("*.json"):
        code_trial_data = safe_load_json(trial_file)
        if code_trial_data:
            all_code_trials_data.append(code_trial_data)

    if not all_code_trials_data:
        return results # No valid trial files found

    # 2. Process each CodeTrial
    best_score = float('inf')
    found_valid_score = False
    all_train_pair_trials = []
    all_test_pair_trials = []
    best_trial_for_metrics = None # Store the data of the best CodeTrial

    for ct_data in all_code_trials_data:
        score = ct_data.get("score")
        train_results = ct_data.get("train_results", {}).get("trials", [])
        test_results = ct_data.get("test_results", {}).get("trials", [])

        # Aggregate TaskPairTrial data (represented as dicts)
        all_train_pair_trials.extend(train_results)
        all_test_pair_trials.extend(test_results)

        # Update best score and track the best trial data
        if score is not None and score < best_score:
            best_score = score
            found_valid_score = True
            best_trial_for_metrics = ct_data # Keep track of the best one

        # Check if this trial passed train/test
        if train_results and all(t.get(MATCH_KEY, False) for t in train_results):
            results["any_train_passed"] = True
        if test_results and all(t.get(MATCH_KEY, False) for t in test_results):
            results["any_test_passed"] = True

    results["best_score"] = best_score if found_valid_score else None

    # 3. Calculate overall trial summaries
    if all_train_pair_trials:
        passed = sum(1 for t in all_train_pair_trials if t.get(MATCH_KEY, False))
        results["all_train_results_summary"] = {
            "total": len(all_train_pair_trials),
            "passed": passed,
            "failed": len(all_train_pair_trials) - passed,
        }
    if all_test_pair_trials:
        passed = sum(1 for t in all_test_pair_trials if t.get(MATCH_KEY, False))
        results["all_test_results_summary"] = {
            "total": len(all_test_pair_trials),
            "passed": passed,
            "failed": len(all_test_pair_trials) - passed,
        }

    # 4. Extract metrics from the best trial's *train* results for the step summary
    if best_trial_for_metrics:
        best_train_trials = best_trial_for_metrics.get("train_results", {}).get("trials", [])
        if best_train_trials:
            size_correct_list = [t.get(SIZE_CORRECT_KEY) for t in best_train_trials]
            palette_correct_list = [t.get(PALETTE_CORRECT_KEY) for t in best_train_trials]
            color_count_correct_list = [t.get(COLOR_COUNT_CORRECT_KEY) for t in best_train_trials]
            pixels_off_list = [t.get(PIXELS_OFF_KEY) for t in best_train_trials if t.get(PIXELS_OFF_KEY) is not None]
            percent_correct_list = [t.get(PERCENT_CORRECT_KEY) for t in best_train_trials if t.get(PERCENT_CORRECT_KEY) is not None]

            # Use all() for boolean checks, sum/avg for numerical
            results["best_trial_metrics"]["size_correct"] = all(s is True for s in size_correct_list) if size_correct_list else None
            results["best_trial_metrics"]["palette_correct"] = all(p is True for p in palette_correct_list) if palette_correct_list else None
            results["best_trial_metrics"]["colors_correct"] = all(c is True for c in color_count_correct_list) if color_count_correct_list else None
            results["best_trial_metrics"]["pixels_off"] = sum(pixels_off_list) if pixels_off_list else None
            results["best_trial_metrics"]["percent_correct"] = sum(percent_correct_list) / len(percent_correct_list) if percent_correct_list else None

    return results


# --- Rebuild Functions ---

def rebuild_step_summary(step_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a single TaskStep directory.
    If dry_run is True, logs the intended action instead of writing the file.
    """
    logging.debug(f"  Rebuilding Step: {step_dir.name}")
    summary = {}
    try:
        # Basic info
        title, index = get_step_title_index(step_dir)
        summary["title"] = title
        summary["index"] = index

        # Error count
        error_count = count_errors(step_dir)
        summary["errors"] = {"count": error_count, "types": []} # Types not easily available
        summary["has_errors"] = error_count > 0

        # Response info
        response_data = safe_load_json(step_dir / "response.json")
        response_summary = {
            "response_time": None,
            "prompt_tokens": None,
            "candidates_tokens": None,
            "total_tokens": None,
        }
        attempts = 0 # Default if not found
        if response_data:
            response_summary["response_time"] = response_data.get("response_time")
            # Extract token counts (handle potential structure variations)
            usage_metadata = response_data.get("usage_metadata", {})
            if usage_metadata: # Gemini API structure
                 response_summary["prompt_tokens"] = usage_metadata.get("prompt_token_count")
                 response_summary["candidates_tokens"] = usage_metadata.get("candidates_token_count")
                 response_summary["total_tokens"] = usage_metadata.get("total_token_count")
            # Add other potential structures if needed
            attempts = response_data.get("retries", 0) + 1 # Retries + initial attempt

        summary["response"] = response_summary
        summary["attempts"] = attempts

        # Code info
        codes = {}
        code_files = list(step_dir.glob("code_*"))
        for cf in code_files:
            file_type = cf.suffix[1:] # e.g., 'py'
            if file_type not in codes:
                codes[file_type] = {}
            codes[file_type][cf.name] = "Content not loaded" # Don't need content for summary
        summary["codes"] = {
            "count": len(code_files),
            "types": list(codes.keys()),
        }

        # Trial info
        trial_analysis = analyze_step_trials(step_dir)
        summary["best_score"] = trial_analysis["best_score"]
        if trial_analysis["any_train_passed"] is not None:
             summary["train_passed"] = trial_analysis["any_train_passed"]
        if trial_analysis["any_test_passed"] is not None:
             summary["test_passed"] = trial_analysis["any_test_passed"]

        # Add best trial metrics directly
        summary.update(trial_analysis["best_trial_metrics"])

        # Add overall trial summaries (optional, but useful)
        summary["trials"] = {}
        if trial_analysis["all_train_results_summary"]["total"] > 0:
            summary["trials"]["train"] = trial_analysis["all_train_results_summary"]
        if trial_analysis["all_test_results_summary"]["total"] > 0:
            summary["trials"]["test"] = trial_analysis["all_test_results_summary"]

        # Duration - cannot be accurately recalculated, keep if exists?
        existing_index = safe_load_json(step_dir / "index.json")
        summary["duration_seconds"] = existing_index.get("duration_seconds") if existing_index else None

        # Write the new index or log if dry run
        output_path = step_dir / "index.json"
        if dry_run:
            logging.info(f"    DRY RUN: Would write index to {output_path}")
            # Optionally log the summary content in dry run for debugging
            # logging.debug(f"    DRY RUN Content:\n{json.dumps(summary, indent=2)}")
        else:
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=2)
            logging.debug(f"    -> Wrote {output_path}")
        return summary

    except Exception as e:
        logging.error(f"  Failed to rebuild step {step_dir.name}: {e}")
        logging.error(traceback.format_exc())
        return None


def rebuild_task_summary(task_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a SessionTask directory.
    If dry_run is True, logs the intended action instead of writing the file.
    """
    logging.info(f" Rebuilding Task: {task_dir.name}")
    summary = {}
    step_summaries = []
    try:
        # Find and rebuild step summaries first
        step_dirs = sorted([d for d in task_dir.iterdir() if d.is_dir() and d.name.isdigit()])
        for step_dir in step_dirs:
            step_summary = rebuild_step_summary(step_dir, dry_run=dry_run) # Pass dry_run down
            if step_summary:
                step_summaries.append(step_summary)

        # Aggregate from step summaries
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_steps = 0
        task_train_passed = False
        task_test_passed = False
        best_score = float('inf')
        found_valid_score = False
        all_train_results = []
        all_test_results = []

        for step_summary in step_summaries:
            # Aggregate tokens
            tokens = step_summary.get("response", {})
            if tokens.get("prompt_tokens") is not None:
                total_prompt_tokens += tokens["prompt_tokens"]
            if tokens.get("candidates_tokens") is not None:
                total_candidates_tokens += tokens["candidates_tokens"]
            if tokens.get("total_tokens") is not None:
                total_tokens_all_steps += tokens["total_tokens"]

            # Aggregate passed status
            if step_summary.get("train_passed") is True:
                task_train_passed = True
            if step_summary.get("test_passed") is True:
                task_test_passed = True

            # Find overall best score
            step_best_score = step_summary.get("best_score")
            if step_best_score is not None and step_best_score < best_score:
                best_score = step_best_score
                found_valid_score = True

            # Aggregate trial summaries (if needed for task level)
            # Note: SessionTask.summarize aggregates raw trials, let's mimic that
            # This requires analyze_step_trials to return more detail or re-parsing
            # For simplicity now, we'll just use the step-level summaries
            # If you need the detailed trial aggregation at the task level,
            # analyze_step_trials would need modification.


        summary["steps"] = len(step_summaries)
        summary["train_passed"] = task_train_passed
        summary["test_passed"] = task_test_passed
        summary["best_score"] = best_score if found_valid_score else None
        summary["tokens"] = {
            "prompt_tokens": total_prompt_tokens,
            "candidates_tokens": total_candidates_tokens,
            "total_tokens": total_tokens_all_steps,
        }

        # Task-level errors
        error_count = count_errors(task_dir)
        summary["errors"] = {"count": error_count, "types": []} # Types not easily available

        # Duration - keep if exists?
        existing_index = safe_load_json(task_dir / "index.json")
        summary["duration_seconds"] = existing_index.get("duration_seconds") if existing_index else None
        # Matches - Removed as per request
        # summary["matches"] = None # Or read from existing if needed

        # Trials - Re-aggregate if needed, or use step summaries
        # For now, leave it empty or use step summaries if sufficient
        summary["trials"] = {} # Placeholder


        # Write the new index or log if dry run
        output_path = task_dir / "index.json"
        if dry_run:
            logging.info(f"    DRY RUN: Would write index to {output_path}")
            # logging.debug(f"    DRY RUN Content:\n{json.dumps(summary, indent=2)}")
        else:
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=2)
            logging.info(f"   -> Wrote {output_path}")
        return summary

    except Exception as e:
        logging.error(f" Failed to rebuild task {task_dir.name}: {e}")
        logging.error(traceback.format_exc())
        return None


def rebuild_session_summary(session_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a Session directory.
    If dry_run is True, logs the intended action instead of writing the file.
    """
    logging.info(f"Rebuilding Session: {session_dir.name}")
    summary = {}
    task_summaries = []
    try:
        # Find and rebuild task summaries first
        # Assume task dirs are subdirs that are not step-like (not just digits)
        # And not special files/dirs like 'config.json', context files etc.
        potential_task_dirs = [
            d for d in session_dir.iterdir()
            if d.is_dir() and not d.name.isdigit()
        ]
        for task_dir in potential_task_dirs:
            # Simple check: does it contain step-like dirs?
            if any(sd.is_dir() and sd.name.isdigit() for sd in task_dir.iterdir()):
                 task_summary = rebuild_task_summary(task_dir, dry_run=dry_run) # Pass dry_run down
                 if task_summary:
                     task_summaries.append(task_summary)
            else:
                logging.debug(f" Skipping non-task directory: {task_dir.name}")


        # Aggregate from task summaries
        session_train_passed_count = 0
        session_test_passed_count = 0
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        total_steps = 0
        total_task_error_count = 0 # Errors from tasks

        for task_summary in task_summaries:
            if task_summary.get("train_passed") is True:
                session_train_passed_count += 1
            if task_summary.get("test_passed") is True:
                session_test_passed_count += 1

            # Aggregate tokens
            tokens = task_summary.get("tokens", {})
            if tokens.get("prompt_tokens") is not None:
                total_prompt_tokens += tokens["prompt_tokens"]
            if tokens.get("candidates_tokens") is not None:
                total_candidates_tokens += tokens["candidates_tokens"]
            if tokens.get("total_tokens") is not None:
                total_tokens_all_tasks += tokens["total_tokens"]

            # Aggregate steps
            total_steps += task_summary.get("steps", 0)

            # Aggregate task errors
            total_task_error_count += task_summary.get("errors", {}).get("count", 0)

        summary["count"] = len(task_summaries)
        summary["train_passed"] = session_train_passed_count
        summary["test_passed"] = session_test_passed_count
        summary["total_steps"] = total_steps
        summary["tokens"] = {
            "prompt_tokens": total_prompt_tokens,
            "candidates_tokens": total_candidates_tokens,
            "total_tokens": total_tokens_all_tasks,
        }

        # Session-level errors + aggregated task errors
        session_error_count = count_errors(session_dir)
        total_error_count = session_error_count + total_task_error_count
        summary["errors"] = {"count": total_error_count, "types": []} # Types not easily available

        # Description - keep if exists
        summary["description"] = get_level_description(session_dir)

        # Duration - keep if exists
        existing_index = safe_load_json(session_dir / "index.json")
        summary["duration_seconds"] = existing_index.get("duration_seconds") if existing_index else None

        # Task trials - Removed as per request
        # summary["task_trials"] = {} # Placeholder or read from existing if needed


        # Write the new index or log if dry run
        output_path = session_dir / "index.json"
        if dry_run:
            logging.info(f"  DRY RUN: Would write index to {output_path}")
            # logging.debug(f"  DRY RUN Content:\n{json.dumps(summary, indent=2)}")
        else:
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=2)
            logging.info(f" -> Wrote {output_path}")
        return summary

    except Exception as e:
        logging.error(f" Failed to rebuild session {session_dir.name}: {e}")
        logging.error(traceback.format_exc())
        return None

# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(
        description="Rebuild index.json files for sessions, tasks, and steps."
    )
    parser.add_argument(
        "sessions_root",
        type=str,
        nargs="?",
        default=".",
        help="Path to the root directory containing session folders (default: ./sessions)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without writing any files.",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # sessions_root_path = Path("../../seer_sessions/session_002") # Use arg instead
    sessions_root_path = Path(args.sessions_root)

    if not sessions_root_path.is_dir():
        logging.error(f"Sessions root directory not found: {sessions_root_path}")
        return

    logging.info(f"Starting index rebuild process in: {sessions_root_path.resolve()}")

    session_dirs = sorted([d for d in sessions_root_path.iterdir() if d.is_dir()])

    if not session_dirs:
        logging.warning(f"No session directories found in {sessions_root_path}")
        return

    for session_dir in session_dirs:
        rebuild_session_summary(session_dir, dry_run=args.dry_run) # Pass dry_run flag

    if args.dry_run:
        logging.info("DRY RUN completed. No files were modified.")
    else:
        logging.info("Index rebuild process completed.")


if __name__ == "__main__":
    main()
