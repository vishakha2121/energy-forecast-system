from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EnergyData(Base):
    __tablename__ = "energy_data"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    energy_consumption = Column(Float, nullable=False)
    temperature = Column(Float)
    humidity = Column(Float)
    day_of_week = Column(Integer)
    is_holiday = Column(Integer)
    peak_load = Column(Float)

class ForecastResult(Base):
    __tablename__ = "forecast_results"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    model_used = Column(String, nullable=False)
    predicted_value = Column(Float, nullable=False)
    actual_value = Column(Float)
    confidence_interval_lower = Column(Float)
    confidence_interval_upper = Column(Float)

class GridOptimization(Base):
    __tablename__ = "grid_optimizations"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    load_before = Column(JSON)
    load_after = Column(JSON)
    optimization_strategy = Column(String)
    energy_saved = Column(Float)

class CarbonEmission(Base):
    __tablename__ = "carbon_emissions"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False)
    energy_consumption = Column(Float)
    carbon_intensity = Column(Float)
    co2_emissions = Column(Float)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()