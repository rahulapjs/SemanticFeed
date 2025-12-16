import feedparser
from app.utils.article_content import scrape_article_content

def scrape_verge():
    feed = feedparser.parse("https://www.theverge.com/rss/tech/index.xml")

    print(f"[Verge RSS] Entries found: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        content = scrape_article_content(entry.link)
        yield {
            "source": "The Verge",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published"),
            "content": content
        }
