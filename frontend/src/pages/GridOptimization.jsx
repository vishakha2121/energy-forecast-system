import React, { useState } from 'react';
import { motion } from 'framer-motion';
import toast from 'react-hot-toast';
import GridControls from '../components/GridOptimization/GridControls';
import OptimizationResults from '../components/GridOptimization/OptimizationResults';
import LoadBalancingChart from '../components/GridOptimization/LoadBalancingChart';
import { gridAPI } from '../services/gridAPI';

const GridOptimization = () => {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [beforeLoad, setBeforeLoad] = useState([]);
  const [afterLoad, setAfterLoad] = useState([]);

  const handleOptimize = async ({ goal, scenario }) => {
    setLoading(true);
    try {
      const response = await gridAPI.optimizeGrid({ goal, scenario });
      const data = response.data;
      
      setResults(data);
      
      // Generate mock load data
      const before = Array.from({ length: 24 }, () => 600 + Math.random() * 300);
      const after = before.map(load => load * (1 - data.reduction_percentage / 100));
      setBeforeLoad(before);
      setAfterLoad(after);
      
      toast.success(`Optimization complete! ${data.reduction_percentage?.toFixed(1)}% peak reduction`);
    } catch (error) {
      console.error('Optimization error:', error);
      toast.error('Optimization failed');
      
      // Mock data
      const mockResults = {
        strategy: "peak_load_smoothing",
        reduction_percentage: 15.3,
        peak_reduction: 125,
        recommendations: [
          "Shift non-critical loads to off-peak hours",
          "Implement demand response programs",
          "Use energy storage during peak hours"
        ]
      };
      setResults(mockResults);
      
      const before = [850, 820, 780, 750, 800, 880, 920, 950, 980, 960, 940, 900, 880, 860, 840, 820, 800, 780, 760, 740, 720, 700, 680, 660];
      const after = before.map(l => l * 0.85);
      setBeforeLoad(before);
      setAfterLoad(after);
    } finally {
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
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Grid Optimization</h1>
        <p className="text-gray-600 dark:text-gray-400">
          Optimize power grid performance and reduce peak loads
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div>
          <GridControls onOptimize={handleOptimize} isLoading={loading} />
        </div>
        
        <div className="lg:col-span-2 space-y-6">
          <OptimizationResults results={results} />
          {beforeLoad.length > 0 && afterLoad.length > 0 && (
            <LoadBalancingChart before={beforeLoad} after={afterLoad} />
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default GridOptimization;