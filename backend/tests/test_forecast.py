import pytest
from app.services.forecast_service import ForecastService

def test_forecast_service_initialization():
    service = ForecastService()
    assert service is not None

def test_predict_peak_load():
    service = ForecastService()
    # Add test logic here
    pass