import pydicom
import os
from collections import defaultdict

def scan_dicom_directory(root_path):
    """
    Recursively scans a directory for DICOM files.
    Groups them by StudyInstanceUID -> SeriesInstanceUID.
    This mirrors the DICOM hierarchy that Kheops uses for album creation.
    """
    albums = defaultdict(lambda: defaultdict(list))
    for dirpath, _, files in os.walk(root_path):
        for f in files:
            if f.endswith('.dcm'):
                try:
                    ds = pydicom.dcmread(os.path.join(dirpath, f))
                    study = str(getattr(ds, 'StudyInstanceUID', 'unknown'))
                    series = str(getattr(ds, 'SeriesInstanceUID', 'unknown'))
                    albums[study][series].append(os.path.join(dirpath, f))
                except Exception:
                    continue
    return albums

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scan_dicom.py <path_to_dicom_folder>")
        sys.exit(1)
    results = scan_dicom_directory(sys.argv[1])
    for study, series_map in results.items():
        print(f"Study: {study}")
        for series, files in series_map.items():
            print(f"  Series: {series} — {len(files)} file(s)")
