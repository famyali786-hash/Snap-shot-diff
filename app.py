import streamlit as st
import hashlib

def get_hash(data):
    return hashlib.md5(data).hexdigest()

def build_snapshot_from_uploads(uploaded_files):
    files_data = {}
    for uf in uploaded_files:
        raw = uf.read()
        files_data[uf.name] = {"size": len(raw), "hash": get_hash(raw)}
    return files_data
