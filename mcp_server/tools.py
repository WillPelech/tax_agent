from pathlib import Path
from app import mcp


@mcp.tool()
def get_file_contents(file_path: str) -> str:
    """
    get contents of a file already on disk (e.g. after the user uploads/copies a PDF or image).
    """
    p = Path(file_path).resolve().absolute()
    if not p.is_file():
        return f"This is an invalid filepath"
    if p.suffix not in [".txt",".pdf"]:
        return f"invalid file type"
    return p.read_text()


