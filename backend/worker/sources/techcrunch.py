import feedparser

def scrape_techcrunch():
    feed = feedparser.parse("https://techcrunch.com/feed/")
    print(f"[TechCrunch RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        yield {
            "source": "TechCrunch",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published")
        }
