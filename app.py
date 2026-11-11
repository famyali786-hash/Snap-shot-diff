import os
import json
from datetime import datetime
import streamlit as st

SNAPSHOT_DIR = "snapshots"

@st.cache_data(show_spinner=False)
def list_snapshots():
    snaps = []
    if not os.path.exists(SNAPSHOT_DIR):
        return snaps
    for f in os.listdir(SNAPSHOT_DIR):
        if f.endswith(".json"):
            path = os.path.join(SNAPSHOT_DIR, f)
            snaps.append({"name": f, "date": datetime.fromtimestamp(os.stat(path).st_mtime)})
    return sorted(snaps, key=lambda x: x["date"], reverse=True)
