# 🚀 IT Trend Agent — Local Agentic AI System

> An autonomous agentic AI system that collects IT news, analyzes technology trends using a **local LLM (Phi-3 via Ollama)**, stores historical insights in **MongoDB**, and displays them on a live **FastAPI dashboard**.

Built to help developers identify **trending skills before they become outdated**.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Agent Workflow](#-agent-workflow)
- [API Endpoints](#-api-endpoints)
- [Dashboard](#-dashboard)
- [Getting Started](#-getting-started)
- [MongoDB Document Schema](#-mongodb-document-schema)
- [Performance Optimizations](#-performance-optimizations)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🧠 Features

### 🤖 Agentic AI
- Autonomous daily execution via **APScheduler**
- Local LLM reasoning with **Phi-3 Mini**
- Persistent memory using **MongoDB**
- Structured JSON trend analysis

### 📊 Trend Intelligence
Automatically extracts:
- 🔥 **Trending technologies**
- 🌱 **Emerging technologies**
- 📉 **Declining technologies**
- 🧠 **Skills for backend Python developers**

### 🏠 Fully Local — No API Keys Required
- Runs entirely on your local machine
- Uses **Ollama** for LLM inference
- Works on as low as **8GB RAM**

### 🌐 Full-Stack Application
- **FastAPI** backend
- **MongoDB** database
- **Tailwind CSS** dashboard
- Auto-refresh UI

---

## 🏗️ Architecture

```
Hacker News API → Async Collector → Prompt Builder → Phi-3 (Ollama)
       → JSON Parser → MongoDB → FastAPI → Dashboard
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI, Motor (async MongoDB), APScheduler, httpx |
| **AI Layer** | Ollama, Phi-3 Mini (local LLM) |
| **Database** | MongoDB (`trend_db` / `daily_trends`) |
| **Frontend** | Jinja2 Templates, TailwindCSS, Vanilla JavaScript |

---

## 📁 Project Structure

```
trend_agent/
│
├── app/
│   ├── main.py
│   ├── agent/
│   │   ├── trend_agent.py
│   │   ├── collectors.py
│   │   ├── llm_client.py
│   │   ├── prompt_builder.py
│   │   └── scheduler.py
│   ├── db/
│   │   └── mongo.py
│   ├── routes/
│   │   └── trends.py
│   └── templates/
│       └── dashboard.html
```

---

## 🔄 Agent Workflow

```
1. Fetch latest IT news from Hacker News
2. Build structured prompt
3. Analyze trends using Phi-3 (Ollama)
4. Extract valid JSON (custom parser)
5. Store results in MongoDB
6. Serve via /trends API
7. Display on dashboard
8. Run automatically every 24 hours
```

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | `GET` | Dashboard UI |
| `/trends` | `GET` | Latest trend analysis |
| `/run-agent` | `POST` | Manual agent trigger |

---

## 🖥️ Dashboard

- 🌑 Dark theme UI
- 🔥 Trending tech panel
- 🌱 Emerging tech panel
- 📉 Declining tech panel
- 🧠 Skills recommendation panel
- 📰 Latest news feed
- 🔄 Auto-refresh every 60 seconds

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MongoDB installed locally
- [Ollama](https://ollama.com/) installed

### 1️⃣ Start MongoDB

```bash
mongod --dbpath ~/mongodb-data
```

### 2️⃣ Start Ollama

```bash
ollama run phi3:mini
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Open Dashboard

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 MongoDB Document Schema

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
```

---

## ⚡ Performance Optimizations

- Limited news input (≤ 15 items) for low-RAM LLM inference
- Token cap on Phi-3 responses
- Async I/O throughout the entire stack
- Lightweight local model (Phi-3 Mini)

---

## 🧠 Agentic Characteristics

| Characteristic | Implementation |
|----------------|----------------|
| **Autonomy** | Scheduler-based execution |
| **Memory** | MongoDB historical storage |
| **Reasoning** | LLM trend extraction |
| **Perception** | News ingestion |
| **Action** | Database updates |

---

## 📈 Future Enhancements

- [ ] Trend momentum detection (today vs. yesterday)
- [ ] GitHub trending integration
- [ ] Job market skill analysis
- [ ] Time-series charts
- [ ] Personalized learning roadmap
- [ ] Multi-agent architecture

---

## 💼 About This Project

> Built a fully local agentic AI system using **FastAPI**, **MongoDB**, **APScheduler**, and **Phi-3 via Ollama** that autonomously analyzes IT trends and generates structured skill recommendations with a live dashboard.

---

## 🧑‍💻 Author

**Yogjeet Singh**  
Backend & AI Developer

---

> ⭐ If you found this useful, consider giving the repo a star!