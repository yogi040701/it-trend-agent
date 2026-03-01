from fastapi import FastAPI, Request
from app.routes.trends import router as trends_router
from app.agent.scheduler import start_scheduler
from fastapi.templating import Jinja2Templates


app = FastAPI(title="IT Trend Agent API")

templates = Jinja2Templates(directory="app/templates")

app.include_router(trends_router)

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})