import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  Cell
} from 'recharts';

const LoadBalancingChart = ({ before, after }) => {
  const data = before.map((load, idx) => ({
    hour: `Hour ${idx + 1}`,
    before: load,
    after: after[idx]
  }));

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Load Balancing Visualization</h3>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="hour" interval={3} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="before" fill="#EF4444" name="Before Optimization" />
          <Bar dataKey="after" fill="#10B981" name="After Optimization" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default LoadBalancingChart;