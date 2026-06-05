import React from 'react';
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from 'recharts';

const EmissionChart = ({ data }) => {
  const chartData = data || [
    { date: 'Mon', emissions: 120, intensity: 0.45 },
    { date: 'Tue', emissions: 135, intensity: 0.48 },
    { date: 'Wed', emissions: 125, intensity: 0.44 },
    { date: 'Thu', emissions: 140, intensity: 0.47 },
    { date: 'Fri', emissions: 155, intensity: 0.49 },
    { date: 'Sat', emissions: 110, intensity: 0.42 },
    { date: 'Sun', emissions: 115, intensity: 0.43 },
  ];

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Emissions Forecast</h3>
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart data={chartData}>
          <defs>
            <linearGradient id="colorEmissions" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#10B981" stopOpacity={0.8}/>
              <stop offset="95%" stopColor="#10B981" stopOpacity={0}/>
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis yAxisId="left" />
          <YAxis yAxisId="right" orientation="right" />
          <Tooltip />
          <Area
            yAxisId="left"
            type="monotone"
            dataKey="emissions"
            stroke="#10B981"
            fill="url(#colorEmissions)"
            name="CO2 Emissions (kg)"
          />
          <Area
            yAxisId="right"
            type="monotone"
            dataKey="intensity"
            stroke="#3B82F6"
            fill="none"
            name="Carbon Intensity"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default EmissionChart;