import httpx

HN_URL = "https://hn.algolia.com/api/v1/search?query=AI"

async def fetch_hackernews():
    async with httpx.AsyncClient() as client:
        res = await client.get(HN_URL)
        data = res.json()

    titles = [item["title"] for item in data["hits"] if item["title"]]
    return titles[:15]  # keep small for phi3