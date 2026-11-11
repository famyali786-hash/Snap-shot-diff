import streamlit as st
import hashlib

st.set_page_config(page_title="File System Snapshot", page_icon="📁", layout="wide")
def get_hash(data):
    return hashlib.md5(data).hexdigest()

with st.sidebar:
    section = st.radio("Navigation", ["Take Snapshot", "Snapshot History", "Compare Snapshots", "Compare Files"])

if section == "Take Snapshot":
    uploaded = st.file_uploader("Upload files")
