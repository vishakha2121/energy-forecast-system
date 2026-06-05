import api from './api';

export const carbonAPI = {
  // Estimate carbon impact
  estimateImpact: (energyConsumption, timestamp = null) => {
    return api.get('/carbon/estimate', {
      params: { energy_consumption: energyConsumption, timestamp }
    });
  },

  // Get emission forecast
  getEmissionForecast: (days = 7) => {
    return api.get(`/carbon/forecast?days=${days}`);
  },

  // Get carbon intensity factor
  getIntensityFactor: (region = 'default') => {
    return api.get(`/carbon/intensity-factor?region=${region}`);
  },

  // Get reduction recommendations
  getRecommendations: (currentConsumption) => {
    return api.get(`/carbon/recommendations?current_consumption=${currentConsumption}`);
  },

  // Get carbon metrics (for dashboard)
  getCarbonMetrics: () => {
    return api.get('/carbon/estimate', {
      params: { energy_consumption: 1250, timestamp: new Date().toISOString() }
    });
  }
};