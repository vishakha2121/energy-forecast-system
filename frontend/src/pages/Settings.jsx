import React, { useState } from 'react';
import { motion } from 'framer-motion';
import toast from 'react-hot-toast';

const Settings = () => {
  const [settings, setSettings] = useState({
    notifications: true,
    autoRefresh: true,
    refreshInterval: 5,
    darkMode: false,
    defaultModel: 'ensemble',
    emailAlerts: true,
    alertThreshold: 850
  });

  const handleChange = (key, value) => {
    setSettings({ ...settings, [key]: value });
  };

  const handleSave = () => {
    localStorage.setItem('userSettings', JSON.stringify(settings));
    toast.success('Settings saved successfully!');
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="space-y-6"
    >
      <div>
        <h1 className="text-2xl font-bold text-gray-800 dark:text-white">Settings</h1>
        <p className="text-gray-600 dark:text-gray-400">Configure your application preferences</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* General Settings */}
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">General Settings</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <div>
                <p className="font-medium">Enable Notifications</p>
                <p className="text-sm text-gray-500">Receive alerts about peak loads</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={settings.notifications}
                  onChange={(e) => handleChange('notifications', e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>

            <div className="flex justify-between items-center">
              <div>
                <p className="font-medium">Auto Refresh Data</p>
                <p className="text-sm text-gray-500">Automatically update dashboard</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={settings.autoRefresh}
                  onChange={(e) => handleChange('autoRefresh', e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>

            <div>
              <label className="block font-medium mb-2">Refresh Interval (minutes)</label>
              <input
                type="number"
                value={settings.refreshInterval}
                onChange={(e) => handleChange('refreshInterval', parseInt(e.target.value))}
                className="input-field"
                min="1"
                max="60"
              />
            </div>

            <div>
              <label className="block font-medium mb-2">Default Forecasting Model</label>
              <select
                value={settings.defaultModel}
                onChange={(e) => handleChange('defaultModel', e.target.value)}
                className="input-field"
              >
                <option value="lstm">LSTM</option>
                <option value="xgboost">XGBoost</option>
                <option value="arima">ARIMA</option>
                <option value="ensemble">Ensemble (Recommended)</option>
              </select>
            </div>
          </div>
        </div>

        {/* Alert Settings */}
        <div className="card">
          <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">Alert Settings</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <div>
                <p className="font-medium">Email Alerts</p>
                <p className="text-sm text-gray-500">Receive alerts via email</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={settings.emailAlerts}
                  onChange={(e) => handleChange('emailAlerts', e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
              </label>
            </div>

            <div>
              <label className="block font-medium mb-2">Peak Load Alert Threshold (MW)</label>
              <input
                type="number"
                value={settings.alertThreshold}
                onChange={(e) => handleChange('alertThreshold', parseFloat(e.target.value))}
                className="input-field"
                min="500"
                max="1000"
              />
              <p className="text-xs text-gray-500 mt-1">Alert when load exceeds this value</p>
            </div>
          </div>
        </div>
      </div>

      <div className="flex justify-end gap-3">
        <button className="btn-secondary">Cancel</button>
        <button onClick={handleSave} className="btn-primary">Save Settings</button>
      </div>
    </motion.div>
  );
};

export default Settings;