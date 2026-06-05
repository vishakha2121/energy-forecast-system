#!/usr/bin/env python3
"""
Train all ML models for energy forecasting
"""

import sys
import os
import numpy as np
import pandas as pd

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.data_preprocessor import DataPreprocessor
from app.models.lstm_model import LSTMModel
from app.models.xgboost_model import XGBoostModel
from app.models.arima_model import ARIMAModel
from app.models.ensemble_model import EnsembleModel
from app.config import settings

def create_directories():
    """Create necessary directories"""
    dirs = [
        'backend/data/raw',
        'backend/data/processed', 
        'backend/data/models',
        'backend/notebooks'
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def train_lstm_model(X_train, y_train, X_val, y_val):
    """Train LSTM model"""
    print("\n🔷 Training LSTM Model...")
    lstm = LSTMModel()
    
    # Build model
    input_shape = (X_train.shape[1], X_train.shape[2])
    lstm.build_model(input_shape)
    
    # Train
    history = lstm.train(X_train, y_train, X_val, y_val)
    
    # Save
    lstm.save(settings.MODEL_PATH)
    print("✅ LSTM model saved!")
    
    return lstm, history

def train_xgboost_model(X_train, y_train):
    """Train XGBoost model"""
    print("\n🔷 Training XGBoost Model...")
    xgb = XGBoostModel()
    xgb.build_model()
    
    # Create features
    X_train_features = xgb.create_features(y_train)
    
    # Train
    xgb.train(X_train_features, y_train)
    
    # Save
    xgb.save(settings.MODEL_PATH)
    print("✅ XGBoost model saved!")
    
    return xgb

def train_arima_model(data):
    """Train ARIMA model"""
    print("\n🔷 Training ARIMA Model...")
    arima = ARIMAModel()
    
    # Make data stationary if needed
    stationary_data = arima.make_stationary(data)
    
    # Train
    arima.train(stationary_data)
    
    # Save
    arima.save(settings.MODEL_PATH)
    print("✅ ARIMA model saved!")
    
    return arima

def evaluate_models(models, X_test, y_test):
    """Evaluate trained models"""
    print("\n📊 Evaluating Models...")
    
    results = {}
    
    for name, model in models.items():
        if name == 'lstm':
            # Prepare test data for LSTM
            pred = model.predict(X_test)
            mae = np.mean(np.abs(pred.flatten() - y_test[:len(pred)]))
            rmse = np.sqrt(np.mean((pred.flatten() - y_test[:len(pred)]) ** 2))
            
        elif name == 'xgboost':
            X_test_features = model.create_features(y_test)
            pred = model.predict(X_test_features)
            mae = np.mean(np.abs(pred - y_test[:len(pred)]))
            rmse = np.sqrt(np.mean((pred - y_test[:len(pred)]) ** 2))
            
        elif name == 'arima':
            pred = model.predict(len(y_test))
            mae = np.mean(np.abs(pred - y_test[:len(pred)]))
            rmse = np.sqrt(np.mean((pred - y_test[:len(pred)]) ** 2))
        
        results[name] = {'mae': mae, 'rmse': rmse}
        print(f"  {name.upper()}: MAE={mae:.2f}, RMSE={rmse:.2f}")
    
    return results

def main():
    print("🚀 Starting Model Training Pipeline...")
    
    # Create directories
    create_directories()
    
    # Load and preprocess data
    print("\n📁 Loading and preprocessing data...")
    preprocessor = DataPreprocessor()
    data = preprocessor.load_historical_data()
    X_lstm, X_xgb, y = preprocessor.prepare_features(data)
    
    # Split data
    split_idx = int(len(X_lstm) * 0.8)
    X_train_lstm, X_val_lstm = X_lstm[:split_idx], X_lstm[split_idx:]
    y_train, y_val = y[:split_idx], y[split_idx:]
    
    # Train models
    models = {}
    
    # Train LSTM
    lstm, history = train_lstm_model(X_train_lstm, y_train, X_val_lstm, y_val)
    models['lstm'] = lstm
    
    # Train XGBoost
    xgb = train_xgboost_model(y_train[:len(X_train_lstm)], y_train[:len(X_train_lstm)])
    models['xgboost'] = xgb
    
    # Train ARIMA
    arima = train_arima_model(y)
    models['arima'] = arima
    
    # Evaluate models
    results = evaluate_models(models, X_val_lstm, y_val)
    
    # Create and train ensemble
    print("\n🔷 Creating Ensemble Model...")
    ensemble = EnsembleModel()
    for name, model in models.items():
        ensemble.add_model(name, model)
    ensemble.save(settings.MODEL_PATH)
    print("✅ Ensemble model saved!")
    
    print("\n" + "="*50)
    print("🎉 Model Training Complete!")
    print("="*50)
    print("\n📈 Best Model Performance:")
    best_model = min(results, key=lambda x: results[x]['mae'])
    print(f"  {best_model.upper()}: MAE={results[best_model]['mae']:.2f}, RMSE={results[best_model]['rmse']:.2f}")

if __name__ == "__main__":
    main()