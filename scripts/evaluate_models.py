#!/usr/bin/env python3
"""
Evaluate and compare all trained models
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.data_preprocessor import DataPreprocessor
from app.models.lstm_model import LSTMModel
from app.models.xgboost_model import XGBoostModel
from app.models.arima_model import ARIMAModel
from app.models.ensemble_model import EnsembleModel
from app.config import settings

def load_models():
    """Load all trained models"""
    print("📁 Loading trained models...")
    
    models = {}
    
    # Load LSTM
    try:
        lstm = LSTMModel()
        lstm.load(settings.MODEL_PATH)
        models['lstm'] = lstm
        print("✅ LSTM model loaded")
    except Exception as e:
        print(f"❌ Failed to load LSTM: {e}")
    
    # Load XGBoost
    try:
        xgb = XGBoostModel()
        xgb.load(settings.MODEL_PATH)
        models['xgboost'] = xgb
        print("✅ XGBoost model loaded")
    except Exception as e:
        print(f"❌ Failed to load XGBoost: {e}")
    
    # Load ARIMA
    try:
        arima = ARIMAModel()
        arima.load(settings.MODEL_PATH)
        models['arima'] = arima
        print("✅ ARIMA model loaded")
    except Exception as e:
        print(f"❌ Failed to load ARIMA: {e}")
    
    return models

def calculate_metrics(y_true, y_pred):
    """Calculate evaluation metrics"""
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    r2 = r2_score(y_true, y_pred)
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape,
        'R2': r2
    }

def evaluate_models(models, X_test, y_test):
    """Evaluate all models on test data"""
    print("\n📊 Evaluating models...")
    
    results = {}
    predictions = {}
    
    for name, model in models.items():
        print(f"\n  Evaluating {name.upper()}...")
        
        try:
            if name == 'lstm':
                pred = model.predict(X_test).flatten()
                y_true = y_test[:len(pred)]
                
            elif name == 'xgboost':
                X_test_features = model.create_features(y_test)
                pred = model.predict(X_test_features)
                y_true = y_test[:len(pred)]
                
            elif name == 'arima':
                pred = model.predict(len(y_test))
                y_true = y_test[:len(pred)]
            
            metrics = calculate_metrics(y_true, pred)
            results[name] = metrics
            predictions[name] = pred
            
            print(f"    MAE: {metrics['MAE']:.2f}")
            print(f"    RMSE: {metrics['RMSE']:.2f}")
            print(f"    MAPE: {metrics['MAPE']:.2f}%")
            print(f"    R2: {metrics['R2']:.4f}")
            
        except Exception as e:
            print(f"    ❌ Error: {e}")
            results[name] = None
    
    return results, predictions

def plot_results(predictions, y_true):
    """Plot prediction results"""
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    colors = {'lstm': 'blue', 'xgboost': 'green', 'arima': 'orange', 'ensemble': 'red'}
    
    for idx, (name, pred) in enumerate(predictions.items()):
        if idx < 4 and pred is not None:
            ax = axes[idx]
            ax.plot(y_true[:len(pred)], label='Actual', color='black', linewidth=2)
            ax.plot(pred, label=f'{name.upper()} Prediction', color=colors.get(name, 'gray'), 
                   linestyle='--', alpha=0.7)
            ax.set_title(f'{name.upper()} Model Performance')
            ax.set_xlabel('Time Steps')
            ax.set_ylabel('Energy Consumption (kWh)')
            ax.legend()
            ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('backend/data/models/evaluation_plot.png', dpi=100)
    print("\n📈 Evaluation plot saved to backend/data/models/evaluation_plot.png")
    plt.show()

def create_comparison_table(results):
    """Create comparison table of all models"""
    
    df = pd.DataFrame(results).T
    df = df.round(2)
    
    print("\n" + "="*60)
    print("MODEL COMPARISON TABLE")
    print("="*60)
    print(df.to_string())
    
    # Save to CSV
    df.to_csv('backend/data/models/model_comparison.csv')
    print("\n📊 Comparison table saved to backend/data/models/model_comparison.csv")
    
    # Find best model
    best_model = df['MAE'].idxmin()
    print(f"\n🏆 Best Model: {best_model.upper()} (Lowest MAE: {df.loc[best_model, 'MAE']:.2f})")

def main():
    print("🚀 Starting Model Evaluation...")
    
    # Load data
    print("\n📁 Loading test data...")
    preprocessor = DataPreprocessor()
    data = preprocessor.load_historical_data()
    X_lstm, X_xgb, y = preprocessor.prepare_features(data)
    
    # Use last 20% for testing
    split_idx = int(len(X_lstm) * 0.8)
    X_test_lstm = X_lstm[split_idx:]
    y_test = y[split_idx:]
    
    # Load models
    models = load_models()
    
    if not models:
        print("❌ No models found. Please train models first using train_models.py")
        return
    
    # Evaluate models
    results, predictions = evaluate_models(models, X_test_lstm, y_test)
    
    # Create ensemble predictions
    print("\n🔷 Creating Ensemble Predictions...")
    ensemble = EnsembleModel()
    for name, model in models.items():
        ensemble.add_model(name, model)
    
    # Get ensemble predictions
    ensemble_pred = []
    for i in range(len(y_test)):
        # Simplified ensemble prediction
        preds = []
        for name, model in models.items():
            if name == 'lstm' and i < len(X_test_lstm):
                preds.append(model.predict(X_test_lstm[i:i+1]).flatten()[0])
            elif name == 'xgboost':
                X_feat = model.create_features(y_test[:i+1])
                if len(X_feat) > 0:
                    preds.append(model.predict(X_feat[-1:])[0])
            elif name == 'arima' and i < 100:
                preds.append(model.predict(1)[0] if hasattr(model, 'predict') else 0)
        
        if preds:
            ensemble_pred.append(np.mean(preds))
        else:
            ensemble_pred.append(y_test[i])
    
    predictions['ensemble'] = np.array(ensemble_pred)
    ensemble_metrics = calculate_metrics(y_test[:len(ensemble_pred)], ensemble_pred)
    results['ensemble'] = ensemble_metrics
    
    print(f"\n  ENSEMBLE:")
    print(f"    MAE: {ensemble_metrics['MAE']:.2f}")
    print(f"    RMSE: {ensemble_metrics['RMSE']:.2f}")
    print(f"    MAPE: {ensemble_metrics['MAPE']:.2f}%")
    print(f"    R2: {ensemble_metrics['R2']:.4f}")
    
    # Plot results
    plot_results(predictions, y_test)
    
    # Create comparison table
    create_comparison_table(results)
    
    print("\n" + "="*50)
    print("🎉 Evaluation Complete!")
    print("="*50)

if __name__ == "__main__":
    main()