from fastapi import APIRouter
from app.db.mongo import trends_collection
from app.agent.trend_agent import run_trend_agent

router = APIRouter()

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