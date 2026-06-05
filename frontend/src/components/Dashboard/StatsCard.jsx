import React from 'react';
import { motion } from 'framer-motion';

const StatsCard = ({ title, value, unit, icon: Icon, color, change }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="stat-card"
    >
      <div className="flex justify-between items-start">
        <div>
          <p className="text-gray-500 dark:text-gray-400 text-sm mb-1">{title}</p>
          <h3 className="text-2xl font-bold text-gray-800 dark:text-white">
            {value} <span className="text-sm font-normal">{unit}</span>
          </h3>
          {change && (
            <p className={`text-xs mt-2 ${change > 0 ? 'text-red-500' : 'text-green-500'}`}>
              {change > 0 ? '↑' : '↓'} {Math.abs(change)}% from last hour
            </p>
          )}
        </div>
        <div className={`p-3 rounded-full bg-${color}-100 dark:bg-${color}-900/30`}>
          <Icon className={`text-${color}-600 dark:text-${color}-400 text-2xl`} />
        </div>
      </div>
    </motion.div>
  );
};

export default StatsCard;