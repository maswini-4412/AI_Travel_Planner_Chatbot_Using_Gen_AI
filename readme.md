# ✈️ AI Travel Planner (Agentic AI with CrewAI + Gradio)

---

## 📌 Overview

The **AI Travel Planner** is a chatbot-based application that generates complete travel plans based on user input. It leverages a **multi-agent AI system (CrewAI)** to collaboratively provide:

* 🗺️ Travel routes
* 💰 Cost estimation
* 📅 Day-wise itinerary

The system integrates a **Gradio frontend** for interaction and a **Python backend powered by Groq LLM (LLaMA 3.3)**.

---

## 🎯 Objective

* Automate travel planning using AI agents
* Provide budget-friendly and optimized travel suggestions
* Demonstrate **Agentic AI architecture** in a real-world use case
* Reduce manual effort in itinerary planning

---

## 🚀 Key Features

* 🤖 Multi-agent system (CrewAI)
* 🧭 Smart route suggestions (bus/train/flight)
* 💸 Budget-based cost estimation
* 🗓️ Day-wise itinerary generation
* 💬 Chatbot interface (Gradio)
* ⚡ Fast response (typically < 1 minute)
* 🧩 Modular architecture (frontend + backend separation)

---

## 🏗️ Architecture

### 🔹 High-Level Flow

```text
User → Frontend (Gradio) → Backend → CrewAI Agents → LLM → Response → UI
```

### 🔹 Components

* **Frontend**: Handles user interaction (Gradio chatbot UI)
* **Backend**: Manages agents, tasks, and orchestration
* **LLM**: Groq (LLaMA 3.3) generates intelligent responses

### 🔹 Agents

* 🧭 **Route Agent** → Finds best travel routes
* 💰 **Cost Agent** → Estimates total trip cost
* 📅 **Planner Agent** → Creates itinerary

---

## 🛠️ Tech Stack

| Layer        | Technology                 |
| ------------ | -------------------------- |
| Frontend     | Gradio                     |
| Backend      | Python                     |
| AI Framework | CrewAI                     |
| LLM          | Groq (LLaMA 3.3)           |
| Environment  | Virtual Environment (venv) |

---

## ⚙️ Workflow

1. User enters travel query in UI
2. Frontend sends input to backend
3. Backend creates tasks for each agent
4. CrewAI executes tasks sequentially
5. LLM generates responses for each task
6. Final combined result is returned
7. UI displays the travel plan

---

## ▶️ Run Commands

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install gradio crewai python-dotenv
```

### 4. Add API Key (.env)

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run Application

```bash
python frontend.py
```

---

## 📊 Use Cases

* 🧳 Personal trip planning
* 🏢 Travel agency automation
* 💬 AI chatbot assistants
* 🌍 Tourism recommendation systems

---

## ⏱️ Performance

* Average response time: **30–60 seconds**
* Depends on:

  * API latency
  * Query complexity
  * Multi-agent processing

---

## 🔮 Future Enhancements

* 📊 Structured UI (cards for routes, cost, itinerary)
* 🌍 Google Maps integration
* 📄 Download itinerary as PDF
* 🎤 Voice input support
* ☁️ Cloud deployment (Hugging Face / AWS)

---

## 👩‍💻 Author

**Aswani**

---
 