# 🧪 Blood Test Report Analyzer (CrewAI + FastAPI)

A multi-agent medical assistant that analyzes uploaded blood test reports using large language models. Built with [CrewAI](https://docs.crewai.com/), [FastAPI](https://fastapi.tiangolo.com/), [Redis Queue (RQ)](https://python-rq.org/), and SQLite for persistent storage.

---

## 🚀 Features

✅ Multi-agent LLM system using CrewAI  
✅ Upload PDF blood reports for automated analysis  
✅ Concurrent request handling with Redis Queue (RQ)  
✅ Persistent analysis result storage via SQLite database  
✅ RESTful API with FastAPI  
✅ Modular, extensible codebase  
✅ Ethical, medically relevant outputs  

---

## 📁 Project Structure

├── main.py # FastAPI app for report upload & API
├── worker.py # Background job worker using Redis Queue
├── agents.py # LLM agent definitions (doctor, nutritionist, etc.)
├── task.py # Task definitions for each agent
├── tools.py # Tools for reading PDFs and processing reports
├── models.py # SQLAlchemy ORM model
├── db.py # Database initialization and session setup
├── data/ # Folder for uploaded blood report PDFs
├── requirements.txt # Python dependencies

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/blood-analyzer-crewai.git
cd blood-analyzer-crewai

### 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate 

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add .env File with OpenAI Key
OPENAI_API_KEY=your-openai-api-key


## 🧠 How It Works
User uploads a blood report PDF to /analyze endpoint.

The file is saved and a background job is queued via Redis Queue (RQ).

CrewAI launches 4 agents:

🧑‍⚕️ Doctor (medical interpretation)

🥦 Nutritionist (diet & supplement suggestions)

🏋️ Exercise Coach (fitness plan based on health markers)

📋 Verifier (checks if it's a valid blood report)

Each agent performs its task and results are stored in a SQLite database.

## 🛠️ Running the Application

### Step 1: Start Redis Server
Make sure you have Redis installed. Then:

redis-server

### Step 2: Run the RQ Worker

rq worker

### Step 3: Run the FastAPI App

uvicorn main:app --reload

## 📤 Sample API Request (Using curl)

curl -X POST "http://localhost:8000/analyze" \
  -F "file=@path/to/your_blood_report.pdf" \
  -F "query=Summarize my blood report"

## Sample JSON response:

{
  "status": "queued",
  "message": "Your report is being analyzed. Check back shortly.",
  "file": "your_blood_report.pdf"
}

## ✅ Bugs Fixed

File	Fix Description
agents.py	Fixed incorrect tool usage, llm=llm bug, updated agents to be medically safe
task.py	Rewritten for medically appropriate and query-aligned tasks
tools.py	Added PDF loading, real logic in nutrition & exercise tools, error handling
main.py	Integrated Redis queue, background processing, multi-agent support
models.py	Added for saving report results in database
worker.py	Processes jobs in background via RQ
db.py	Initializes SQLite database with SQLAlchemy

## 🎁 Bonus Features Implemented
✅ Queue Worker Model using Redis + RQ

✅ Database Integration using SQLAlchemy + SQLite