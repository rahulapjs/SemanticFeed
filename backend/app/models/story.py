from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from app.models.base import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    canonical_title = Column(String(500), nullable=False)
    normalized_title = Column(String(500), index=True)
    embedding = Column(JSON)
    ai_summary = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
