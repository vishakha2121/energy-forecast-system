import React, { useState } from 'react';
import { HiCalendar, HiRefresh } from 'react-icons/hi';

const ForecastControls = ({ onForecast, isLoading }) => {
  const [startDate, setStartDate] = useState(new Date().toISOString().split('T')[0]);
  const [endDate, setEndDate] = useState(() => {
    const date = new Date();
    date.setDate(date.getDate() + 7);
    return date.toISOString().split('T')[0];
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onForecast({ startDate, endDate });
  };

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Forecast Controls</h3>
      <form onSubmit={handleSubmit}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Start Date
            </label>
            <div className="relative">
              <HiCalendar className="absolute left-3 top-3 text-gray-400" />
              <input
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="input-field pl-10"
                required
              />
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              End Date
            </label>
            <div className="relative">
              <HiCalendar className="absolute left-3 top-3 text-gray-400" />
              <input
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                className="input-field pl-10"
                required
              />
            </div>
          </div>
        </div>
        <button
          type="submit"
          disabled={isLoading}
          className="btn-primary w-full flex items-center justify-center gap-2"
        >
          {isLoading ? (
            <>
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
              Forecasting...
            </>
          ) : (
            <>
              <HiRefresh /> Generate Forecast
            </>
          )}
        </button>
      </form>
    </div>
  );
};

export default ForecastControls;