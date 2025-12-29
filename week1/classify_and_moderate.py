# week1/classify_and_moderate.py

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def moderate_input(text: str) -> bool:
    """
    Returns True if content is allowed, False otherwise
    """
    response = client.moderations.create(
        model="omni-moderation-latest",
        input=text,
    )
    return not response.results[0].flagged

def classify_input(text: str) -> dict:
    """
    Classifies user input into predefined categories.
    Returns structured JSON.
    """
    system_prompt = """
    You are a classification engine.
    Classify the user input into ONE of the following categories:
    - billing
    - technical_issue
    - general_question
    - feedback

    Respond ONLY in valid JSON with keys:
    category, confidence
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        temperature=0,
    )

    return response.choices[0].message.content

def safe_parse_json(text: str) -> dict | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None

def classify_with_retry(text: str, retries: int = 2) -> dict | None:
    for attempt in range(retries):
        raw = classify_input(text)
        parsed = safe_parse_json(raw)
        if parsed is not None:
            return parsed
    return None

if __name__ == "__main__":
    user_input = "My payment was declined and I was charged twice."

    if not moderate_input(user_input):
        print("Input rejected by moderation.")
    else:
        parsed = classify_with_retry(user_input, retries=2)

        if parsed is None:
            fallback = {"category": "general_question", "confidence": 0.0, "fallback": True}
            print("Fallback classification:", fallback)
        else:
            print("Final classification:", parsed)
