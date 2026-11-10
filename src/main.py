"""CLI menu interface for the snapshot tool."""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.snapshot import take_snapshot
from src.diff import diff_snapshots
from src.file_compare import file_status

SNAP_DIR = os.path.join(os.path.dirname(__file__), '..', 'snapshots')


def list_snapshots():
    if not os.path.exists(SNAP_DIR):
        return []
    return sorted(f for f in os.listdir(SNAP_DIR) if f.endswith('.json'))


def take_snapshot_cli():
    folder = input("Enter folder path: ").strip()
    if not os.path.isdir(folder):
        print("Error: Invalid folder path")
        return

    name = input("Enter snapshot name: ").strip()
    if not name.endswith('.json'):
        name += '.json'

    try:
        files = take_snapshot(folder, os.path.join(SNAP_DIR, name))
        print(f"Snapshot saved with {len(files)} files")
    except Exception as e:
        print(f"Error: {e}")


def compare_snapshots_cli():
    snaps = list_snapshots()
    if len(snaps) < 2:
        print("Need at least 2 snapshots to compare")
        return

    print("\nAvailable snapshots:")
    for i, s in enumerate(snaps, 1):
        print(f"  {i}. {s}")

    try:
        a = int(input("Select snapshot A (number): ").strip()) - 1
        b = int(input("Select snapshot B (number): ").strip()) - 1
    except ValueError:
        print("Invalid selection")
        return

    with open(os.path.join(SNAP_DIR, snaps[a])) as f:
        old = json.load(f)
    with open(os.path.join(SNAP_DIR, snaps[b])) as f:
        new = json.load(f)

    added, removed, modified = diff_snapshots(old, new)
    print(f"\nAdded: {len(added)}, Removed: {len(removed)}, Modified: {len(modified)}")
    for label, items in [("Added", added), ("Removed", removed), ("Modified", modified)]:
        if items:
            print(f"{label}: {items}")


def compare_files_cli():
    old = input("Enter path to old file: ").strip()
    new = input("Enter path to new file: ").strip()
    print(f"Status: {file_status(old, new)}")


def show_menu():
    while True:
        print("\n=== File System Snapshot Tool ===")
        print("a. Take Snapshot")
        print("b. Compare 2 Snapshots")
        print("c. Compare 2 Files")
        print("d. Exit")
        choice = input("\nSelect option: ").strip().lower()

        if choice == 'a':
            take_snapshot_cli()
        elif choice == 'b':
            compare_snapshots_cli()
        elif choice == 'c':
            compare_files_cli()
        elif choice == 'd':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    show_menu()
