#!/usr/bin/env python3

import sys
import csv # Add csv import
from pathlib import Path
from collections import defaultdict
from rich.console import Console
from rich.table import Table

def find_duplicate_tasks(corpus_dirs: list[Path]) -> dict[str, list[str]]:
    """
    Scans specified corpus directories for task files (*.json) and identifies
    task IDs present in more than one directory.

    Args:
        corpus_dirs: A list of Path objects representing the directories to scan.

    Returns:
        A dictionary where keys are task IDs found in multiple corpora,
        and values are lists of the names of the corpora containing that task ID.
        Returns an empty dictionary if no duplicates are found.
    """
    task_locations = defaultdict(list)
    valid_corpus_names = []

    print("Scanning directories...")
    for corpus_dir in corpus_dirs:
        # Ensure we are working with Path objects
        corpus_path = Path(corpus_dir)
        if not corpus_path.is_dir():
            print(f"Warning: '{corpus_path}' is not a valid directory. Skipping.", file=sys.stderr)
            continue

        # Construct a two-level identifier (e.g., parent_dir/current_dir)
        corpus_identifier = f"{corpus_path.parent.name}/{corpus_path.name}"
        valid_corpus_names.append(corpus_identifier)
        print(f" -> Scanning '{corpus_identifier}' ({corpus_path})...")
        found_count = 0
        for task_file in corpus_path.glob('*.json'):
            if task_file.is_file():
                task_id = task_file.stem  # Get filename without extension
                task_locations[task_id].append(corpus_identifier) # Use the new identifier
                found_count += 1
        print(f"    Found {found_count} task files.")

    print("\nIdentifying duplicates...")
    duplicates = {}
    for task_id, locations in task_locations.items():
        # Use set to count unique corpus names for a task_id
        if len(set(locations)) > 1:
            duplicates[task_id] = sorted(list(set(locations))) # Store unique, sorted list

    return duplicates

def main():
    # --- Define your corpus directories here ---
    # Replace these example paths with the actual paths to your corpus folders
    corpus_directory_paths = [
        "/path/to/your/arc-v1/data/training",
        "/path/to/your/arc-v2/data/training",
        "/path/to/another/corpus/folder",
        # Add more paths as needed
    ]
    output_csv_file = "duplicate_tasks.csv" # Define output CSV filename
    # -------------------------------------------

    # Convert string paths to Path objects and resolve them (optional but good practice)
    absolute_corpus_dirs = [Path(p).resolve() for p in corpus_directory_paths]

    duplicate_tasks = find_duplicate_tasks(absolute_corpus_dirs)

    if not duplicate_tasks:
        print("\nNo duplicate task IDs found across the specified directories.")
    else:
        print(f"\nFound {len(duplicate_tasks)} duplicate task IDs:")

        # --- Create and print the rich table ---
        console = Console()
        table = Table(title="Duplicate Task IDs Across Corpora", show_header=True, header_style="bold magenta")

        # Determine all unique corpus locations involved in duplicates
        all_locations = set()
        for locations in duplicate_tasks.values():
            all_locations.update(locations)
        # sorted_locations = sorted(list(all_locations)) # Keep original order instead

        # Determine the order of columns based on the input list, filtering by those actually found
        ordered_locations = []
        for p_str in corpus_directory_paths:
            p = Path(p_str).resolve()
            identifier = f"{p.parent.name}/{p.name}"
            if identifier in all_locations and identifier not in ordered_locations:
                 ordered_locations.append(identifier)

        # Add columns to the table in the desired order
        table.add_column("Task ID", style="dim", width=12)
        for loc in ordered_locations: # Use ordered_locations
            table.add_column(loc, justify="center")

        # Add rows to the table
        # Sort by task ID for consistent output
        for task_id in sorted(duplicate_tasks.keys()):
            locations = duplicate_tasks[task_id]
            row_data = [task_id]
            for loc_header in ordered_locations: # Use ordered_locations
                if loc_header in locations:
                    row_data.append("[green]X[/]") # Mark if found
                else:
                    row_data.append("") # Empty if not found
            table.add_row(*row_data)

        console.print(table)

        # --- Write data to CSV file ---
        print(f"\nWriting duplicate task information to '{output_csv_file}'...")
        try:
            with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # Write header
                header = ["Task ID"] + ordered_locations
                writer.writerow(header)
                # Write data rows
                for task_id in sorted(duplicate_tasks.keys()):
                    locations = duplicate_tasks[task_id]
                    row_data = [task_id]
                    for loc_header in ordered_locations:
                        row_data.append("X" if loc_header in locations else "")
                    writer.writerow(row_data)
            print(f"Successfully wrote CSV file: {output_csv_file}")
        except IOError as e:
            print(f"Error writing CSV file: {e}", file=sys.stderr)
        # ---------------------------------------

if __name__ == "__main__":
    main()
