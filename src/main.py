"""CLI menu interface."""
import os
from src.file_compare import file_status

def compare_files_cli():
    old = input("Old: ").strip()
    new = input("New: ").strip()
    print(f"Status: {file_status(old, new)}")
