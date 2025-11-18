# 🌟 Smart Life Organizer — Multi-Agent Concierge System
**Kaggle x Google — AI Agents Intensive (Concierge Track)**  
**Author:** Najil Umair  
**Project Type:** Multi-Agent Personal Automation System  
**Tech:** Python · Multi-Agent System · Tools · Memory · Observability · FastAPI-ready · Docker-ready

---

## 📌 Overview
Smart Life Organizer is a **multi-agent automation system** designed to help individuals streamline daily routines such as:

- Meal Planning  
- Shopping List Generation  
- Daily Schedule Suggestions  
- Task Automation  
- Reminder Management  

The system uses a **Supervisor Agent** to coordinate 5 sub-agents, each responsible for a specific part of the workflow.

This project was developed as part of the  
**Google & Kaggle 5-Day AI Agents Intensive — Capstone Project (2025).**

---

## 🚀 Key Features

### 🧠 Multi-Agent System (5 Agents)
- **Meal Planner Agent** – Creates a 7-day meal plan  
- **Shopping Agent** – Generates shopping list from meals  
- **Scheduler Agent** – Suggests daily cooking & breakfast schedule  
- **Task Manager Agent** – Creates tasks from meal plan  
- **Reminder Agent** – Creates reminders from the schedule  
- **Supervisor Agent** – Orchestrates the full workflow  

### 🔧 Tools  
- Custom **JSONStoreTool** for structured storage  
- Acts as an ADK-style tool for saving/retrieving artifacts

### 🗃 Memory  
- **MemoryBank** stores summaries (long-term memory)  
- Follows ADK “sessions & memory” best practices

### 🔍 Observability  
- Logging using `logging` module  
- Supervisor traces overall execution steps

### 🧱 Deployment-Ready (Bonus Points)
Includes:
- **Dockerfile** for containerization  
- **FastAPI backend** (optional)  
- Deployable to **Vertex AI Agent Engine**  

### 💯 Kaggle-Friendly  
- Works **offline** inside Kaggle  
- No API keys needed  
- No paid services required  
- Fully reproducible

---
 🧩 **Architecture Diagram**

```text
                   ┌──────────────────────────┐
                   │      Supervisor Agent    │
                   │  (Central Orchestrator)  │
                   └──────────────┬───────────┘
                                  │
                ┌─────────────────┼───────────────────┐
                │                 │                   │
                ▼                 ▼                   ▼
     ┌─────────────────┐  ┌────────────────┐   ┌───────────────────┐
     │ Meal Planner    │  │ Shopping Agent │   │  Scheduler Agent  │
     │  Agent          │  │                │   │                   │
     └───────┬─────────┘  └──────┬───────-─┘   └──────────┬────────┘
             │                    │                       │
             ▼                    ▼                       ▼
      Meal Plan (JSON)     Shopping List (JSON)   Schedule (JSON)
             │                    │                       │
             └──────────┬────────┘                       │
                        ▼                                ▼
               ┌─────────────────┐             ┌────────────────────┐
               │ Task Manager    │             │  Reminder Agent    │
               │     Agent       │             │                    │
               └────────┬────────┘             └──────────┬─────────┘
                        │                                 │
                        ▼                                 ▼
                   Task List                         Reminder List
                        │                                 │
                        └───────┬─────────────────────────┘
                                ▼
                   ┌──────────────────────────┐
                   │       MemoryBank         │
                   │ (Long-Term User Memory)  │
                   └──────────────────────────┘


SMART-LIFE-ORGANIZER/
│
├── src/
│   ├── supervisor_agent.py
│   ├── agents/
│   │   ├── meal_planner.py
│   │   ├── shopping_agent.py
│   │   ├── scheduler_agent.py
│   │   ├── task_manager.py
│   │   └── reminder_agent.py
│   ├── tools/
│   │   └── json_store_tool.py
│   ├── memory/
│   │   └── memory_bank.py
│   └── observability/
│       └── logging.py
│
├── app/
│   └── api.py  (FastAPI optional)
│
├── deployment/
│   └── vertex_agent_engine_deploy.md
│
├── Dockerfile
├── requirements.txt
└── README.md

```

python3 src/supervisor_agent.py
 eg output:

 {
  "meal_plan": {...},
  "shopping_list": [...],
  "schedule": [...],
  "tasks": [...],
  "reminders": [...]
}



🐳 Running with Docker
docker build -t smart-life-organizer .
docker run -p 8000:8000 smart-life-organizer



⭐ Acknowledgements
This project was built as part of:
Google x Kaggle — AI Agents Intensive 2025
Huge thanks to the teaching team and agents community.

