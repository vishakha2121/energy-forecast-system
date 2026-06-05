from pydantic import BaseModel
from typing import List, Dict, Optional

class OptimizationRequest(BaseModel):
    current_load: List[float]
    forecasted_load: List[float]
    optimization_goal: str = "minimize_peak"

class OptimizationResponse(BaseModel):
    strategy: str
    original_peak: float
    optimized_peak: float
    reduction_percentage: float
    recommendations: List[str]
    optimized_load: List[float]