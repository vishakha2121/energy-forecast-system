import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { HiMenu, HiX, HiBell, HiUserCircle } from 'react-icons/hi';
import ThemeToggle from '../Common/ThemeToggle';
import { NAV_ITEMS } from '../../routes';

const Navbar = ({ sidebarOpen, setSidebarOpen }) => {
  const location = useLocation();
  const [notifications, setNotifications] = useState(3);

  return (
    <nav className="bg-white dark:bg-gray-800 shadow-lg fixed top-0 right-0 left-0 z-50 lg:left-64 transition-all duration-300">
      <div className="px-4 py-3 flex justify-between items-center">
        {/* Left side */}
        <div className="flex items-center gap-4">
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="lg:hidden text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
          >
            {sidebarOpen ? <HiX size={24} /> : <HiMenu size={24} />}
          </button>
          <h1 className="text-xl font-bold bg-gradient-to-r from-blue-600 to-blue-400 bg-clip-text text-transparent">
            Energy Forecast System
          </h1>
        </div>

        {/* Right side */}
        <div className="flex items-center gap-4">
          <ThemeToggle />
          
          {/* Notifications */}
          <button className="relative text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
            <HiBell size={22} />
            {notifications > 0 && (
              <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                {notifications}
              </span>
            )}
          </button>

          {/* User Profile */}
          <button className="flex items-center gap-2 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white">
            <HiUserCircle size={28} />
            <span className="hidden md:inline">Admin User</span>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;