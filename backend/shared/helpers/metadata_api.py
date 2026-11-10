import requests
from enum import Enum
from app.core.config import METADATA_API_URL

class MetadataStatus(Enum):
    PROCESSING = 1
    PROCESSED = 2
    ERROR = 3

class MetadataApi:
    def __init__(self, file_id: int):
        self.api_endpoint = f"{METADATA_API_URL}api/files/{file_id}/status"
        self.headers = {"Content-Type": "application/json"}

    def set_status(self, status: MetadataStatus):

        if (status == MetadataStatus.ERROR):
            requests.patch(self.api_endpoint, json={ "status": status.name, "error": "There was an error processing the document."}, headers=self.headers)
        else:
            requests.patch(self.api_endpoint, json={ "status": status.name}, headers=self.headers)