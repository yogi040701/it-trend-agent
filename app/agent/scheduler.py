from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.agent.trend_agent import run_trend_agent

scheduler = AsyncIOScheduler()

AGENT_INTERVAL_MINUTES = 5

def start_scheduler():
    scheduler.add_job(
        run_trend_agent,
        "interval",
        # hours=24, temporarily set to 1 minute for testing
        minutes=AGENT_INTERVAL_MINUTES,
        id="daily_trend_job",
        replace_existing=True,
    )
    scheduler.start()