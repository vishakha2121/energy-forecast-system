import api from './api';

export const gridAPI = {
  // Optimize grid
  optimizeGrid: (data) => {
    return api.post('/grid/optimize', {
      current_load: data.currentLoad || Array(24).fill(600).map(() => 600 + Math.random() * 300),
      forecasted_load: Array(24).fill(600).map(() => 600 + Math.random() * 300),
      optimization_goal: data.goal || 'minimize_peak'
    });
  },

  // Run simulation
  runSimulation: (scenario) => {
    return api.get(`/grid/simulation?scenario=${scenario}`);
  },

  // Get load balancing strategy
  getLoadBalancing: (currentPeak, capacity) => {
    return api.get(`/grid/load-balancing?current_peak=${currentPeak}&capacity=${capacity}`);
  },

  // Run what-if analysis
  whatIfAnalysis: (changes) => {
    return api.post('/grid/what-if', changes);
  }
};