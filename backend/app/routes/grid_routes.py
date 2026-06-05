from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict
from app.services.grid_optimizer import GridOptimizer

router = APIRouter()
grid_optimizer = GridOptimizer()

class OptimizationRequest(BaseModel):
    current_load: List[float]
    forecasted_load: List[float]
    optimization_goal: str = "minimize_peak"

@router.post("/optimize")
async def optimize_grid(request: OptimizationRequest):
    """Optimize grid load distribution"""
    try:
        result = grid_optimizer.optimize(
            current_load=request.current_load,
            forecasted_load=request.forecasted_load,
            goal=request.optimization_goal
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/simulation")
async def run_simulation(
    scenario: str = "peak_load_reduction"
):
    """Run grid optimization simulation"""
    simulation_result = await grid_optimizer.run_simulation(scenario)
    return simulation_result

@router.get("/load-balancing")
async def get_load_balancing_strategy(
    current_peak: float,
    capacity: float
):
    """Get load balancing recommendations"""
    strategy = grid_optimizer.balance_load(current_peak, capacity)
    return strategy

@router.post("/what-if")
async def what_if_analysis(
    load_changes: Dict[str, float]
):
    """Run what-if analysis for load changes"""
    analysis = await grid_optimizer.what_if_analysis(load_changes)
    return analysis