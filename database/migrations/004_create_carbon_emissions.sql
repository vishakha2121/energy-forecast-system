-- Create carbon_emissions table
CREATE TABLE IF NOT EXISTS carbon_emissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    energy_consumption FLOAT NOT NULL,
    carbon_intensity FLOAT,
    co2_emissions FLOAT,
    emission_factor VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create carbon_recommendations table
CREATE TABLE IF NOT EXISTS carbon_recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recommendation_text TEXT NOT NULL,
    priority VARCHAR(20),
    potential_savings FLOAT,
    implemented BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    implemented_at DATETIME
);

-- Create carbon_offsets table for tracking offset projects
CREATE TABLE IF NOT EXISTS carbon_offsets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name VARCHAR(200),
    offset_amount FLOAT,
    cost FLOAT,
    status VARCHAR(50),
    purchase_date DATE,
    certificate_url VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_carbon_emissions_timestamp ON carbon_emissions(timestamp);
CREATE INDEX idx_carbon_recommendations_priority ON carbon_recommendations(priority);