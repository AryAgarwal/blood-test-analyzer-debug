

from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ReportAnalysis(Base):
    __tablename__ = "report_analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String)
    query = Column(Text)
    analysis_result = Column(Text)
    saved_path = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
