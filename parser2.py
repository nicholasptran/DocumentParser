import pymupdf.layout
import pymupdf4llm
from pathlib import Path

def parse(document: str):
    doc = pymupdf.open(document)

    json = pymupdf4llm.to_json(doc)
    md = pymupdf4llm.to_markdown(doc)
    text = pymupdf4llm.to_text(doc)
    Path(doc.name).with_suffix(".json").write_bytes(json.encode())
    Path(doc.name).with_suffix(".md").write_bytes(md.encode())
    Path(doc.name).with_suffix(".txt").write_bytes(text.encode())

    doc.close()



if __name__ == "__main__":
    parse("documents/testing-cms1500.pdf")
