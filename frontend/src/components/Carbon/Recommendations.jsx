import React from 'react';
import { HiLightBulb, HiTrendingUp, HiRefresh } from 'react-icons/hi';

const Recommendations = ({ recommendations }) => {
  const recs = recommendations || [
    { priority: 'HIGH', action: 'Shift heavy loads to off-peak hours', savings: 187.5 },
    { priority: 'HIGH', action: 'Implement energy efficiency measures', savings: 250.0 },
    { priority: 'MEDIUM', action: 'Install solar panels or renewable sources', savings: 375.0 },
    { priority: 'LOW', action: 'Optimize HVAC scheduling and setpoints', savings: 93.75 },
  ];

  const getPriorityColor = (priority) => {
    switch(priority) {
      case 'HIGH': return 'text-red-600 bg-red-100 dark:bg-red-900/30';
      case 'MEDIUM': return 'text-yellow-600 bg-yellow-100 dark:bg-yellow-900/30';
      case 'LOW': return 'text-green-600 bg-green-100 dark:bg-green-900/30';
      default: return 'text-gray-600 bg-gray-100 dark:bg-gray-700';
    }
  };

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4 flex items-center gap-2">
        <HiLightBulb className="text-yellow-500" /> Carbon Reduction Recommendations
      </h3>
      
      <div className="space-y-3">
        {recs.map((rec, idx) => (
          <div key={idx} className="p-4 border border-gray-200 dark:border-gray-700 rounded-lg hover:shadow-md transition-shadow">
            <div className="flex items-start justify-between mb-2">
              <div className="flex items-center gap-2">
                <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getPriorityColor(rec.priority)}`}>
                  {rec.priority}
                </span>
                <span className="font-medium text-gray-800 dark:text-white">{rec.action}</span>
              </div>
              <div className="text-right">
                <p className="text-sm text-green-600 dark:text-green-400 font-semibold">
                  Save {rec.savings} kg CO2
                </p>
              </div>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400">
              <HiTrendingUp />
              <span>Potential reduction: {((rec.savings / 1000) * 100).toFixed(1)}% of monthly emissions</span>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
        <div className="flex items-center gap-2">
          <HiRefresh className="text-blue-500" />
          <p className="text-sm text-blue-700 dark:text-blue-300">
            Implementing all recommendations could reduce carbon footprint by up to 65%
          </p>
        </div>
      </div>
    </div>
  );
};

export default Recommendations;