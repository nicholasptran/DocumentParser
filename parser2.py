import pymupdf.layout
import pymupdf4llm
from pathlib import Path

doc = pymupdf.open("documents/testing-cms1500.pdf")
json = pymupdf4llm.to_json(doc, pages=[0])
suffix = ".json"

Path(doc.name).with_suffix(suffix).write_bytes(json.encode())