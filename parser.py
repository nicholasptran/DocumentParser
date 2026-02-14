import pymupdf4llm
import pathlib
md_text = pymupdf4llm.to_markdown("documents/testing-cms1500.pdf", pages=[0])

if __name__ == "__main__":
    pathlib.Path("output/testing-cms1500.md").write_bytes(md_text.encode())