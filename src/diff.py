"""Snapshot comparison module."""

def diff_snapshots(old_snap, new_snap):
    old_files = set(old_snap.get("files", {}).keys())
    new_files = set(new_snap.get("files", {}).keys())
    added = list(new_files - old_files)
    removed = list(old_files - new_files)
    modified = []
    for path in old_files & new_files:
        old_h = old_snap["files"][path].get("hash")
        new_h = new_snap["files"][path].get("hash")
        if old_h != new_h:
            modified.append(path)
    return added, removed, modified
