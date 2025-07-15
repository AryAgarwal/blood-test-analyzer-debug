

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os, uuid
from db import init_db
from models import ReportAnalysis
from worker import process_report_job
from rq import Queue
from redis import Redis

# CrewAI
from crewai import Crew, Process
from agents import doctor, nutritionist, exercise_specialist, verifier
from task import help_patients, nutrition_analysis, exercise_planning, verification

app = FastAPI(title="Blood Test Report Analyzer")

# Initialize Redis Queue
redis_conn = Redis()
queue = Queue(connection=redis_conn)

# DB setup
init_db()

def run_crew(query: str, file_path: str):
    """Run CrewAI pipeline with all agents"""
    crew = Crew(
        agents=[doctor, nutritionist, exercise_specialist, verifier],
        tasks=[verification, help_patients, nutrition_analysis, exercise_planning],
        process=Process.sequential,
    )
    return crew.kickoff(inputs={'query': query, 'file_path': file_path})

@app.get("/")
async def root():
    return {"message": "Blood Test Analyzer API is running."}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarize my blood report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    os.makedirs("data", exist_ok=True)

    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Enqueue background job
        queue.enqueue(process_report_job, file_path, query, file.filename)

        return {
            "status": "queued",
            "message": "Your report is being analyzed. Check back shortly.",
            "file": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
