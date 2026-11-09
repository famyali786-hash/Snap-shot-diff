"""Snapshot generation — walk a folder, hash files, save as JSON."""

import os
import json
import hashlib


def get_file_hash(file_path):
    """Compute MD5 hash of a file, reading in chunks to handle large files."""
    h = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def take_snapshot(folder_path, output_file):
    """Scan folder recursively, record size/mtime/hash for each file, save as JSON."""
    files = {}

    for root, _, filenames in os.walk(folder_path):
        for fname in filenames:
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, folder_path)

            try:
                stat = os.stat(full_path)
                files[rel_path] = {
                    "size": stat.st_size,
                    "mtime": stat.st_mtime,
                    "hash": get_file_hash(full_path)
                }
            except (OSError, PermissionError):
                continue

    snapshot = {"files": files}

    out_dir = os.path.dirname(output_file)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(snapshot, f, indent=2)

    return files
