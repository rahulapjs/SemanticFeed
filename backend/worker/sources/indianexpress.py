import feedparser
from app.utils.article_content import scrape_article_content

def scrape_indianexpress():
    feed = feedparser.parse("https://indianexpress.com/section/technology/feed/")
    print(f"[IndianExpress RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        content = scrape_article_content(entry.link)
        yield {
            "source": "IndianExpress",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published"),
            "content": content
        }
