ENERGY_UNITS = {
    "kWh": "Kilowatt-hour",
    "MWh": "Megawatt-hour",
    "GWh": "Gigawatt-hour"
}

CARBON_FACTORS = {
    "coal": 0.85,
    "gas": 0.40,
    "nuclear": 0.05,
    "solar": 0.05,
    "wind": 0.01,
    "hydro": 0.02
}

MODEL_TYPES = ["lstm", "xgboost", "arima", "ensemble"]

GRID_OPTIMIZATION_GOALS = ["minimize_peak", "balance_load", "optimize_efficiency"]

DEFAULT_FORECAST_HOURS = 24
MAX_FORECAST_DAYS = 30