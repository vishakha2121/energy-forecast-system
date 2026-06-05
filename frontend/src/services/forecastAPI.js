import api from './api';

export const forecastAPI = {
  // Get forecast for date range
  getForecast: (startDate, endDate, modelType = 'ensemble') => {
    return api.post('/forecast/predict', {
      start_date: startDate,
      end_date: endDate,
      model_type: modelType
    });
  },

  // Get available models
  getModels: () => {
    return api.get('/forecast/models');
  },

  // Get model accuracy metrics
  getAccuracy: (modelType) => {
    return api.get(`/forecast/accuracy/${modelType}`);
  },

  // Predict peak load for specific date
  predictPeakLoad: (date) => {
    return api.get(`/forecast/peak-prediction?date=${date}`);
  },

  // Compare all models
  compareModels: (startDate, endDate) => {
    return api.post('/forecast/compare-models', null, {
      params: { start_date: startDate, end_date: endDate }
    });
  },

  // Get current forecast (for dashboard)
  getCurrentForecast: () => {
    const now = new Date();
    const endDate = new Date(now);
    endDate.setHours(now.getHours() + 24);
    
    return api.post('/forecast/predict', {
      start_date: now.toISOString(),
      end_date: endDate.toISOString(),
      model_type: 'ensemble'
    });
  }
};