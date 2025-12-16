from itertools import chain
from app.core.database import SessionLocal
from app.repositories import story_repo, article_repo
from app.utils.text import normalize_title
from app.services.dedup_service import find_semantic_story

from worker.sources.techcrunch import scrape_techcrunch
from worker.sources.verge import scrape_verge
from worker.sources.gadgets360 import scrape_gadgets360
from worker.sources.indianexpress import scrape_indianexpress
from worker.sources.indiatoday import scrape_indiatoday
from worker.sources.techcircle import scrape_techcircle
from worker.sources.economictimes import scrape_economictimes
from worker.sources.expresscomputer import scrape_expresscomputer
from worker.sources.crn import scrape_crn


def run_scraper():
    db = SessionLocal()

    print("\n▶ Scraper started", flush=True)
    total = 0
    created_count = 0
    skipped_count = 0

    for article in chain(
        scrape_techcrunch(),
        scrape_verge(),
        scrape_gadgets360(),
        scrape_indianexpress(),
        scrape_indiatoday(),
        scrape_techcircle(),
        scrape_economictimes(),
        scrape_expresscomputer(),
        scrape_crn(),
    ):
        total += 1

        title = article["title"]
        print(f"\n📰 Article fetched: {title}", flush=True)

        norm = normalize_title(title)
        print(f"   normalized_title = {norm}", flush=True)

        # 1️⃣ Rule-based dedup
        story = story_repo.find_by_norm(db, norm)
        if story:
            print(f"   ✓ Rule-based match (story_id={story.id})", flush=True)

        # 2️⃣ Semantic dedup
        if not story:
            story = find_semantic_story(db, title)
            if story:
                print(f"   ✓ Semantic match (story_id={story.id})", flush=True)

        # 3️⃣ Create story
        if not story:
            story = story_repo.create_story(db, title, norm)
            print(f"   ➕ New story created (story_id={story.id})", flush=True)

        # 4️⃣ Create article
        created = article_repo.create_article(db, article, story.id)
        if not created:
            skipped_count += 1
            print("   ⏭ Duplicate article skipped (URL exists)", flush=True)
            continue

        created_count += 1
        print(f"   ✅ Article saved (article_id={created.id})", flush=True)

        db.commit()

    db.close()

    print("\n▶ Scraper finished", flush=True)
    print(f"   Total fetched   : {total}", flush=True)
    print(f"   New articles    : {created_count}", flush=True)
    print(f"   Duplicates skip : {skipped_count}\n", flush=True)
