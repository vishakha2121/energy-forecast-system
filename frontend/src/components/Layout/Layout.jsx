import React, { useState } from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import Footer from './Footer';

const Layout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Navbar sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
      <Sidebar isOpen={sidebarOpen} />
      
      <main className={`
        transition-all duration-300 pt-16
        lg:pl-64
      `}>
        <div className="p-4 md:p-6 min-h-[calc(100vh-64px)]">
          {children}
        </div>
        <Footer />
      </main>
    </div>
  );
};

export default Layout;