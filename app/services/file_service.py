import os
from app.core.config import DOCUMENTS_PATH
from fastapi import UploadFile, HTTPException, status

ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024

class FileService:
    def __init__(self):
        os.makedirs(DOCUMENTS_PATH, exist_ok=True)
    
    async def save_file(self, upload_file: UploadFile) -> None:
        """Save a file to the specified path."""

        # 1. Validate extension
        _, ext = os.path.splitext(upload_file.filename)
        if ext.lower() not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Invalid file type extension."
            )

        # 2. Destination path
        file_path = os.path.join(DOCUMENTS_PATH, upload_file.filename)
        
        # 3. Stream data to disk securely & track size dynamically
        file_size = 0
        try:
            with open(file_path, "wb") as buffer:
                while chunk := await upload_file.read(64 * 1024):  # 64KB chunks
                    file_size += len(chunk)
                    if file_size > MAX_FILE_SIZE:
                        raise HTTPException(
                            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                            detail="File size exceeds the 5MB maximum limit."
                        )
                    buffer.write(chunk)
        except Exception as e:
            if os.path.exists(file_path):
                os.remove(file_path)  # Cleanup partial files on failure
            raise e
        
        return