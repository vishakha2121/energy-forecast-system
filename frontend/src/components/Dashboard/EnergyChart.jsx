import React from 'react';
import {
  LineChart,
  Line,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ComposedChart,
  Bar
} from 'recharts';

const EnergyChart = ({ data, title, type = 'line' }) => {
  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700">
          <p className="text-sm font-semibold text-gray-600 dark:text-gray-300">{label}</p>
          {payload.map((p, idx) => (
            <p key={idx} className="text-sm" style={{ color: p.color }}>
              {p.name}: {p.value.toFixed(2)} kWh
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="card">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">{title}</h3>
      <ResponsiveContainer width="100%" height={400}>
        {type === 'line' ? (
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
            <XAxis dataKey="time" stroke="#9CA3AF" />
            <YAxis stroke="#9CA3AF" />
            <Tooltip content={<CustomTooltip />} />
            <Legend />
            <Line
              type="monotone"
              dataKey="actual"
              stroke="#3B82F6"
              strokeWidth={2}
              dot={false}
              name="Actual Load"
            />
            <Line
              type="monotone"
              dataKey="forecast"
              stroke="#10B981"
              strokeWidth={2}
              strokeDasharray="5 5"
              dot={false}
              name="Forecast"
            />
          </LineChart>
        ) : (
          <ComposedChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="peak" fill="#EF4444" name="Peak Load" />
            <Area type="monotone" dataKey="average" fill="#3B82F6" stroke="#2563EB" name="Average" />
          </ComposedChart>
        )}
      </ResponsiveContainer>
    </div>
  );
};

export default EnergyChart;