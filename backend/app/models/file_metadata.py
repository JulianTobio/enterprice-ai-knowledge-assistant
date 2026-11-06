from pydantic import BaseModel, ConfigDict, AwareDatetime
from typing import Optional

class BaseFileMetadata(BaseModel):
    file_name: str
    path: str

class FileMetadataCreate(BaseFileMetadata):
    pass

class FileMetadataUpdate(BaseFileMetadata):
    file_name: Optional[str] = None
    path: Optional[str] = None
    status: Optional[str] = None
    processed_at: AwareDatetime | None = None

class FileMetadata(BaseFileMetadata):
    id: int
    status: str
    
    model_config = ConfigDict(from_attributes=True)