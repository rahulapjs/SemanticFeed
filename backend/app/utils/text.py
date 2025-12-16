import re

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on",
    "for", "with", "by", "as", "at", "from"
}

def normalize_title(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", "", title)
    words = title.split()
    words = [w for w in words if w not in STOPWORDS]
    return " ".join(words)
