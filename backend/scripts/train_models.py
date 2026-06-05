import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from app.services.data_preprocessor import DataPreprocessor
from app.models.lstm_model import LSTMModel
from app.models.xgboost_model import XGBoostModel
from app.models.arima_model import ARIMAModel
from app.config import settings

def train_all_models():
    print("Loading data...")
    preprocessor = DataPreprocessor()
    data = preprocessor.load_historical_data()
    
    print("Preparing features...")
    X_lstm, X_xgb, y = preprocessor.prepare_features(data)
    
    # Train LSTM (simplified for CPU)
    print("Training LSTM model...")
    lstm = LSTMModel()
    input_shape = (X_lstm.shape[1], X_lstm.shape[2])
    lstm.build_model(input_shape)
    
    # Split data
    split_idx = int(len(X_lstm) * 0.8)
    X_train, X_val = X_lstm[:split_idx], X_lstm[split_idx:]
    y_train, y_val = y[:split_idx], y[split_idx:]
    
    lstm.train(X_train, y_train, X_val, y_val)
    lstm.save(settings.MODEL_PATH)
    print("LSTM model saved!")
    
    # Train XGBoost
    print("Training XGBoost model...")
    xgb = XGBoostModel()
    xgb.build_model()
    
    # Create features for XGBoost
    X_xgb_features = xgb.create_features(y[:len(X_xgb)])
    split_idx_xgb = int(len(X_xgb_features) * 0.8)
    X_train_xgb = X_xgb_features[:split_idx_xgb]
    y_train_xgb = y[:split_idx_xgb]
    
    xgb.train(X_train_xgb, y_train_xgb)
    xgb.save(settings.MODEL_PATH)
    print("XGBoost model saved!")
    
    # Train ARIMA
    print("Training ARIMA model...")
    arima = ARIMAModel()
    arima.train(y)
    arima.save(settings.MODEL_PATH)
    print("ARIMA model saved!")
    
    print("All models trained successfully!")

if __name__ == "__main__":
    train_all_models()