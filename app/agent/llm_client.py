import httpx
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"


def extract_json(text: str) -> dict:
    """
    Extract JSON object from LLM response even if wrapped in markdown or extra text.
    """
    try:
        # 1️⃣ Try direct JSON
        return json.loads(text)
    except:
        pass

    # 2️⃣ Extract JSON inside ```json ... ```
    code_block = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if code_block:
        try:
            return json.loads(code_block.group(1))
        except:
            pass

    # 3️⃣ Extract first {...} JSON object
    json_match = re.search(r"(\{.*\})", text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except:
            pass

    return {"error": "Invalid JSON", "raw": text}


async def ask_llm(prompt: str) -> dict:
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 300}
            }
        )

    raw = response.json()["response"]
    return extract_json(raw)