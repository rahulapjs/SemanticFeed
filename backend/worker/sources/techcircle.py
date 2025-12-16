import feedparser

def scrape_techcircle():
    feed = feedparser.parse("https://techcircle.in/feed/")
    print(f"[TechCircle RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        yield {
            "source": "TechCircle",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published")
        }
