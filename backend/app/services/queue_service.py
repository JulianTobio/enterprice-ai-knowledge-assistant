from rq import Queue
from app.models.file_metadata import FileMetadata

class QueueService:
    def __init__(self, queue: Queue):
        self.queue = queue

    def queue_file_embedding(self, metadata: FileMetadata) -> str:
        job =self.queue.enqueue("shared.tasks.file_embedding", file_path=metadata.path, file_name=metadata.file_name, file_id=metadata.id)
        return job.id