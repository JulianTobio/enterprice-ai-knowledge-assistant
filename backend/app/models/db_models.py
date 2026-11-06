from app.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id = Column(Integer,primary_key=True,nullable=False)
    file_name = Column(String,nullable=False)
    path = Column(String,nullable=False)
    status = Column(String,nullable=False)
    error = Column(String,nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    processed_at = Column(TIMESTAMP(timezone=True), nullable=True)