-- Create energy_data table for storing historical energy consumption
CREATE TABLE IF NOT EXISTS energy_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    energy_consumption FLOAT NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    day_of_week INTEGER,
    is_holiday INTEGER DEFAULT 0,
    peak_load FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX idx_energy_data_timestamp ON energy_data(timestamp);
CREATE INDEX idx_energy_data_day_of_week ON energy_data(day_of_week);
CREATE INDEX idx_energy_data_is_holiday ON energy_data(is_holiday);

-- Create trigger to update updated_at
CREATE TRIGGER update_energy_data_updated_at 
AFTER UPDATE ON energy_data
BEGIN
    UPDATE energy_data SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;