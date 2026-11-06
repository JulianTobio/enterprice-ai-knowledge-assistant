from abc import ABC, abstractmethod
from typing import List
from app.models.file_metadata import FileMetadata, FileMetadataCreate, FileMetadataUpdate

class MetadataBase(ABC):
    @abstractmethod
    def create_metadata(self, metadata: FileMetadataCreate) -> FileMetadata:
        """Creates file metadata"""
        pass

    @abstractmethod
    def get_file_metadata(self, id: int) -> FileMetadata:
        """Gets file metadata"""
        pass

    @abstractmethod
    def get_all_files(self) -> List[FileMetadata]:
        """Gets all files metadata"""
        pass

    @abstractmethod
    def update_metadata(self, id: int, updated_metadata: FileMetadataUpdate) -> FileMetadata:
        """Updates a file metadata"""
        pass