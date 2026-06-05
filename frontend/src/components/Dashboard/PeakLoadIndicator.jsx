import React from 'react';
import { HiLightningBolt } from 'react-icons/hi';

const PeakLoadIndicator = ({ currentLoad, peakThreshold, maxCapacity }) => {
  const percentage = (currentLoad / maxCapacity) * 100;
  const isPeak = currentLoad > peakThreshold;
  
  const getColor = () => {
    if (percentage > 85) return 'red';
    if (percentage > 70) return 'yellow';
    return 'green';
  };

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800 dark:text-white">Peak Load Indicator</h3>
        {isPeak && (
          <span className="px-3 py-1 bg-red-100 dark:bg-red-900/30 text-red-600 dark:text-red-400 rounded-full text-sm flex items-center gap-1">
            <HiLightningBolt /> PEAK ALERT
          </span>
        )}
      </div>
      
      <div className="relative pt-1">
        <div className="flex mb-2 items-center justify-between">
          <div>
            <span className="text-xs font-semibold inline-block text-gray-600 dark:text-gray-300">
              Current Load
            </span>
          </div>
          <div className="text-right">
            <span className="text-xs font-semibold inline-block text-gray-600 dark:text-gray-300">
              {currentLoad.toFixed(1)} MW / {maxCapacity} MW
            </span>
          </div>
        </div>
        <div className="overflow-hidden h-4 text-xs flex rounded bg-gray-200 dark:bg-gray-700">
          <div
            style={{ width: `${percentage}%` }}
            className={`shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-${getColor()}-500`}
          />
        </div>
      </div>
      
      <div className="mt-4 grid grid-cols-2 gap-4">
        <div className="text-center">
          <p className="text-gray-500 dark:text-gray-400 text-sm">Threshold</p>
          <p className="text-lg font-semibold text-gray-800 dark:text-white">{peakThreshold} MW</p>
        </div>
        <div className="text-center">
          <p className="text-gray-500 dark:text-gray-400 text-sm">Available Capacity</p>
          <p className="text-lg font-semibold text-green-600">{(maxCapacity - currentLoad).toFixed(1)} MW</p>
        </div>
      </div>
    </div>
  );
};

export default PeakLoadIndicator;