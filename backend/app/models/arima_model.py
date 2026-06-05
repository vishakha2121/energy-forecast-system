from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
import joblib
from app.config import settings
import os
import warnings
warnings.filterwarnings('ignore')

class ARIMAModel:
    def __init__(self):
        self.model = None
        self.order = settings.ARIMA_ORDER
        
    def check_stationarity(self, data):
        result = adfuller(data)
        return result[1] < 0.05  # p-value < 0.05 means stationary
    
    def make_stationary(self, data):
        if not self.check_stationarity(data):
            return np.diff(data)
        return data
    
    def train(self, data):
        try:
            self.model = ARIMA(data, order=self.order)
            self.fitted_model = self.model.fit()
            return self.fitted_model
        except Exception as e:
            print(f"ARIMA training error: {e}")
            return None
    
    def predict(self, steps):
        if self.fitted_model:
            forecast = self.fitted_model.forecast(steps=steps)
            return forecast
        return np.zeros(steps)
    
    def save(self, path):
        joblib.dump(self.fitted_model, os.path.join(path, 'arima_model.pkl'))
    
    def load(self, path):
        self.fitted_model = joblib.load(os.path.join(path, 'arima_model.pkl'))