import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { HiLightningBolt, HiChartBar, HiGlobe, HiChip } from 'react-icons/hi';
import StatsCard from '../components/Dashboard/StatsCard';
import EnergyChart from '../components/Dashboard/EnergyChart';
import PeakLoadIndicator from '../components/Dashboard/PeakLoadIndicator';
import { forecastAPI } from '../services/forecastAPI';

const Dashboard = () => {
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    currentLoad: 745,
    peakLoad: 892,
    avgConsumption: 654,
    carbonSaved: 1250
  });
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const response = await forecastAPI.getCurrentForecast();
      const data = response.data;
      setChartData(data.map(item => ({
        time: item.hour,
        actual: item.consumption,
        forecast: item.forecast
      })));
      setLoading(false);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
      // Mock data for demo
      setChartData([
        { time: '00:00', actual: 520, forecast: 530 },
        { time: '04:00', actual: 480, forecast: 490 },
        { time: '08:00', actual: 680, forecast: 700 },
        { time: '12:00', actual: 820, forecast: 810 },
        { time: '16:00', actual: 890, forecast: 880 },
        { time: '20:00', actual: 750, forecast: 740 },
        { time: '24:00', actual: 550, forecast: 560 },
      ]);
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
      {/* Page Header */}
      <div>
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Dashboard</h1>
        <p className="text-gray-600 dark:text-gray-400">Real-time energy monitoring and analytics</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatsCard
          title="Current Load"
          value={stats.currentLoad}
          unit="MW"
          icon={HiLightningBolt}
          color="blue"
          change={5.2}
        />
        <StatsCard
          title="Peak Load"
          value={stats.peakLoad}
          unit="MW"
          icon={HiChartBar}
          color="red"
          change={-2.1}
        />
        <StatsCard
          title="Avg Consumption"
          value={stats.avgConsumption}
          unit="MW"
          icon={HiChip}
          color="green"
          change={-1.5}
        />
        <StatsCard
          title="Carbon Saved"
          value={stats.carbonSaved}
          unit="kg"
          icon={HiGlobe}
          color="purple"
          change={-12.3}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <EnergyChart data={chartData} title="Energy Consumption (Last 24 Hours)" />
        </div>
        <div>
          <PeakLoadIndicator
            currentLoad={stats.currentLoad}
            peakThreshold={800}
            maxCapacity={1000}
          />
        </div>
      </div>

      {/* Additional Info */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">System Status</h3>
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <span>Grid Health</span>
              <span className="px-2 py-1 bg-green-100 text-green-600 rounded-full text-sm">Excellent</span>
            </div>
            <div className="flex justify-between items-center">
              <span>Forecast Accuracy</span>
              <span>93.9%</span>
            </div>
            <div className="flex justify-between items-center">
              <span>Active Models</span>
              <span>LSTM, XGBoost, ARIMA, Ensemble</span>
            </div>
          </div>
        </div>
        
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Quick Actions</h3>
          <div className="space-y-2">
            <button className="btn-primary w-full">Generate New Forecast</button>
            <button className="btn-secondary w-full">Run Grid Optimization</button>
            <button className="btn-secondary w-full">View Carbon Report</button>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default Dashboard;