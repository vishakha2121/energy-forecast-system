import React from 'react';
import { HiChip, HiChartBar, HiTrendingUp, HiCollection } from 'react-icons/hi';

const models = [
  { id: 'lstm', name: 'LSTM', icon: HiChip, description: 'Deep Learning based forecast', color: 'blue' },
  { id: 'xgboost', name: 'XGBoost', icon: HiChartBar, description: 'Gradient boosting forecast', color: 'green' },
  { id: 'arima', name: 'ARIMA', icon: HiTrendingUp, description: 'Statistical time series', color: 'purple' },
  { id: 'ensemble', name: 'Ensemble', icon: HiCollection, description: 'Combined model (Best)', color: 'orange' },
];

const ModelSelector = ({ selectedModel, onModelChange }) => {
  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Select Model</h3>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {models.map((model) => {
          const Icon = model.icon;
          const isSelected = selectedModel === model.id;
          
          return (
            <button
              key={model.id}
              onClick={() => onModelChange(model.id)}
              className={`
                p-4 rounded-lg border-2 transition-all duration-300 text-left
                ${isSelected 
                  ? `border-${model.color}-500 bg-${model.color}-50 dark:bg-${model.color}-900/20` 
                  : 'border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
                }
              `}
            >
              <div className="flex items-start gap-3">
                <Icon className={`text-xl text-${model.color}-500 mt-1`} />
                <div>
                  <h4 className={`font-semibold ${isSelected ? `text-${model.color}-600` : 'text-gray-700 dark:text-gray-300'}`}>
                    {model.name}
                  </h4>
                  <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">{model.description}</p>
                </div>
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
};

export default ModelSelector;