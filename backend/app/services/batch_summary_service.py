from app.core.database import SessionLocal
from app.models.story import Story
from app.models.article import Article
from app.services.genai_client import get_client
from app.utils.json_parser import parse_json


def generate_batch_summaries():
    db = SessionLocal()
    client = get_client()

    stories = (
        db.query(Story)
        .filter(Story.ai_summary.is_(None))
        .all()
    )

    if not stories:
        print("✓ No stories pending summary", flush=True)
        db.close()
        return

    print(f"✨ Generating summaries for {len(stories)} stories", flush=True)

    prompt_blocks = []

    for story in stories:
        articles = (
            db.query(Article)
            .filter(Article.story_id == story.id)
            .all()
        )

        if not articles:
            continue

        contents = []

        for a in articles:
            text = f"TITLE: {a.title}\n"

            if a.content:
                text += f"CONTENT:\n{a.content[:3000]}"
            else:
                text += "CONTENT:\n(Not available)"

            contents.append(text)

        joined_content = "\n\n---\n\n".join(contents)

        prompt_blocks.append(
            f"""
STORY_ID: {story.id}
CONTENT:
{joined_content}
"""
        )

    if not prompt_blocks:
        print("✓ No valid stories with content to summarize", flush=True)
        db.close()
        return

    final_prompt = f"""
You are a professional tech news analyst.

For each STORY_ID below, generate a concise summary.

Rules:
- Neutral tone
- Bullet points
- No repetition
- 2–4 bullets max
- Summarize the *core idea*, not every detail
- Output MUST be a JSON array
- Do NOT add any text outside JSON

Format:
[
  {{
    "story_id": number,
    "summary": string
  }}
]

INPUT:
{''.join(prompt_blocks)}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=final_prompt
        )
    except Exception as e:
        print(f"⚠️ Gemini request failed: {e}", flush=True)
        db.close()
        return

    try:
        summaries = parse_json(response.text)
    except Exception as e:
        print(f"⚠️ Failed to parse Gemini response: {e}", flush=True)
        db.close()
        return

    updated = 0
    for item in summaries:
        story = db.get(Story, item.get("story_id"))
        if story and item.get("summary"):
            story.ai_summary = item["summary"]
            updated += 1

    db.commit()
    db.close()

    print(f"★ Batch summaries updated: {updated}", flush=True)
