import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

class EnergyModel:
    """Base Energy Model Class for handling common operations"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_columns = [
            'hour', 'day_of_week', 'month', 'is_holiday',
            'temperature', 'humidity', 'lag_1', 'lag_2', 
            'lag_3', 'lag_24', 'rolling_mean_24'
        ]
        
    def create_features(self, df):
        """Create time-based features from datetime"""
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.dayofweek
            df['month'] = df['timestamp'].dt.month
            df['weekend'] = (df['day_of_week'] >= 5).astype(int)
        
        return df
    
    def create_lag_features(self, df, target_col='energy_consumption', lags=[1, 2, 3, 24]):
        """Create lag features for time series"""
        for lag in lags:
            df[f'lag_{lag}'] = df[target_col].shift(lag)
        return df
    
    def create_rolling_features(self, df, target_col='energy_consumption', windows=[24]):
        """Create rolling statistics features"""
        for window in windows:
            df[f'rolling_mean_{window}'] = df[target_col].rolling(window=window).mean()
            df[f'rolling_std_{window}'] = df[target_col].rolling(window=window).std()
        return df
    
    def prepare_data(self, df):
        """Prepare data for training"""
        df = self.create_features(df)
        df = self.create_lag_features(df)
        df = self.create_rolling_features(df)
        
        # Drop rows with NaN values
        df = df.dropna()
        
        # Select features
        available_features = [col for col in self.feature_columns if col in df.columns]
        X = df[available_features].values
        y = df['energy_consumption'].values
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y, available_features
    
    def train_random_forest(self, X, y):
        """Train Random Forest model as baseline"""
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X, y)
        return self.model
    
    def predict(self, X):
        """Make predictions"""
        if self.model is None:
            raise ValueError("Model not trained yet!")
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def save(self, path):
        """Save model and scaler"""
        os.makedirs(path, exist_ok=True)
        joblib.dump(self.model, os.path.join(path, 'energy_model.pkl'))
        joblib.dump(self.scaler, os.path.join(path, 'energy_scaler.pkl'))
        joblib.dump(self.feature_columns, os.path.join(path, 'features.pkl'))
    
    def load(self, path):
        """Load model and scaler"""
        self.model = joblib.load(os.path.join(path, 'energy_model.pkl'))
        self.scaler = joblib.load(os.path.join(path, 'energy_scaler.pkl'))
        self.feature_columns = joblib.load(os.path.join(path, 'features.pkl'))
    
    def get_feature_importance(self):
        """Get feature importance if using tree-based model"""
        if hasattr(self.model, 'feature_importances_'):
            importance = dict(zip(self.feature_columns, self.model.feature_importances_))
            return sorted(importance.items(), key=lambda x: x[1], reverse=True)
        return []