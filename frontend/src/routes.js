// Route configuration
export const ROUTES = {
  DASHBOARD: '/',
  FORECASTING: '/forecasting',
  GRID_OPTIMIZATION: '/grid-optimization',
  CARBON_IMPACT: '/carbon-impact',
  REPORTS: '/reports',
  SETTINGS: '/settings'
};

export const NAV_ITEMS = [
  { path: ROUTES.DASHBOARD, label: 'Dashboard', icon: 'HiHome' },
  { path: ROUTES.FORECASTING, label: 'Forecasting', icon: 'HiChartBar' },
  { path: ROUTES.GRID_OPTIMIZATION, label: 'Grid Optimization', icon: 'HiLightningBolt' },
  { path: ROUTES.CARBON_IMPACT, label: 'Carbon Impact', icon: 'HiGlobe' },
  { path: ROUTES.REPORTS, label: 'Reports', icon: 'HiDocumentText' },
  { path: ROUTES.SETTINGS, label: 'Settings', icon: 'HiCog' }
];