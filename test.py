import pymupdf.layout
import pymupdf4llm
from pathlib import Path
import os

os.environ["TESSDATA_PREFIX"] = "C:/Program Files/Tesseract-OCR/tessdata"

doc = pymupdf.open("stage/hcfa.pdf")
md = pymupdf4llm.to_markdown(doc, header=False, footer=False)
txt = pymupdf4llm.to_text(doc, header=False, footer=False)

Path("output/hcfa.md").write_bytes(md.encode())
Path("output/hcfa.txt").write_bytes(txt.encode())

doc.close()


# promt = "parse this" (attach txt and md)