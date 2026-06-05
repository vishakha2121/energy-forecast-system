import React from 'react';
import { HiTrendingDown, HiLightBulb, HiCheckCircle, HiChartBar } from 'react-icons/hi';

const OptimizationResults = ({ results }) => {
  if (!results) {
    return (
      <div className="card">
        <div className="text-center py-12 text-gray-500 dark:text-gray-400">
          Run optimization to see results
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Optimization Results</h3>
      
      {/* Key Metrics */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        <div className="text-center p-4 bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/20 dark:to-green-900/10 rounded-lg">
          <HiTrendingDown className="text-green-500 text-2xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">Peak Reduction</p>
          <p className="text-2xl font-bold text-green-600">
            {results.reduction_percentage?.toFixed(1) || 0}%
          </p>
        </div>
        <div className="text-center p-4 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-900/10 rounded-lg">
          <HiChartBar className="text-blue-500 text-2xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">Energy Saved</p>
          <p className="text-2xl font-bold text-blue-600">
            {results.peak_reduction?.toFixed(1) || 0} MW
          </p>
        </div>
      </div>

      {/* Strategy */}
      <div className="mb-4 p-4 bg-gray-50 dark:bg-gray-700/50 rounded-lg">
        <h4 className="font-semibold text-gray-800 dark:text-white mb-2">Optimization Strategy</h4>
        <p className="text-gray-600 dark:text-gray-300">{results.strategy || 'Load smoothing strategy applied'}</p>
      </div>

      {/* Recommendations */}
      <div>
        <h4 className="font-semibold text-gray-800 dark:text-white mb-3 flex items-center gap-2">
          <HiLightBulb /> Recommendations
        </h4>
        <ul className="space-y-2">
          {(results.recommendations || []).map((rec, idx) => (
            <li key={idx} className="flex items-start gap-2 text-sm text-gray-600 dark:text-gray-300">
              <HiCheckCircle className="text-green-500 mt-0.5 flex-shrink-0" />
              <span>{rec}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default OptimizationResults;