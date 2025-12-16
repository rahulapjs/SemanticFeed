import json
import re


def parse_json(text: str):
    """
    Safely extract a JSON array from LLM output.
    """
    match = re.search(r"\[.*\]", text, re.S)
    if not match:
        raise ValueError("No JSON array found in response")

    return json.loads(match.group())
