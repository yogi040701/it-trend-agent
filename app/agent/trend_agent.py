from datetime import datetime
from app.agent.collectors import fetch_hackernews
from app.agent.llm_client import ask_llm
from app.agent.prompt_builder import build_prompt
from app.db.mongo import trends_collection

async def run_trend_agent():

    news_titles = await fetch_hackernews()
    news_text = "\n".join(news_titles)

    prompt = build_prompt(news_text)

    analysis = await ask_llm(prompt)

    await trends_collection.insert_one({
        "date": datetime.utcnow(),
        "news": news_titles,
        "analysis": analysis
    })

    return analysis