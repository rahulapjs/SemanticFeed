import sys
import os
from datetime import datetime, timedelta, timezone

# Add the current directory to sys.path to make 'app' importable
sys.path.append(os.getcwd())

from sqlalchemy import delete
from app.core.database import SessionLocal
from app.models.story import Story
from app.models.article import Article

def cleanup_old_news():
    db = SessionLocal()
    try:
        # Calculate the threshold date (1 week ago)
        # Using timezone-aware UTC if possible, assuming app uses UTC
        threshold_date = datetime.now(timezone.utc) - timedelta(weeks=1)
        print(f"Cleaning up news older than: {threshold_date}")

        # Find stories created before the threshold
        # We also want to delete articles associated with these stories
        # Since we don't know if CASCADE is set up, we'll do it manually to be safe.
        
        # Method 1: Get IDs then delete
        # This is safer to debug
        stories_to_delete = db.query(Story.id).filter(Story.created_at < threshold_date).all()
        story_ids = [s[0] for s in stories_to_delete]
        
        if not story_ids:
            print("No old news found to delete.")
            return

        print(f"Found {len(story_ids)} stories to delete.")

        # Delete Articles
        deleted_articles_count = db.query(Article).filter(Article.story_id.in_(story_ids)).delete(synchronize_session=False)
        print(f"Deleted {deleted_articles_count} associated articles.")

        # Delete Stories
        deleted_stories_count = db.query(Story).filter(Story.id.in_(story_ids)).delete(synchronize_session=False)
        print(f"Deleted {deleted_stories_count} stories.")

        db.commit()
        print("Cleanup complete.")

    except Exception as e:
        print(f"Error during cleanup: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    cleanup_old_news()
