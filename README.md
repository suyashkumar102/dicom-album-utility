# dicom-album-utility

A Python utility for scanning locally stored DICOM files and grouping them 
into albums based on the standard DICOM hierarchy — Patient → Study → Series → Image.

## What it does

Recursively scans a local directory for `.dcm` files and groups them by 
`StudyInstanceUID` and `SeriesInstanceUID`. This grouping maps directly to how 
Kheops creates shareable albums — each series becomes an album entry identified 
by its StudyUID and SeriesUID pair.

## Usage

Install dependency: `pip install pydicom`
Run: `python scan_dicom.py /path/to/dicom/folder`
