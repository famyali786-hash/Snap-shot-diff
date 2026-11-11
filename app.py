import io
import zipfile
import hashlib

def build_snapshot_from_zip(zip_bytes):
    files_data = {}
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        for info in zf.infolist():
            if not info.is_dir():
                raw = zf.read(info.filename)
                files_data[info.filename] = {"size": len(raw), "hash": hashlib.md5(raw).hexdigest()}
    return files_data, []
