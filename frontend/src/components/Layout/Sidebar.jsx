import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  HiHome, HiChartBar, HiLightningBolt, HiGlobe, 
  HiDocumentText, HiCog, HiChip 
} from 'react-icons/hi';

const navItems = [
  { path: '/', label: 'Dashboard', icon: HiHome },
  { path: '/forecasting', label: 'Forecasting', icon: HiChartBar },
  { path: '/grid-optimization', label: 'Grid Optimization', icon: HiLightningBolt },
  { path: '/carbon-impact', label: 'Carbon Impact', icon: HiGlobe },
  { path: '/reports', label: 'Reports', icon: HiDocumentText },
  { path: '/settings', label: 'Settings', icon: HiCog },
];

const Sidebar = ({ isOpen }) => {
  return (
    <aside className={`
      fixed top-0 left-0 z-40 h-screen transition-all duration-300
      bg-gradient-to-b from-gray-900 to-gray-800 text-white
      ${isOpen ? 'w-64' : 'w-20'} lg:w-64
      transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} lg:translate-x-0
    `}>
      {/* Logo */}
      <div className="flex items-center justify-center h-16 border-b border-gray-700">
        <HiChip className="text-3xl text-blue-400" />
        {isOpen && (
          <span className="ml-2 text-lg font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent">
            EnergyAI
          </span>
        )}
      </div>

      {/* Navigation */}
      <nav className="mt-8">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => `
              flex items-center px-4 py-3 mx-2 mb-2 rounded-lg transition-all duration-200
              ${isActive 
                ? 'bg-blue-600 text-white shadow-lg' 
                : 'text-gray-300 hover:bg-gray-700 hover:text-white'
              }
            `}
          >
            <item.icon className="text-xl" />
            {isOpen && <span className="ml-3">{item.label}</span>}
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-700">
        <div className="text-xs text-gray-400 text-center">
          {isOpen ? 'v1.0.0 | Smart Grid AI' : 'v1.0'}
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;