import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../database/energy_db.sqlite")
    MODEL_PATH = os.getenv("MODEL_PATH", "./data/models/")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    
    # Model parameters
    LSTM_SEQUENCE_LENGTH = 24
    LSTM_EPOCHS = 30
    LSTM_BATCH_SIZE = 32
    
    XGBOOST_PARAMS = {
        'n_estimators': 100,
        'max_depth': 5,
        'learning_rate': 0.1,
        'subsample': 0.8
    }
    
    ARIMA_ORDER = (5, 1, 0)
    
    # API settings
    API_V1_PREFIX = "/api/v1"
    
settings = Settings()