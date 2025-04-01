#!/usr/bin/env python3

# import argparse # Removed argparse
# import hashlib # Removed hashlib (no longer generating dest name)
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

# Removed find_latest_session function

def main():
    # --- Hardcoded Configuration ---
    # Set these values directly before running the script
    SESSIONS_ROOT = Path("./sessions")
    SOURCE_SESSION_NAME = "24.092.1100"  # Replace with the actual source session name
    TASK_IDS_TO_MOVE = ["00576224", "009d5c81"] # Replace with the list of task IDs
    DEST_SESSION_NAME = "aggregated-session-example" # Replace with the desired destination name
    DRY_RUN = False # Set to False to actually move files, True to simulate
    VERBOSE = True # Set to True for detailed logging
    # --- End Hardcoded Configuration ---

    if VERBOSE:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO) # Ensure INFO level if not verbose

    # --- Validate sessions root ---
    if not SESSIONS_ROOT.is_dir():
        logging.error(f"Sessions root directory not found: {SESSIONS_ROOT}")
        sys.exit(1)

    # --- Determine source session path ---
    source_session_path = SESSIONS_ROOT / SOURCE_SESSION_NAME
    if not source_session_path.is_dir():
        logging.error(f"Source session directory not found: {source_session_path}")
        sys.exit(1)
    logging.info(f"Using source session: {source_session_path.name}")

    # --- Determine destination session path ---
    dest_session_path = SESSIONS_ROOT / DEST_SESSION_NAME

    # --- Check if destination already exists ---
    if dest_session_path.exists() and not DRY_RUN: # Only error if not dry run
        logging.error(
            f"Destination session directory already exists: {dest_session_path}"
        )
        logging.error("Please choose a different name using --dest-name or remove the existing directory.")
        sys.exit(1)

    # --- Log planned actions ---
    logging.info("-" * 30)
    logging.info(f"Operation Plan {'(DRY RUN)' if DRY_RUN else ''}:")
    logging.info(f"  Source Session: {source_session_path}")
    logging.info(f"  Destination Session: {dest_session_path}")
    logging.info(f"  Tasks to Move: {', '.join(TASK_IDS_TO_MOVE)}")
    logging.info("-" * 30)

    # --- Execute ---
    if DRY_RUN:
        logging.info("Dry Run: Simulating operations...")
        print(f"DRY RUN: Would create directory: {dest_session_path}")
        source_config = source_session_path / "config.json"
        if source_config.is_file():
            print(f"DRY RUN: Would copy {source_config} to {dest_session_path / source_config.name}")
        else:
            logging.warning(f"DRY RUN: Source config.json not found at {source_config}")

        for task_id in TASK_IDS_TO_MOVE:
            source_task_path = source_session_path / task_id
            dest_task_path = dest_session_path / task_id
            if source_task_path.is_dir():
                print(f"DRY RUN: Would move {source_task_path} to {dest_task_path}")
            else:
                logging.warning(f"Task directory not found in source session: {source_task_path}")
        logging.info("Dry Run: Simulation complete.")

    else:
        # 1. Create destination directory
        try:
            logging.info(f"Creating destination directory: {dest_session_path}")
            dest_session_path.mkdir(parents=True, exist_ok=False)
        except OSError as e:
            logging.error(f"Failed to create destination directory: {e}")
            sys.exit(1)

        # 2. Copy essential files (e.g., config.json)
        source_config = source_session_path / "config.json"
        if source_config.is_file():
            try:
                dest_config = dest_session_path / source_config.name
                logging.info(f"Copying {source_config} to {dest_config}")
                shutil.copy2(source_config, dest_config) # copy2 preserves metadata
            except Exception as e:
                logging.error(f"Failed to copy {source_config.name}: {e}")
                # Decide if this is fatal or just a warning
                logging.warning("Proceeding without config file in destination.")
        else:
            logging.warning(f"Source config.json not found at {source_config}, skipping copy.")

        # 3. Move task directories
        moved_count = 0
        error_count = 0
        for task_id in TASK_IDS_TO_MOVE:
            source_task_path = source_session_path / task_id
            dest_task_path = dest_session_path / task_id

            if not source_task_path.is_dir():
                logging.warning(f"Task directory not found, skipping: {source_task_path}")
                error_count += 1
                continue

            try:
                logging.info(f"Moving {source_task_path} to {dest_task_path}")
                shutil.move(str(source_task_path), str(dest_task_path))
                moved_count += 1
            except Exception as e:
                logging.error(f"Failed to move task '{task_id}': {e}")
                error_count += 1

        logging.info("-" * 30)
        logging.info("Operation complete.")
        logging.info(f"  Tasks successfully moved: {moved_count}")
        logging.info(f"  Tasks skipped/failed: {error_count}")
        if error_count > 0:
             logging.warning("There were errors or skipped tasks during the operation.")


if __name__ == "__main__":
    main()
