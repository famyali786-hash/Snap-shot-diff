"""CLI menu interface."""
import os
from src.snapshot import take_snapshot

SNAP_DIR = os.path.join(os.path.dirname(__file__), "..", "snapshots")

def take_snapshot_cli():
    folder = input("Folder: ").strip()
    name = input("Name: ").strip()
    take_snapshot(folder, os.path.join(SNAP_DIR, name))
