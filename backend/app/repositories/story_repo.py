from app.models.story import Story
from app.services.embedding_service import embed

def find_by_norm(db, norm):
    return db.query(Story).filter_by(normalized_title=norm).first()

def create_story(db, title, norm):
    s = Story(
        canonical_title=title,
        normalized_title=norm,
        embedding=embed(title)
    )
    db.add(s)
    db.commit()
    db.refresh(s)
    return s
