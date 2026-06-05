import React from 'react';
import { HiCloud, HiTree, HiCar, HiFactory } from 'react-icons/hi';

const CarbonMetrics = ({ emissions }) => {
  const metrics = emissions || {
    co2_emissions_kg: 1250,
    equivalent_trees_needed_per_year: 57,
    equivalent_car_miles: 3125,
    carbon_intensity_kgCO2_per_kWh: 0.45
  };

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4 flex items-center gap-2">
        <HiCloud className="text-green-500" /> Carbon Impact Metrics
      </h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-4 bg-red-50 dark:bg-red-900/20 rounded-lg text-center">
          <HiFactory className="text-red-500 text-3xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">CO2 Emissions</p>
          <p className="text-2xl font-bold text-red-600">{metrics.co2_emissions_kg} kg</p>
          <p className="text-xs text-gray-500">({(metrics.co2_emissions_kg / 1000).toFixed(2)} tons)</p>
        </div>
        
        <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg text-center">
          <HiTree className="text-green-500 text-3xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">Trees Needed to Offset</p>
          <p className="text-2xl font-bold text-green-600">{metrics.equivalent_trees_needed_per_year}</p>
          <p className="text-xs text-gray-500">per year</p>
        </div>
        
        <div className="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg text-center">
          <HiCar className="text-blue-500 text-3xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">Equivalent Car Miles</p>
          <p className="text-2xl font-bold text-blue-600">{metrics.equivalent_car_miles.toLocaleString()}</p>
          <p className="text-xs text-gray-500">miles driven</p>
        </div>
        
        <div className="p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg text-center">
          <HiCloud className="text-purple-500 text-3xl mx-auto mb-2" />
          <p className="text-sm text-gray-600 dark:text-gray-400">Carbon Intensity</p>
          <p className="text-2xl font-bold text-purple-600">{metrics.carbon_intensity_kgCO2_per_kWh}</p>
          <p className="text-xs text-gray-500">kg CO2 per kWh</p>
        </div>
      </div>
    </div>
  );
};

export default CarbonMetrics;