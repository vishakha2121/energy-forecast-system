import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

class EnsembleModel:
    def __init__(self):
        self.models = {}
        self.weights = {
            'lstm': 0.4,
            'xgboost': 0.4,
            'arima': 0.2
        }
    
    def add_model(self, name, model):
        self.models[name] = model
    
    def predict(self, X_lstm, X_xgb, arima_steps):
        predictions = {}
        
        # LSTM prediction
        if 'lstm' in self.models and self.models['lstm']:
            lstm_pred = self.models['lstm'].predict(X_lstm).flatten()
            predictions['lstm'] = lstm_pred
        
        # XGBoost prediction
        if 'xgboost' in self.models and self.models['xgboost']:
            xgb_pred = self.models['xgboost'].predict(X_xgb)
            predictions['xgboost'] = xgb_pred
        
        # ARIMA prediction
        if 'arima' in self.models and self.models['arima']:
            arima_pred = self.models['arima'].predict(arima_steps)
            predictions['arima'] = arima_pred
        
        # Ensemble prediction (weighted average)
        ensemble_pred = np.zeros(len(list(predictions.values())[0]))
        total_weight = 0
        
        for model_name, pred in predictions.items():
            weight = self.weights.get(model_name, 0.33)
            ensemble_pred += pred * weight
            total_weight += weight
        
        ensemble_pred = ensemble_pred / total_weight
        
        return {
            'ensemble': ensemble_pred,
            'individual': predictions
        }
    
    def update_weights(self, actual, predictions):
        """Dynamic weight updating based on recent performance"""
        errors = {}
        for model_name, pred in predictions.items():
            mae = mean_absolute_error(actual[:len(pred)], pred)
            errors[model_name] = mae
        
        total_error = sum(errors.values())
        if total_error > 0:
            new_weights = {}
            for model_name, error in errors.items():
                new_weights[model_name] = 1 - (error / total_error)
            
            # Normalize
            weight_sum = sum(new_weights.values())
            for model_name in new_weights:
                new_weights[model_name] /= weight_sum
            
            self.weights.update(new_weights)
        
        return self.weights
    
    def save(self, path):
        joblib.dump(self.weights, f"{path}/ensemble_weights.pkl")
    
    def load(self, path):
        self.weights = joblib.load(f"{path}/ensemble_weights.pkl")