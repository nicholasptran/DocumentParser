import pymupdf


def is_image(document: pymupdf.Document) -> bool:
    """Check if the document is an image based on its metadata.

    Args:
        document (pymupdf.Document): The document to check.

    Returns:
        bool: True if the document is an image, False otherwise.
    """
    if document.metadata is None:
        return False

    format = document.metadata.get("format")
    return format is not None and format == "Image"
