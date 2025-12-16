from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.story import Story
from app.models.article import Article

router = APIRouter()

@router.get("/feed")
def get_feed(db: Session = Depends(get_db)):
    data = []

    stories = (
        db.query(Story)
        .order_by(Story.created_at.desc())
        .all()
    )

    for s in stories:
        articles = (
            db.query(Article)
            .filter(Article.story_id == s.id)
            .all()
        )

        data.append({
            "story_id": s.id,
            "title": s.canonical_title,
            "summary": s.ai_summary,
            "sources": [
                {
                    "source": a.source,
                    "url": a.url,
                    "published_at": a.published_at,
                }
                for a in articles
            ],
        })

    return data
