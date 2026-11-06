from rq import Queue
from app.models.file_metadata import FileMetadata

class QueueService:
    def __init__(self, queue: Queue):
        self.queue = queue

    def queue_file_embedding(self, metadata: FileMetadata) -> str:
        job =self.queue.enqueue("shared.tasks.file_embedding", metadata)
        return job.id