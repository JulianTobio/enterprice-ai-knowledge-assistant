from fastapi import APIRouter, File, UploadFile, status, Depends
from app.dependencies import get_file_service
from app.services.file_service import FileService

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    service: FileService = Depends(get_file_service)
):
    await service.save_file(file)
    return {"message": "File uploaded successfully."}