export const validateDateRange = (startDate, endDate) => {
  const start = new Date(startDate);
  const end = new Date(endDate);
  
  if (isNaN(start.getTime())) {
    return { valid: false, error: 'Invalid start date' };
  }
  if (isNaN(end.getTime())) {
    return { valid: false, error: 'Invalid end date' };
  }
  if (start > end) {
    return { valid: false, error: 'Start date must be before end date' };
  }
  const daysDiff = (end - start) / (1000 * 60 * 60 * 24);
  if (daysDiff > 30) {
    return { valid: false, error: 'Date range cannot exceed 30 days' };
  }
  return { valid: true };
};

export const validateEnergyValue = (value) => {
  if (typeof value !== 'number' || isNaN(value)) {
    return { valid: false, error: 'Value must be a number' };
  }
  if (value < 0) {
    return { valid: false, error: 'Value cannot be negative' };
  }
  if (value > 10000) {
    return { valid: false, error: 'Value exceeds maximum limit' };
  }
  return { valid: true };
};

export const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return { valid: re.test(email), error: 'Invalid email format' };
};