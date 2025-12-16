import threading
import time
from fastapi import FastAPI

from app.core.database import engine
from app.models import story, article
from app.api.feed import router as feed_router
from worker.scraper import run_scraper
from app.services.batch_summary_service import generate_batch_summaries

stop_event = threading.Event()

# Create tables
story.Base.metadata.create_all(bind=engine)
article.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech News Aggregator")
app.include_router(feed_router)


def cron_loop():
    while not stop_event.is_set():
        print("▶ Running scraper...", flush=True)

        try:
            run_scraper()
        except Exception as e:
            print(f"⚠️ Scraper failed: {e}", flush=True)

        print("▶ Running batch summarizer...", flush=True)

        try:
            generate_batch_summaries()
        except Exception as e:
            print(f"⚠️ Batch summary failed: {e}", flush=True)

        print("Sleeping 5 minutes...", flush=True)
        stop_event.wait(300)


@app.on_event("startup")
def start_cron():
    t = threading.Thread(target=cron_loop, daemon=True)
    t.start()


@app.on_event("shutdown")
def stop_cron():
    print("Stopping cron loop...", flush=True)
    stop_event.set()
