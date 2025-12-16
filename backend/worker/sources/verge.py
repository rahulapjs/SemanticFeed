import feedparser

def scrape_verge():
    feed = feedparser.parse("https://www.theverge.com/rss/tech/index.xml")

    print(f"[Verge RSS] Entries found: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        yield {
            "source": "The Verge",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published")
        }
