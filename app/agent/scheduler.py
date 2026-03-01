from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.agent.trend_agent import run_trend_agent

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(
        run_trend_agent,
        "interval",
        # hours=24, temporarily set to 1 minute for testing
        minutes=1,
        id="daily_trend_job",
        replace_existing=True,
    )
    scheduler.start()