import streamlit as st
st.set_page_config(page_title="File System Snapshot", page_icon="📁", layout="wide")
st.title("📁 File System Snapshot Tool")

with st.sidebar:
    st.title("Settings")
    section = st.radio("Navigation", ["Take Snapshot", "Snapshot History", "Compare Snapshots", "Compare Files"])
