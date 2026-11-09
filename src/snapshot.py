"""Snapshot generation module."""
import os
import hashlib

def get_file_hash(file_path):
    h = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def take_snapshot(folder_path, output_file):
    files = {}
    for root, _, filenames in os.walk(folder_path):
        for fname in filenames:
            full_path = os.path.join(root, fname)
            rel = os.path.relpath(full_path, folder_path)
            try:
                st = os.stat(full_path)
                files[rel] = {"size": st.st_size, "mtime": st.st_mtime, "hash": get_file_hash(full_path)}
            except (OSError, PermissionError):
                continue
    return files
