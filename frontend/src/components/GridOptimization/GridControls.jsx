import React, { useState } from 'react';
import { HiPlay, HiRefresh, HiChartPie } from 'react-icons/hi';

const GridControls = ({ onOptimize, isLoading }) => {
  const [goal, setGoal] = useState('minimize_peak');
  const [scenario, setScenario] = useState('peak_load_reduction');

  const optimizationGoals = [
    { value: 'minimize_peak', label: 'Minimize Peak Load', description: 'Reduce maximum demand' },
    { value: 'balance_load', label: 'Balance Load', description: 'Smooth load distribution' },
    { value: 'optimize_efficiency', label: 'Optimize Efficiency', description: 'Maximize grid efficiency' },
  ];

  const scenarios = [
    { value: 'peak_load_reduction', label: 'Peak Load Reduction' },
    { value: 'renewable_integration', label: 'Renewable Integration' },
    { value: 'emergency_response', label: 'Emergency Response' },
  ];

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4 flex items-center gap-2">
        <HiChartPie /> Optimization Controls
      </h3>
      
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Optimization Goal
          </label>
          <div className="grid grid-cols-1 gap-2">
            {optimizationGoals.map((opt) => (
              <label key={opt.value} className="flex items-center p-3 border rounded-lg cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700">
                <input
                  type="radio"
                  name="goal"
                  value={opt.value}
                  checked={goal === opt.value}
                  onChange={(e) => setGoal(e.target.value)}
                  className="mr-3"
                />
                <div>
                  <div className="font-medium text-gray-800 dark:text-white">{opt.label}</div>
                  <div className="text-sm text-gray-500 dark:text-gray-400">{opt.description}</div>
                </div>
              </label>
            ))}
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Simulation Scenario
          </label>
          <select
            value={scenario}
            onChange={(e) => setScenario(e.target.value)}
            className="input-field"
          >
            {scenarios.map((s) => (
              <option key={s.value} value={s.value}>{s.label}</option>
            ))}
          </select>
        </div>

        <div className="flex gap-3">
          <button
            onClick={() => onOptimize({ goal, scenario })}
            disabled={isLoading}
            className="btn-primary flex-1 flex items-center justify-center gap-2"
          >
            {isLoading ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
            ) : (
              <HiPlay />
            )}
            Run Optimization
          </button>
          <button className="btn-secondary">
            <HiRefresh />
          </button>
        </div>
      </div>
    </div>
  );
};

export default GridControls;