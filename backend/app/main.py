from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import forecast_routes, grid_routes, carbon_routes, gemini_routes
from app.database import init_db
from app.config import settings

app = FastAPI(
    title="Energy Load Forecasting & Smart Grid Optimization System",
    description="AI-powered energy forecasting system with LSTM, XGBoost, and ARIMA",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Register routes
app.include_router(forecast_routes.router, prefix=f"{settings.API_V1_PREFIX}/forecast", tags=["Forecast"])
app.include_router(grid_routes.router, prefix=f"{settings.API_V1_PREFIX}/grid", tags=["Grid Optimization"])
app.include_router(carbon_routes.router, prefix=f"{settings.API_V1_PREFIX}/carbon", tags=["Carbon Impact"])
app.include_router(gemini_routes.router, prefix=f"{settings.API_V1_PREFIX}/gemini", tags=["Gemini AI"])

@app.get("/")
def root():
    return {
        "message": "Energy Load Forecasting System",
        "status": "running",
        "models": ["LSTM", "XGBoost", "ARIMA", "Ensemble"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}