export const formatNumber = (num, decimals = 2) => {
  if (num === null || num === undefined) return 'N/A';
  return num.toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
};

export const formatCurrency = (num) => {
  return `$${formatNumber(num, 2)}`;
};

export const formatEnergy = (kwh) => {
  if (kwh >= 1000000) {
    return `${formatNumber(kwh / 1000000, 2)} GWh`;
  }
  if (kwh >= 1000) {
    return `${formatNumber(kwh / 1000, 2)} MWh`;
  }
  return `${formatNumber(kwh, 2)} kWh`;
};

export const formatDate = (date, format = 'short') => {
  const d = new Date(date);
  if (format === 'short') {
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }
  if (format === 'long') {
    return d.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    });
  }
  if (format === 'time') {
    return d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
  }
  return d.toISOString();
};

export const formatPercentage = (value) => {
  return `${formatNumber(value, 1)}%`;
};