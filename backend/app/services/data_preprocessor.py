import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import random

class DataPreprocessor:
    def __init__(self):
        self.scaler = MinMaxScaler()
        
    def load_historical_data(self):
        """Load or generate historical energy data"""
        # Generate sample data for demonstration
        dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='H')
        
        # Create base pattern with seasonality
        hours = dates.hour
        day_of_week = dates.dayofweek
        month = dates.month
        
        # Base consumption pattern
        base_consumption = 500 + 200 * np.sin(2 * np.pi * hours / 24)  # Daily pattern
        weekly_pattern = 50 * np.sin(2 * np.pi * day_of_week / 7)  # Weekly pattern
        seasonal_pattern = 100 * np.sin(2 * np.pi * month / 12)  # Seasonal pattern
        
        # Add noise
        noise = np.random.normal(0, 30, len(dates))
        
        energy_consumption = base_consumption + weekly_pattern + seasonal_pattern + noise
        energy_consumption = np.maximum(energy_consumption, 200)  # Minimum consumption
        
        # Create temperature data (correlated with consumption)
        temperature = 20 + 10 * np.sin(2 * np.pi * (month - 6) / 12) + np.random.normal(0, 5, len(dates))
        
        data = pd.DataFrame({
            'timestamp': dates,
            'energy_consumption': energy_consumption,
            'temperature': temperature,
            'humidity': 60 + 20 * np.sin(2 * np.pi * hours / 24) + np.random.normal(0, 10, len(dates)),
            'day_of_week': day_of_week,
            'is_holiday': [1 if d.weekday() >= 5 else 0 for d in dates],
            'hour': hours,
            'month': month
        })
        
        return data
    
    def prepare_features(self, data):
        """Prepare features for model training"""
        
        # Ensure data is sorted
        data = data.sort_values('timestamp')
        
        # Create lag features
        for lag in range(1, 25):
            data[f'lag_{lag}'] = data['energy_consumption'].shift(lag)
        
        # Create rolling statistics
        data['rolling_mean_24'] = data['energy_consumption'].rolling(window=24).mean()
        data['rolling_std_24'] = data['energy_consumption'].rolling(window=24).std()
        
        # Drop NaN values
        data = data.dropna()
        
        # Select features
        feature_columns = ['temperature', 'humidity', 'day_of_week', 'is_holiday', 'hour', 'month']
        feature_columns += [f'lag_{i}' for i in range(1, 25)]
        feature_columns += ['rolling_mean_24', 'rolling_std_24']
        
        # Scale features
        X = data[feature_columns].values
        X_scaled = self.scaler.fit_transform(X)
        
        y = data['energy_consumption'].values
        
        # Prepare for LSTM (3D: samples, timesteps, features)
        sequence_length = 24
        X_lstm = []
        for i in range(len(X_scaled) - sequence_length):
            X_lstm.append(X_scaled[i:i + sequence_length])
        X_lstm = np.array(X_lstm)
        
        # Prepare for XGBoost (2D)
        X_xgb = X_scaled
        
        return X_lstm, X_xgb, y
    
    def inverse_transform(self, scaled_data):
        """Inverse transform scaled data"""
        # Create dummy array for inverse transform
        dummy = np.zeros((len(scaled_data), self.scaler.scale_.shape[0]))
        dummy[:, 0] = scaled_data.flatten()
        return self.scaler.inverse_transform(dummy)[:, 0]
    
    def handle_missing_values(self, data):
        """Handle missing values in dataset"""
        data = data.fillna(method='ffill')
        data = data.fillna(method='bfill')
        return data
    
    def detect_anomalies(self, data, threshold=3):
        """Detect anomalies in energy consumption"""
        mean = data['energy_consumption'].mean()
        std = data['energy_consumption'].std()
        
        anomalies = data[abs(data['energy_consumption'] - mean) > threshold * std]
        
        return anomalies