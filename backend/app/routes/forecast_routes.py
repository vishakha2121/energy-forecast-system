from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timedelta
from typing import Optional
from app.services.forecast_service import ForecastService
from app.schemas.forecast_schema import ForecastRequest, ForecastResponse

router = APIRouter()
forecast_service = ForecastService()

@router.post("/predict", response_model=ForecastResponse)
async def predict_energy(request: ForecastRequest):
    """Get energy consumption forecast"""
    try:
        result = await forecast_service.predict(
            start_date=request.start_date,
            end_date=request.end_date,
            model_type=request.model_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_available_models():
    """Get list of available forecasting models"""
    return {
        "models": ["lstm", "xgboost", "arima", "ensemble"],
        "current_best": "ensemble"
    }

@router.get("/accuracy/{model_type}")
async def get_model_accuracy(model_type: str):
    """Get accuracy metrics for a specific model"""
    metrics = forecast_service.get_accuracy_metrics(model_type)
    return metrics

@router.get("/peak-prediction")
async def predict_peak_load(
    date: str = Query(..., description="Date for peak prediction (YYYY-MM-DD)")
):
    """Predict peak load for a specific date"""
    peak_info = await forecast_service.predict_peak_load(date)
    return peak_info

@router.post("/compare-models")
async def compare_models(
    start_date: str,
    end_date: str
):
    """Compare all models for the same time period"""
    comparison = await forecast_service.compare_all_models(start_date, end_date)
    return comparison