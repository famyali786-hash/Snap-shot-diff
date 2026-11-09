"""Snapshot comparison module."""

def diff_snapshots(old_snap, new_snap):
    old_files = set(old_snap.get("files", {}).keys())
    new_files = set(new_snap.get("files", {}).keys())
    added = list(new_files - old_files)
    removed = list(old_files - new_files)
    return added, removed, []
