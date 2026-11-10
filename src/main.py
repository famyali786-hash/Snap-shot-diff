"""CLI menu interface."""
import os
import json
from src.snapshot import take_snapshot
from src.diff import diff_snapshots

SNAP_DIR = os.path.join(os.path.dirname(__file__), "..", "snapshots")

def list_snapshots():
    return [f for f in os.listdir(SNAP_DIR) if f.endswith(".json")] if os.path.exists(SNAP_DIR) else []
