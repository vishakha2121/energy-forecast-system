from datetime import datetime
import numpy as np

def format_datetime(dt):
    """Format datetime to ISO string"""
    if isinstance(dt, datetime):
        return dt.isoformat()
    return dt

def calculate_accuracy(actual, predicted):
    """Calculate accuracy metrics"""
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    return {
        "mae": round(mae, 2),
        "rmse": round(rmse, 2),
        "mape": round(mape, 2)
    }

def validate_date_range(start_date, end_date):
    """Validate date range"""
    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)
    
    if start > end:
        raise ValueError("Start date must be before end date")
    
    if (end - start).days > 30:
        raise ValueError("Date range cannot exceed 30 days")
    
    return start, end