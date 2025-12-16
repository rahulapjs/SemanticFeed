import numpy as np
from app.services.embedding_service import embed
from app.models.story import Story

SIM_THRESHOLD = 0.85

def cosine(a, b):
    return np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))

def find_semantic_story(db, title):
    vec = embed(title)
    for s in db.query(Story).all():
        if s.embedding and cosine(vec, s.embedding) > SIM_THRESHOLD:
            return s
    return None
