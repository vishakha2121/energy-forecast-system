import { useState, useCallback } from 'react';
import { forecastAPI } from '../services/forecastAPI';

export const useForecast = () => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const getForecast = useCallback(async (startDate, endDate, modelType) => {
    setLoading(true);
    setError(null);
    try {
      const response = await forecastAPI.getForecast(startDate, endDate, modelType);
      setData(response.data);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const clearForecast = useCallback(() => {
    setData(null);
    setError(null);
  }, []);

  return { loading, data, error, getForecast, clearForecast };
};