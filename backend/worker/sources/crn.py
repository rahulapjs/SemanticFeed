import feedparser

def scrape_crn():
    feed = feedparser.parse("https://www.crn.in/rss.xml")
    print(f"[CRN RSS] Entries: {len(feed.entries)}", flush=True)

    for entry in feed.entries[:5]:
        yield {
            "source": "CRN",
            "title": entry.title,
            "url": entry.link,
            "published_at": entry.get("published")
        }
