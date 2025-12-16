from sqlalchemy.exc import IntegrityError
from app.models.article import Article

def create_article(db, payload, story_id):
    try:
        a = Article(
            story_id=story_id,
            source=payload["source"],
            title=payload["title"],
            url=payload["url"],
            published_at=payload.get("published_at"),
        )
        db.add(a)
        db.commit()
        return a
    except IntegrityError:
        db.rollback()
        return None
