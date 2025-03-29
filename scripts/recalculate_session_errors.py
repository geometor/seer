#!/usr/bin/env python3
"""
Recalculates the error count in session index.json files.

This script iterates through session directories, reads the session's index.json,
counts errors logged directly at the session level, then iterates through
each task within the session, reads the task's index.json, sums up the
task error counts, and finally updates the session's index.json with the
correct total error count.
"""

import argparse
import json
from pathlib import Path
import sys

def recalculate_errors(sessions_root_path: Path, dry_run: bool = False):
    """
    Recalculates the error count for all sessions under the given root path.

    Args:
        sessions_root_path: The Path object pointing to the root directory
                            containing session folders.
        dry_run: If True, only print what would be changed without writing files.
    """
    print(f"Starting error recalculation in: {sessions_root_path}")
    if dry_run:
        print("--- DRY RUN MODE ---")

    session_count = 0
    updated_count = 0

    for session_dir in sessions_root_path.iterdir():
        if not session_dir.is_dir():
            continue # Skip non-directory items

        session_index_path = session_dir / "index.json"
        if not session_index_path.exists():
            print(f"Skipping {session_dir.name}: index.json not found.")
            continue

        session_count += 1
        print(f"Processing session: {session_dir.name}")

        try:
            with open(session_index_path, 'r') as f:
                session_summary = json.load(f)

            # 1. Count errors logged directly at the session level
            session_level_error_count = len(list(session_dir.glob("error_*.json")))
            print(f"  - Session-level errors found: {session_level_error_count}")

            # 2. Aggregate errors from tasks
            task_error_count = 0
            task_dirs_found = 0
            for task_dir in session_dir.iterdir():
                if not task_dir.is_dir():
                    continue # Skip non-directory items (like index.json itself)

                task_dirs_found += 1
                task_index_path = task_dir / "index.json"
                if not task_index_path.exists():
                    print(f"    - Skipping task {task_dir.name}: index.json not found.")
                    continue

                try:
                    with open(task_index_path, 'r') as f_task:
                        task_summary = json.load(f_task)
                    errors_data = task_summary.get("errors", {})
                    count = errors_data.get("count", 0)
                    task_error_count += count
                    # print(f"    - Task {task_dir.name}: Found {count} errors.") # Verbose
                except json.JSONDecodeError:
                    print(f"    - WARNING: Could not decode index.json for task {task_dir.name}. Skipping error count.")
                except Exception as e_task:
                    print(f"    - WARNING: Error reading index.json for task {task_dir.name}: {e_task}. Skipping error count.")

            print(f"  - Total errors found in {task_dirs_found} tasks: {task_error_count}")

            # 3. Calculate total and update summary
            total_error_count = session_level_error_count + task_error_count
            original_count = session_summary.get("errors", {}).get("count", "N/A")

            print(f"  - Original error count: {original_count}")
            print(f"  - Recalculated error count: {total_error_count}")

            if "errors" not in session_summary:
                session_summary["errors"] = {} # Ensure errors key exists

            if session_summary["errors"].get("count") != total_error_count:
                session_summary["errors"]["count"] = total_error_count
                updated_count += 1

                if not dry_run:
                    try:
                        with open(session_index_path, 'w') as f:
                            json.dump(session_summary, f, indent=2)
                        print(f"  - Updated {session_index_path}")
                    except Exception as e_write:
                        print(f"  - ERROR: Failed to write updated index.json for {session_dir.name}: {e_write}")
                else:
                    print(f"  - Would update {session_index_path} (dry run)")
            else:
                print("  - Error count is already correct. No update needed.")

        except json.JSONDecodeError:
            print(f"  - ERROR: Could not decode index.json for session {session_dir.name}. Skipping.")
        except Exception as e:
            print(f"  - ERROR: An unexpected error occurred processing session {session_dir.name}: {e}")

        print("-" * 20) # Separator

    print("\nRecalculation Summary:")
    print(f"  - Total sessions processed: {session_count}")
    print(f"  - Sessions updated: {updated_count}")
    if dry_run:
        print("--- END DRY RUN ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recalculate the 'errors.count' in session index.json files."
    )
    parser.add_argument(
        "--sessions-dir",
        type=str,
        default="./sessions",
        help="Path to the root directory containing session folders (default: ./sessions)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print changes without modifying files.",
    )
    args = parser.parse_args()

    sessions_root = Path(args.sessions_dir)

    if not sessions_root.is_dir():
        print(f"Error: Sessions directory not found or not a directory: {sessions_root}")
        sys.exit(1)

    recalculate_errors(sessions_root, args.dry_run)
