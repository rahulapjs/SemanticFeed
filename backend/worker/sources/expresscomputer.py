import feedparser

def scrape_expresscomputer():
    feed = feedparser.parse("https://www.expresscomputer.in/feed/")
    print(f"[ExpressComputer RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        yield {
            "source": "ExpressComputer",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published")
        }
