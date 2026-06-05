export const chartColors = {
  primary: '#3B82F6',
  secondary: '#10B981',
  danger: '#EF4444',
  warning: '#F59E0B',
  purple: '#8B5CF6',
  pink: '#EC4899',
  indigo: '#6366F1',
};

export const chartGradients = {
  energy: {
    start: '#3B82F6',
    end: '#93C5FD',
  },
  carbon: {
    start: '#10B981',
    end: '#6EE7B7',
  },
  peak: {
    start: '#EF4444',
    end: '#FCA5A5',
  },
};

export const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top',
      labels: {
        usePointStyle: true,
        boxWidth: 10,
      },
    },
    tooltip: {
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      titleColor: 'white',
      bodyColor: '#ddd',
      borderColor: '#3B82F6',
      borderWidth: 1,
    },
  },
  scales: {
    y: {
      grid: {
        color: 'rgba(0, 0, 0, 0.1)',
      },
    },
    x: {
      grid: {
        display: false,
      },
    },
  },
};