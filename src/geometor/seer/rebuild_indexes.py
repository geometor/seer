
import argparse
import json
import logging
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Import the class containing the static analysis method
from geometor.seer.trials.step_code_trials import StepCodeTrials

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

# Removed analyze_step_trials function as its logic is now in StepCodeTrials.analyze_trial_data

# --- Rebuild Functions ---

# --- CHANGE: Return type signature ---
def rebuild_step_summary(step_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a single TaskStep directory.
    If dry_run is True, logs the intended action instead of writing the file.

    Returns:
        The summary dictionary, or None if rebuilding failed.
    """
    logging.debug(f"  Rebuilding Step: {step_dir.name}")
    summary = {}
    try:
        # --- Prioritize existing metadata ---
        existing_index = safe_load_json(step_dir / "index.json")
        if existing_index is None:
            existing_index = {} # Ensure it's a dict to avoid errors on .get()

        # Basic info - Prefer existing, fallback to derived
        title, default_index = get_step_title_index(step_dir) # Get defaults
        summary["title"] = existing_index.get("title", title)
        summary["index"] = existing_index.get("index", default_index)
        # summary["model_name"] = existing_index.get("model_name") # Removed model_name

        # --- CHANGE: Calculate and store has_errors boolean ---
        error_count = count_errors(step_dir)
        summary["has_errors"] = error_count > 0
        # --- REMOVED: errors dict ---

        # Response info - Recalculate from response.json
        response_data = safe_load_json(step_dir / "response.json")
        response_summary = {
            "response_time": None, # Will be overwritten if found
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
        summary["attempts"] = attempts # Recalculated attempts

        # Code info - Set 'py' boolean key
        code_files = list(step_dir.glob("code_*.py")) # Specifically look for .py files
        summary["py"] = len(code_files) > 0
        # summary["codes"] = ... # Removed codes dict

        # --- Trial info - Use the unified analysis method ---
        trial_data_list = []

        # Specifically glob for files ending in '.trial.json'
        for trial_file in step_dir.glob("*.trial.json"):
            code_trial_data = safe_load_json(trial_file)
            if code_trial_data:
                trial_data_list.append(code_trial_data)

        # --- Conditionally Analyze and Add Trial Info ---
        if trial_data_list: # Only analyze if trial files were found
            # Call the static analysis method from StepCodeTrials
            trial_analysis = StepCodeTrials.analyze_trial_data(trial_data_list)

            # Populate summary with analysis results
            # Only add keys if they have meaningful values from the analysis
            if trial_analysis["best_score"] is not None:
                summary["best_score"] = trial_analysis["best_score"]
            if trial_analysis.get("any_train_passed") is not None:
                summary["train_passed"] = trial_analysis["any_train_passed"]
            if trial_analysis.get("any_test_passed") is not None:
                summary["test_passed"] = trial_analysis["any_test_passed"]

            # Add best trial metrics directly only if they are not all None
            best_metrics = trial_analysis["best_trial_metrics"]
            if any(v is not None for v in best_metrics.values()):
                summary.update(best_metrics)
        # else: If no trial_data_list, trial keys are simply not added to the summary

        # Removed "trials" summary section
        # --- End Conditional Trial Info Update ---

        # Duration - cannot be accurately recalculated, keep if exists
        # Already handled by reading existing_index at the start
        summary["duration_seconds"] = existing_index.get("duration_seconds")

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
        # --- CHANGE: Return only summary ---
        return summary

    except Exception as e:
        logging.error(f"  Failed to rebuild step {step_dir.name}: {e}")
        logging.error(traceback.format_exc())
        # --- CHANGE: Return None ---
        return None


# --- CHANGE: Return type signature ---
def rebuild_task_summary(task_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a SessionTask directory.
    If dry_run is True, logs the intended action instead of writing the file.

    Returns:
        The summary dictionary, or None if rebuilding failed.
    """
    logging.info(f" Rebuilding Task: {task_dir.name}")
    summary = {}
    step_summaries = [] # Store loaded/rebuilt step summaries
    # --- REMOVED: total_step_errors ---
    any_step_has_errors = False # Flag for step errors
    try:
        # --- Prioritize existing metadata ---
        existing_index = safe_load_json(task_dir / "index.json")
        if existing_index is None:
            existing_index = {}

        # --- Find and rebuild/load step summaries ---
        step_dirs = sorted([d for d in task_dir.iterdir() if d.is_dir() and d.name.isdigit()])
        for step_dir in step_dirs:
            # --- CHANGE: Get only summary from rebuild_step_summary ---
            step_summary = rebuild_step_summary(step_dir, dry_run=dry_run)
            # --- REMOVED: step_error_count accumulation ---
            if step_summary:
                step_summaries.append(step_summary)
                # --- CHANGE: Check has_errors flag from step summary ---
                if step_summary.get("has_errors"):
                    any_step_has_errors = True
            else:
                # Treat failed step rebuild as an error condition for the task
                any_step_has_errors = True
                logging.warning(f"  Skipping failed step rebuild for task aggregation: {step_dir.name}")


        # --- Analyze Step Summaries using static method ---
        # Import SessionTask locally if not already imported globally
        from geometor.seer.session.session_task import SessionTask
        analysis_results = SessionTask.analyze_step_summaries(step_summaries)

        # --- Populate Task Summary ---
        summary["steps"] = analysis_results["steps"]
        summary["train_passed"] = analysis_results["train_passed"]
        summary["test_passed"] = analysis_results["test_passed"]
        summary["tokens"] = analysis_results["tokens"]

        # Conditionally add best_score
        if analysis_results["best_score"] is not None:
            summary["best_score"] = analysis_results["best_score"]

        # --- CHANGE: Calculate and store has_errors boolean ---
        task_level_error_count = count_errors(task_dir)
        summary["has_errors"] = (task_level_error_count > 0) or any_step_has_errors
        # --- REMOVED: errors dict ---

        # Duration - keep if exists
        summary["duration_seconds"] = existing_index.get("duration_seconds")

        # summary["trials"] = {} # Removed trials summary


        # Write the new index or log if dry run
        output_path = task_dir / "index.json"
        if dry_run:
            logging.info(f"    DRY RUN: Would write index to {output_path}")
            # logging.debug(f"    DRY RUN Content:\n{json.dumps(summary, indent=2)}")
        else:
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=2)
            logging.info(f"   -> Wrote {output_path}")
        # --- CHANGE: Return only summary ---
        return summary

    except Exception as e:
        logging.error(f" Failed to rebuild task {task_dir.name}: {e}")
        logging.error(traceback.format_exc())
        # --- CHANGE: Return None ---
        return None


def rebuild_session_summary(session_dir: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Rebuilds the index.json for a Session directory.
    If dry_run is True, logs the intended action instead of writing the file.

    Returns:
        The summary dictionary, or None if rebuilding failed.
    """
    logging.info(f"Rebuilding Session: {session_dir.name}")
    summary = {}
    task_summaries = []
    # --- REMOVED: total_errors_from_tasks ---
    any_task_has_errors = False # Flag for task errors
    tasks_with_errors_count = 0 # Counter for tasks with errors
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
                 # --- CHANGE: Get only summary from rebuild_task_summary ---
                 task_summary = rebuild_task_summary(task_dir, dry_run=dry_run)
                 # --- REMOVED: task_error_count accumulation ---
                 if task_summary:
                     task_summaries.append(task_summary)
                     # --- CHANGE: Check has_errors flag from task summary and count ---
                     if task_summary.get("has_errors"):
                         any_task_has_errors = True
                         tasks_with_errors_count += 1 # Increment count
                 else:
                     # Treat failed task rebuild as an error condition for the session
                     any_task_has_errors = True
                     tasks_with_errors_count += 1 # Count failed rebuild as error task
            else:
                logging.debug(f" Skipping non-task directory: {task_dir.name}")


        # Aggregate from task summaries
        session_train_passed_count = 0
        session_test_passed_count = 0
        total_prompt_tokens = 0
        total_candidates_tokens = 0
        total_tokens_all_tasks = 0
        total_steps = 0
        # Error counting/aggregation happens during the task rebuild loop above

        for task_summary in task_summaries:
            # Aggregate pass counts, tokens, steps (error status handled above)
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

            # Error aggregation removed here

        summary["count"] = len(task_summaries)
        summary["train_passed"] = session_train_passed_count # Matches Session.summarize key
        summary["test_passed"] = session_test_passed_count # Matches Session.summarize key
        summary["total_steps"] = total_steps
        summary["tokens"] = {
            "prompt_tokens": total_prompt_tokens,
            "candidates_tokens": total_candidates_tokens,
            "total_tokens": total_tokens_all_tasks,
        }

        # --- Store the count of tasks with errors ---
        # This count includes tasks with errors logged at the task level,
        # failed step rebuilds, or failed task rebuilds.
        summary["tasks_with_errors_count"] = tasks_with_errors_count
        # --- REMOVED: has_errors key ---
        # --- REMOVED: errors dict ---

        # Description - keep if exists
        summary["description"] = get_level_description(session_dir)

        # Duration - keep if exists
        existing_index = safe_load_json(session_dir / "index.json")
        summary["duration_seconds"] = existing_index.get("duration_seconds") if existing_index else None

        # Task trials - Removed
        # summary["task_trials"] = {}


        # Write the new index or log if dry run
        output_path = session_dir / "index.json"
        if dry_run:
            logging.info(f"  DRY RUN: Would write index to {output_path}")
            # logging.debug(f"  DRY RUN Content:\n{json.dumps(summary, indent=2)}")
        else:
            with open(output_path, "w") as f:
                json.dump(summary, f, indent=2)
            logging.info(f" -> Wrote {output_path}")
        return summary # Return only the summary dict

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
