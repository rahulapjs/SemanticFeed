import feedparser
from app.utils.article_content import scrape_article_content

def scrape_gadgets360():
    feed = feedparser.parse("https://www.gadgets360.com/rss/home")
    print(f"[Gadgets360 RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        content = scrape_article_content(entry.link)
        yield {
            "source": "Gadgets360",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published"),
            "content": content
        }
