from pydantic import BaseModel
from app.models.file_metadata import FileMetadata

class FileListResponse(BaseModel):
    files: list[FileMetadata]