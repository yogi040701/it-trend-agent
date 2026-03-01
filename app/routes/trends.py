from fastapi import APIRouter
from app.db.mongo import trends_collection
from app.agent.trend_agent import run_trend_agent
import httpx
from pydantic import BaseModel

router = APIRouter()

class BriefRequest(BaseModel):
    headline: str


@router.get("/trends")
async def get_trends():
    latest = await trends_collection.find_one(sort=[("date", -1)])
    if latest:
        latest["_id"] = str(latest["_id"])
        return latest
    return {"message": "No trends available yet"}


@router.get("/run-agent")
async def trigger_agent():
    result = await run_trend_agent()
    return {"status": "agent executed", "analysis": result}


@router.post("/news-brief")
async def news_brief(req: BriefRequest):
    prompt = f"""You are a tech news analyst. Given this IT/tech news headline, write a concise brief of exactly ~60 words explaining what it is about, why it matters for developers, and its key implication. Be direct and insightful. No filler words.

Headline: "{req.headline}"

Respond with ONLY the brief text, no labels or preamble."""

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            },
            timeout=60.0
        )
        data = response.json()
        brief = data.get("response", "").strip()
        return {"brief": brief}