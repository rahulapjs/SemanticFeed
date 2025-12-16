from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.models.base import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    story_id = Column(Integer, ForeignKey("stories.id"))
    source = Column(String(100))
    title = Column(String(500))
    url = Column(String(1000), unique=True)
    published_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
