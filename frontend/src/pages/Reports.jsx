import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { HiDownload, HiPrinter, HiCalendar } from 'react-icons/hi';
import toast from 'react-hot-toast';

const Reports = () => {
  const [dateRange, setDateRange] = useState('weekly');

  const reports = [
    { name: 'Energy Consumption Report', type: 'PDF', size: '2.4 MB', date: '2024-01-15' },
    { name: 'Peak Load Analysis', type: 'PDF', size: '1.8 MB', date: '2024-01-14' },
    { name: 'Carbon Emissions Summary', type: 'PDF', size: '3.1 MB', date: '2024-01-13' },
    { name: 'Grid Optimization Results', type: 'PDF', size: '2.2 MB', date: '2024-01-12' },
    { name: 'Monthly Forecast Report', type: 'PDF', size: '4.5 MB', date: '2024-01-01' },
  ];

  const handleDownload = (report) => {
    toast.success(`Downloading ${report.name}`);
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="space-y-6"
    >
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Reports</h1>
          <p className="text-gray-600 dark:text-gray-400">Download and manage system reports</p>
        </div>
        <div className="flex gap-3">
          <select className="input-field w-40" value={dateRange} onChange={(e) => setDateRange(e.target.value)}>
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
            <option value="yearly">Yearly</option>
          </select>
          <button className="btn-primary flex items-center gap-2">
            <HiCalendar /> Generate
          </button>
        </div>
      </div>

      <div className="card">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-200 dark:border-gray-700">
                <th className="text-left py-3 px-4">Report Name</th>
                <th className="text-left py-3 px-4">Type</th>
                <th className="text-left py-3 px-4">Size</th>
                <th className="text-left py-3 px-4">Date</th>
                <th className="text-left py-3 px-4">Actions</th>
              </tr>
            </thead>
            <tbody>
              {reports.map((report, idx) => (
                <tr key={idx} className="border-b border-gray-100 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800/50">
                  <td className="py-3 px-4 font-medium">{report.name}</td>
                  <td className="py-3 px-4">
                    <span className="px-2 py-1 bg-blue-100 text-blue-600 rounded text-xs">{report.type}</span>
                  </td>
                  <td className="py-3 px-4">{report.size}</td>
                  <td className="py-3 px-4">{report.date}</td>
                  <td className="py-3 px-4">
                    <div className="flex gap-2">
                      <button onClick={() => handleDownload(report)} className="text-blue-500 hover:text-blue-600">
                        <HiDownload />
                      </button>
                      <button className="text-gray-500 hover:text-gray-600">
                        <HiPrinter />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </motion.div>
  );
};

export default Reports;