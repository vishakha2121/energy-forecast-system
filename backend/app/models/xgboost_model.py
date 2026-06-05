import xgboost as xgb
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from app.config import settings
import os

class XGBoostModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        
    def build_model(self):
        self.model = xgb.XGBRegressor(
            n_estimators=settings.XGBOOST_PARAMS['n_estimators'],
            max_depth=settings.XGBOOST_PARAMS['max_depth'],
            learning_rate=settings.XGBOOST_PARAMS['learning_rate'],
            subsample=settings.XGBOOST_PARAMS['subsample'],
            random_state=42,
            n_jobs=-1
        )
        return self.model
    
    def create_features(self, data):
        """Create features for XGBoost"""
        features = []
        for i in range(len(data)):
            features.append([
                data[i],  # current value
                data[i-1] if i > 0 else data[i],  # lag 1
                data[i-2] if i > 1 else data[i],  # lag 2
                data[i-3] if i > 2 else data[i],  # lag 3
                np.mean(data[max(0, i-24):i+1]),  # rolling mean 24h
                np.std(data[max(0, i-24):i+1]) if len(data[max(0, i-24):i+1]) > 1 else 0  # rolling std
            ])
        return np.array(features)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model
    
    def predict(self, X):
        return self.model.predict(X)
    
    def save(self, path):
        joblib.dump(self.model, os.path.join(path, 'xgboost_model.pkl'))
        joblib.dump(self.scaler, os.path.join(path, 'xgboost_scaler.pkl'))
    
    def load(self, path):
        self.model = joblib.load(os.path.join(path, 'xgboost_model.pkl'))
        self.scaler = joblib.load(os.path.join(path, 'xgboost_scaler.pkl'))