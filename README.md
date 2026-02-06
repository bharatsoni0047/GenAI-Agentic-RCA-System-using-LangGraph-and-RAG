# 🚀 GenAI Agentic RCA System (LangGraph + RAG)

---

## 📌 1. Project Title
**GenAI Agentic RCA System using LangGraph and RAG**

---

## 📖 2. Description
This project is an **AI-powered Root Cause Analysis (RCA) system**.

It takes system errors or incident descriptions as input and automatically:
- Finds the **root cause**
- Explains the **impact**
- Suggests the **best possible fix**

The system is built using **agent-based workflows** and **Retrieval-Augmented Generation (RAG)** to ensure reliable and grounded AI responses.

---

## ✨ 3. Features
- 🤖 AI agent for automated root cause analysis  
- 🔍 Searches past incidents using semantic search  
- 🧠 Uses LLMs to generate clear RCA insights  
- 🔁 Agent validation and retry mechanism  
- 🌐 REST API support using FastAPI  
- 📊 Agentic workflow orchestration with LangGraph  

---

## 🛠️ 4. Tech Stack
- **Python** – Core programming language  
- **LangGraph** – Agent workflow orchestration  
- **LangChain** – LLM and retrieval management  
- **ChromaDB** – Vector database for semantic search  
- **FastAPI** – API framework  
- **RAG (Retrieval-Augmented Generation)** – Grounded AI responses  

---


## 🗂️ 5. Project Structure
##GenAI-Agentic-RCA-System/

│── data/ # Logs, sample incidents, datasets
│── rca_agent/ # Agent logic and workflows
│── main.py # FastAPI application entry point
│── requirements.txt # Project dependencies
│── README.md # Project documentation

---

## ⚙️ 6. Installation
### Step 1: Clone the repository

git clone https://github.com/bharatsoni0047/GenAI-Agentic-RCA-System-using-LangGraph-and-RAG.git
cd GenAI-Agentic-RCA-System-using-LangGraph-and-RAG

### Step 2: Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Run the application
uvicorn main:app --reload

---

## ▶️ 7. Usage

-Start the FastAPI server
-Send an error or incident description via API
-The system returns:
-Root Cause
-Impact
-Recommended Fix
-Use the response for faster debugging and incident resolution
