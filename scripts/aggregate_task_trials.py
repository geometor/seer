#!/usr/bin/env python3

import argparse
import hashlib
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


def find_latest_session(sessions_root: Path) -> Path | None:
    """Finds the session directory with the latest timestamp in its name."""
    latest_session = None
    latest_time = None

    for item in sessions_root.iterdir():
        if item.is_dir():
            try:
                # Assuming format like YY.DDD.HHMM or similar sortable timestamp
                # Attempt to parse the name or rely on lexicographical sorting
                # A more robust approach might involve parsing specific formats
                # For now, simple string comparison often works for ISO-like timestamps
                if latest_session is None or item.name > latest_session.name:
                    # Basic check: does it look like a session folder?
                    # Check for common files or naming patterns if needed.
                    # For now, assume any directory could be a session.
                    # Let's refine by checking for a potential timestamp format
                    parts = item.name.split('.')
                    if len(parts) >= 3 and all(p.isdigit() for p in parts):
                         # Crude check, might need adjustment based on exact naming
                        if latest_session is None or item.name > latest_session.name:
                            latest_session = item
            except Exception:
                # Ignore directories that don't match the expected naming pattern
                # or cause errors during comparison
                logging.debug(f"Could not parse session name for sorting: {item.name}")
                continue

    if latest_session:
        logging.info(f"Latest session found: {latest_session.name}")
    else:
        logging.warning(f"Could not automatically determine the latest session in {sessions_root}")

    return latest_session


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate specific task trials from one session into a new session.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--sessions-root",
        type=Path,
        default=Path("./sessions"),
        help="Path to the root directory containing session folders.",
    )
    parser.add_argument(
        "--source-session",
        type=str,
        default=None,
        help="Name of the source session directory. If omitted, the latest session will be used.",
    )
    parser.add_argument(
        "--tasks",
        type=str,
        nargs="+",
        required=True,
        help="List of task IDs (directory names) to move.",
    )
    parser.add_argument(
        "--dest-name",
        type=str,
        default=None,
        help="Name for the new aggregated session directory. If omitted, it will be generated.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually creating/moving files.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging."
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # --- Validate sessions root ---
    if not args.sessions_root.is_dir():
        logging.error(f"Sessions root directory not found: {args.sessions_root}")
        sys.exit(1)

    # --- Determine source session ---
    source_session_path: Path
    if args.source_session:
        source_session_path = args.sessions_root / args.source_session
        if not source_session_path.is_dir():
            logging.error(f"Source session directory not found: {source_session_path}")
            sys.exit(1)
        logging.info(f"Using specified source session: {source_session_path.name}")
    else:
        logging.info("Attempting to find the latest session...")
        latest_session = find_latest_session(args.sessions_root)
        if not latest_session:
            logging.error(
                "Could not find the latest session. Please specify using --source-session."
            )
            sys.exit(1)
        source_session_path = latest_session
        logging.info(f"Using latest source session: {source_session_path.name}")

    # --- Determine destination session name and path ---
    dest_session_name: str
    if args.dest_name:
        dest_session_name = args.dest_name
    else:
        # Generate a name
        timestamp = datetime.now().strftime("%y.%j.%H%M%S")
        # Create a stable hash based on sorted task IDs
        task_hash = hashlib.sha1(
            ",".join(sorted(args.tasks)).encode()
        ).hexdigest()[:8]
        dest_session_name = f"{source_session_path.name}-agg-{task_hash}-{timestamp}"
        logging.info(f"Generated destination session name: {dest_session_name}")

    dest_session_path = args.sessions_root / dest_session_name

    # --- Check if destination already exists ---
    if dest_session_path.exists():
        logging.error(
            f"Destination session directory already exists: {dest_session_path}"
        )
        logging.error("Please choose a different name using --dest-name or remove the existing directory.")
        sys.exit(1)

    # --- Log planned actions ---
    logging.info("-" * 30)
    logging.info(f"Operation Plan {'(DRY RUN)' if args.dry_run else ''}:")
    logging.info(f"  Source Session: {source_session_path}")
    logging.info(f"  Destination Session: {dest_session_path}")
    logging.info(f"  Tasks to Move: {', '.join(args.tasks)}")
    logging.info("-" * 30)

    # --- Execute ---
    if args.dry_run:
        logging.info("Dry Run: Simulating operations...")
        print(f"DRY RUN: Would create directory: {dest_session_path}")
        source_config = source_session_path / "config.json"
        if source_config.is_file():
            print(f"DRY RUN: Would copy {source_config} to {dest_session_path / source_config.name}")
        else:
            logging.warning(f"Source config.json not found at {source_config}")

        for task_id in args.tasks:
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
        for task_id in args.tasks:
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
