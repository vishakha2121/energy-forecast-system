import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import CarbonMetrics from '../components/Carbon/CarbonMetrics';
import EmissionChart from '../components/Carbon/EmissionChart';
import Recommendations from '../components/Carbon/Recommendations';
import { carbonAPI } from '../services/carbonAPI';

const CarbonImpact = () => {
  const [loading, setLoading] = useState(true);
  const [emissions, setEmissions] = useState(null);
  const [forecast, setForecast] = useState([]);

  useEffect(() => {
    fetchCarbonData();
  }, []);

  const fetchCarbonData = async () => {
    try {
      const response = await carbonAPI.getCarbonMetrics();
      setEmissions(response.data);
      
      const forecastResponse = await carbonAPI.getEmissionForecast(7);
      setForecast(forecastResponse.data.daily_forecast);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching carbon data:', error);
      // Mock data
      setEmissions({
        co2_emissions_kg: 1250,
        equivalent_trees_needed_per_year: 57,
        equivalent_car_miles: 3125,
        carbon_intensity_kgCO2_per_kWh: 0.45
      });
      setLoading(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="space-y-6"
    >
      <div>
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Carbon Impact</h1>
        <p className="text-gray-600 dark:text-gray-400">
          Monitor and reduce your carbon footprint
        </p>
      </div>

      <CarbonMetrics emissions={emissions} />
      <EmissionChart data={forecast} />
      <Recommendations />
    </motion.div>
  );
};

export default CarbonImpact;