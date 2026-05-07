from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def handle_career(query):

    prompt = f"""
You are an intelligent career guidance system.

Analyze the user's query carefully.

Return ONLY valid JSON in this exact format:

{{
    "analysis": "...",
    "recommendations": [
        "...",
        "...",
        "..."
    ],
    "next_action": "..."
}}

User Query:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a career guidance AI."},
            {"role": "user", "content": prompt},
        ],
    )

    content = response.choices[0].message.content

    try:
        parsed = json.loads(content)

        return {
            "module": "career",
            "analysis": parsed["analysis"],
            "suggestions": [str(item) for item in parsed["recommendations"]],
            "action": parsed["next_action"],
        }

    except Exception as e:

        return {
            "module": "career",
            "analysis": "Could not analyze properly.",
            "suggestions": ["Try rephrasing your question."],
            "action": "Retry",
        }
