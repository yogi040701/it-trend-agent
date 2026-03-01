def build_prompt(news_text: str) -> str:
    return f"""
You are a technology trend analyzer.

From the IT news below, extract:

- top_trending_technologies (list of 5)
- emerging_technologies (list)
- declining_technologies (list)
- skills_for_backend_python_developer (list)

Rules:
- Output ONLY valid JSON
- No explanation
- No extra text

News:
{news_text}
"""