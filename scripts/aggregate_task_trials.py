#!/usr/bin/env python3

# import argparse # Removed argparse
import logging
import re # Import re for task ID pattern matching
import shutil
import sys
# from datetime import datetime # No longer needed for generated names
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

# Basic check for typical ARC task IDs (8 alphanumeric chars)
# Adjust this regex if your task IDs have a different format
TASK_ID_PATTERN = re.compile(r"^[a-f0-9]{8}$")

def is_task_directory(path: Path) -> bool:
    """Checks if a path is a directory and its name matches the task ID pattern."""
    return path.is_dir() and bool(TASK_ID_PATTERN.match(path.name))

def find_task_ids_in_folder(folder_path: Path) -> set[str]:
    """Finds all directory names matching the task ID pattern within a folder."""
    if not folder_path.is_dir():
        logging.warning(f"Cannot find task IDs: Folder not found or not a directory: {folder_path}")
        return set()
    return {item.name for item in folder_path.iterdir() if is_task_directory(item)}


def main():
    # --- Hardcoded Configuration ---
    # Set these values directly before running the script
    MATCH_FOLDER_PATH = Path("/home/phi/PROJECTS/geometor/seer_sessions/sessions_ARCv2_eval/25.085.0644") # Folder with tasks to match
    DESTINATION_FOLDER_PATH = Path("/home/phi/PROJECTS/geometor/seer_sessions/sessions_ARCv2_eval") # Root folder for results
    SEARCH_FOLDER_PATH = Path("/home/phi/PROJECTS/geometor/seer_sessions/sessions") # Folder containing sessions to search
    DRY_RUN = False # Set to False to actually move/copy files, True to simulate
    VERBOSE = True # Set to True for detailed logging
    # --- End Hardcoded Configuration ---

    if VERBOSE:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # --- Validate input paths ---
    if not MATCH_FOLDER_PATH.is_dir():
        logging.error(f"Match folder not found: {MATCH_FOLDER_PATH}")
        sys.exit(1)
    if not SEARCH_FOLDER_PATH.is_dir():
        logging.error(f"Search folder not found: {SEARCH_FOLDER_PATH}")
        sys.exit(1)

    # --- Ensure destination exists (or create in actual run) ---
    if not DRY_RUN:
        try:
            DESTINATION_FOLDER_PATH.mkdir(parents=True, exist_ok=True)
            logging.info(f"Ensured destination directory exists: {DESTINATION_FOLDER_PATH}")
        except OSError as e:
            logging.error(f"Could not create destination directory {DESTINATION_FOLDER_PATH}: {e}")
            sys.exit(1)
    else:
        logging.info(f"DRY RUN: Would ensure destination directory exists: {DESTINATION_FOLDER_PATH}")


    # --- Get the set of task IDs to match ---
    target_task_ids = find_task_ids_in_folder(MATCH_FOLDER_PATH)
    if not target_task_ids:
        logging.error(f"No task IDs found in match folder: {MATCH_FOLDER_PATH}")
        sys.exit(1)
    logging.info(f"Found {len(target_task_ids)} target task IDs to match in {MATCH_FOLDER_PATH.name}: {', '.join(sorted(target_task_ids))}")

    # --- Iterate through the search folder ---
    logging.info(f"Searching for sessions in: {SEARCH_FOLDER_PATH}")
    sessions_processed = 0
    tasks_moved_total = 0
    errors_total = 0

    for source_session_item in SEARCH_FOLDER_PATH.iterdir():
        if not source_session_item.is_dir():
            logging.debug(f"Skipping non-directory item: {source_session_item.name}")
            continue

        # Skip the match folder itself if it's inside the search path
        if source_session_item.resolve() == MATCH_FOLDER_PATH.resolve():
            logging.info(f"Skipping the match folder itself: {source_session_item.name}")
            continue

        source_session_path = source_session_item
        logging.info(f"\n--- Processing potential source session: {source_session_path.name} ---")

        # Find task IDs in the current source session
        current_session_task_ids = find_task_ids_in_folder(source_session_path)
        if not current_session_task_ids:
            logging.info("No task directories found in this session.")
            continue

        # Find which tasks match the target list
        matching_tasks = target_task_ids.intersection(current_session_task_ids)

        if not matching_tasks:
            logging.info("No matching tasks found in this session.")
            continue

        logging.info(f"Found {len(matching_tasks)} matching task(s): {', '.join(sorted(matching_tasks))}")
        sessions_processed += 1

        # Define the corresponding destination path for this session
        dest_session_path = DESTINATION_FOLDER_PATH / source_session_path.name

        # --- Execute for this session ---
        if DRY_RUN:
            logging.info(f"DRY RUN: Planning actions for session {source_session_path.name}")
            print(f"  DRY RUN: Would ensure destination session directory exists: {dest_session_path}")

            # Simulate copying files from source root
            files_to_copy = [f for f in source_session_path.iterdir() if f.is_file()]
            if files_to_copy:
                print(f"  DRY RUN: Would copy {len(files_to_copy)} file(s) from {source_session_path} to {dest_session_path}:")
                for f in files_to_copy:
                    print(f"    - {f.name}")
            else:
                print(f"  DRY RUN: No files found in the root of {source_session_path} to copy.")

            # Simulate moving matching task directories
            print(f"  DRY RUN: Would move {len(matching_tasks)} task directorie(s):")
            for task_id in sorted(matching_tasks):
                source_task_path = source_session_path / task_id
                dest_task_path = dest_session_path / task_id
                print(f"    - Move {source_task_path} to {dest_task_path}")

        else: # Actual Run
            logging.info(f"Executing actions for session {source_session_path.name}")
            session_errors = 0
            session_tasks_moved = 0

            # 1. Create destination session directory
            try:
                logging.info(f"Creating destination session directory: {dest_session_path}")
                dest_session_path.mkdir(parents=True, exist_ok=True) # exist_ok=True in case run multiple times? Or error? Let's allow overwrite/merge for now.
            except OSError as e:
                logging.error(f"  Failed to create destination session directory {dest_session_path}: {e}")
                errors_total += 1
                continue # Skip processing this session further

            # 2. Copy files from source root
            files_copied_count = 0
            try:
                logging.info(f"Copying files from {source_session_path} root to {dest_session_path}")
                for item in source_session_path.iterdir():
                    if item.is_file():
                        source_file = item
                        dest_file = dest_session_path / item.name
                        try:
                            logging.debug(f"  Copying file: {source_file.name}")
                            shutil.copy2(source_file, dest_file) # copy2 preserves metadata
                            files_copied_count += 1
                        except Exception as e:
                            logging.error(f"  Failed to copy file {source_file.name}: {e}")
                            session_errors += 1
                logging.info(f"  Copied {files_copied_count} file(s).")
            except Exception as e:
                 logging.error(f"  Error during file copying process for {source_session_path.name}: {e}")
                 session_errors += 1


            # 3. Move matching task directories
            logging.info(f"Moving {len(matching_tasks)} matching task directorie(s)...")
            for task_id in matching_tasks:
                source_task_path = source_session_path / task_id
                dest_task_path = dest_session_path / task_id

                if not source_task_path.is_dir(): # Should exist based on earlier check, but double-check
                    logging.warning(f"  Task directory {task_id} suddenly not found in {source_session_path}, skipping move.")
                    session_errors += 1
                    continue

                try:
                    logging.info(f"  Moving {source_task_path} to {dest_task_path}")
                    shutil.move(str(source_task_path), str(dest_task_path))
                    session_tasks_moved += 1
                except Exception as e:
                    logging.error(f"  Failed to move task '{task_id}' from {source_session_path.name}: {e}")
                    session_errors += 1

            logging.info(f"  Finished processing session {source_session_path.name}. Moved: {session_tasks_moved}, Errors: {session_errors}")
            tasks_moved_total += session_tasks_moved
            errors_total += session_errors


    logging.info("\n" + "=" * 30)
    logging.info("Aggregation complete.")
    logging.info(f"  Total source sessions processed containing matches: {sessions_processed}")
    logging.info(f"  Total matching task directories moved: {tasks_moved_total}")
    logging.info(f"  Total errors encountered: {errors_total}")
    if errors_total > 0:
         logging.warning("There were errors during the operation. Please review the logs.")
    logging.info("=" * 30)


if __name__ == "__main__":
    main()
