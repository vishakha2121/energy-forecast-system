from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ForecastRequest(BaseModel):
    start_date: str
    end_date: str
    model_type: str = "ensemble"  # lstm, xgboost, arima, ensemble

class ForecastResponse(BaseModel):
    dates: List[str]
    values: List[float]
    model_used: str
    unit: str = "kWh"
    
class AccuracyMetrics(BaseModel):
    mae: float
    rmse: float
    mape: float