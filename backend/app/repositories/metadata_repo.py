from typing import List

from app.repositories.metadata_base import MetadataBase
from app.models.file_metadata import FileMetadata, FileMetadataCreate, FileMetadataUpdate
from sqlalchemy.orm import Session
import app.models.db_models as models

class MetadataRepository(MetadataBase):
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_metadata(self, metadata: FileMetadataCreate) -> FileMetadata:
        
        new_metadata = FileMetadata(**metadata.model_dump())
        new_metadata.status = "UPLOADED"
        self.db.add(new_metadata)
        self.db.commit()
        self.db.refresh(new_metadata)

        return new_metadata
    
    def get_file_metadata(self, id: int) -> FileMetadata:
        
        metadata = self.db.query(models.FileMetadata).filter(models.FileMetadata.id == id).first()
        
        return metadata

    def get_all_files(self) -> List[FileMetadata]:
        
        metadatas = self.db.query(models.FileMetadata).all()
        
        return metadatas

    def update_metadata(self, id: int, updated_metadata: FileMetadataUpdate) -> FileMetadata:
        
        # Get current file metadata
        db_metadata = self.db.query(models.FileMetadata).filter(models.FileMetadata.id == id).first()

        if db_metadata is None:
            raise ValueError(f"Item with ID {id} not found")

        update_metadata = updated_metadata.model_dump(exclude_unset=True)
        for key, value in update_metadata.items():
            setattr(db_metadata, key, value)
        
        self.db.commit()
        self.db.refresh(db_metadata)
        
        return db_metadata