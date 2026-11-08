"""Snapshot generation module."""
import hashlib

def get_file_hash(file_path):
    h = hashlib.md5()
    with open(file_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()
