import os
from main import run_crew
from db import SessionLocal
from models import ReportAnalysis

def process_report_job(file_path: str, query: str, original_filename: str):
    """Background job to analyze blood report and save to DB"""
    result = run_crew(query=query, file_path=file_path)

    # Save result to DB
    db = SessionLocal()
    report = ReportAnalysis(
        original_filename=original_filename,
        query=query,
        analysis_result=result,
        saved_path=file_path
    )
    db.add(report)
    db.commit()
    db.close()

    return str(result)
