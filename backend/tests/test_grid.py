import pytest
from app.services.grid_optimizer import GridOptimizer

def test_grid_optimizer():
    optimizer = GridOptimizer()
    assert optimizer.grid_capacity == 1000