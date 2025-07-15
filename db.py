

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# SQLite DB (you can switch to PostgreSQL for production)
DATABASE_URL = "sqlite:///./blood_reports.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
