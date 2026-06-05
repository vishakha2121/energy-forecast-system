from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timedelta
from app.services.carbon_calculator import CarbonCalculator

router = APIRouter()
carbon_calculator = CarbonCalculator()

@router.get("/estimate")
async def estimate_carbon_impact(
    energy_consumption: float,
    timestamp: str = Query(None, description="ISO format timestamp")
):
    """Estimate carbon emissions for given energy consumption"""
    impact = carbon_calculator.calculate_emissions(energy_consumption, timestamp)
    return impact

@router.get("/forecast")
async def forecast_carbon_emissions(
    days: int = Query(7, ge=1, le=30)
):
    """Forecast carbon emissions for next N days"""
    forecast = await carbon_calculator.forecast_emissions(days)
    return forecast

@router.get("/intensity-factor")
async def get_carbon_intensity(
    region: str = "default"
):
    """Get current carbon intensity factor"""
    intensity = carbon_calculator.get_intensity_factor(region)
    return {"carbon_intensity_kgCO2_per_kWh": intensity}

@router.get("/recommendations")
async def get_reduction_recommendations(
    current_consumption: float
):
    """Get carbon reduction recommendations"""
    recommendations = carbon_calculator.get_recommendations(current_consumption)
    return {"recommendations": recommendations}