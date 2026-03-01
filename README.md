# 🚀 IT Trend Agent — Local Agentic AI System

An autonomous **agentic AI system** that collects IT news, analyzes technology trends using a **local LLM (Phi-3 via Ollama)**, stores historical insights in **MongoDB**, and displays them on a live **FastAPI dashboard**.

Built to help developers identify **trending skills before they become outdated**.

---

# 🧠 Features

## 🤖 Agentic AI
- Autonomous daily execution (APScheduler)
- Local LLM reasoning (Phi-3 Mini)
- Persistent memory (MongoDB)
- Structured JSON trend analysis

## 📊 Trend Intelligence
Extracts:
- 🔥 Trending technologies
- 🌱 Emerging technologies
- 📉 Declining technologies
- 🧠 Skills for backend Python developers

## 🏠 Fully Local (No API Keys)
- Runs on local machine
- Uses Ollama for LLM
- Works on 8GB RAM

## 🌐 Full-Stack
- FastAPI backend
- MongoDB database
- Tailwind dashboard
- Auto-refresh UI

---

# 🏗️ Architecture
Hacker News API → Async Collector → Prompt Builder → Phi-3 (Ollama)→ JSON Parser → MongoDB → FastAPI → Dashboard

---

# ⚙️ Tech Stack

### Backend
- FastAPI
- Motor (async MongoDB)
- APScheduler
- httpx

### AI Layer
- Ollama
- Phi-3 Mini (local LLM)

### Database
- MongoDB  
  - Database: `trend_db`  
  - Collection: `daily_trends`

### Frontend
- Jinja2 templates
- TailwindCSS
- Vanilla JavaScript

---

# 📁 Project Structure
trend_agent/
│
├── app/
│ ├── main.py
│ ├── agent/
│ │ ├── trend_agent.py
│ │ ├── collectors.py
│ │ ├── llm_client.py
│ │ ├── prompt_builder.py
│ │ └── scheduler.py
│ ├── db/
│ │ └── mongo.py
│ ├── routes/
│ │ └── trends.py
│ └── templates/
│ └── dashboard.html


---

# 🔄 Agent Workflow

1. Fetch latest IT news from Hacker News
2. Build structured prompt
3. Analyze trends using Phi-3 (Ollama)
4. Extract valid JSON (custom parser)
5. Store results in MongoDB
6. Serve via `/trends` API
7. Display on dashboard
8. Run automatically every 24 hours

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|------------|
| `/` | Dashboard UI |
| `/trends` | Latest trend analysis |
| `/run-agent` | Manual agent trigger |

---

# 🖥️ Dashboard

- Dark theme UI
- Trending tech panel
- Emerging tech panel
- Declining tech panel
- Skills recommendation
- Latest news feed
- Auto-refresh every 60 seconds

---

# ⚡ Performance Optimizations

- Limited news input (≤15 items)
- Token cap for Phi-3 responses
- Async I/O everywhere
- Lightweight local model

---

# 🧠 Agentic Characteristics

- Autonomy → Scheduler-based execution  
- Memory → MongoDB historical storage  
- Reasoning → LLM trend extraction  
- Perception → News ingestion  
- Action → DB updates  

---

# 📦 MongoDB Document Example

```json
{
  "date": "UTC timestamp",
  "news": ["title1", "title2"],
  "analysis": {
    "top_trending_technologies": [],
    "emerging_technologies": [],
    "declining_technologies": [],
    "skills_for_backend_python_developer": []
  }
}