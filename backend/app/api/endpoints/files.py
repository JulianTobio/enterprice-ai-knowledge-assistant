from fastapi import APIRouter, File, UploadFile, status, Depends
from app.dependencies import get_file_service, get_queue_service
from app.models.file_list_response import FileListResponse
from app.services.file_service import FileService
from app.services.queue_service import QueueService
from app.models.file_metadata import FileMetadataUpdate, FileMetadata

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED, response_model=FileMetadata)
async def upload_document(
    file: UploadFile = File(...),
    service: FileService = Depends(get_file_service),
    queue: QueueService = Depends(get_queue_service)
):
    file_metadata = await service.save_file(file)
    queue.queue_file_embedding(file_metadata)
    return file_metadata

@router.get("/", status_code=status.HTTP_200_OK, response_model=FileListResponse)
async def list_documents(
    service: FileService = Depends(get_file_service)
):
    files = await service.list_files()
    return FileListResponse(files=files)

@router.patch("/{item_id}/status", status_code=status.HTTP_200_OK, response_model=FileMetadata)
async def update_status(
    item_id: int,
    updated_metadata: FileMetadataUpdate,
    service: FileService = Depends(get_file_service)
    ):
    return await service.update_file_metadata(item_id, updated_metadata)