import feedparser
from app.utils.article_content import scrape_article_content

def scrape_economictimes():
    feed = feedparser.parse("https://economictimes.indiatimes.com/tech/rssfeeds/728148670.cms")
    print(f"[EconomicTimes RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        content = scrape_article_content(entry.link)
        yield {
            "source": "EconomicTimes",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published"),
            "content": content
        }
