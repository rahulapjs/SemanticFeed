import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_article_content(url: str) -> str | None:
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, "html.parser")

        # Economic Times article body
        paragraphs = soup.select(
            "div.artText p, div.article_content p"
        )

        if not paragraphs:
            return None

        text = "\n".join(
            p.get_text(strip=True)
            for p in paragraphs
            if len(p.get_text(strip=True)) > 40
        )

        return text if len(text) > 500 else None

    except Exception as e:
        print(f"[Content scrape failed] {url} → {e}", flush=True)
        return None
