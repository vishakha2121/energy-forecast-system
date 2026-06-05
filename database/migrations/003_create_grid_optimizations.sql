-- Create grid_optimizations table
CREATE TABLE IF NOT EXISTS grid_optimizations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    optimization_type VARCHAR(50) NOT NULL,
    load_before JSON,
    load_after JSON,
    optimization_strategy VARCHAR(100),
    energy_saved FLOAT,
    peak_reduction FLOAT,
    efficiency_gain FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create optimization_logs table for tracking optimization events
CREATE TABLE IF NOT EXISTS optimization_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    optimization_id INTEGER,
    event_type VARCHAR(50),
    event_details TEXT,
    event_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (optimization_id) REFERENCES grid_optimizations(id)
);

CREATE INDEX idx_optimization_logs_optimization_id ON optimization_logs(optimization_id);

-- Create grid_config table for storing grid settings
CREATE TABLE IF NOT EXISTS grid_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    config_key VARCHAR(100) UNIQUE NOT NULL,
    config_value TEXT,
    description TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert default grid configuration
INSERT OR IGNORE INTO grid_config (config_key, config_value, description) VALUES
('grid_capacity', '1000', 'Maximum grid capacity in MW'),
('peak_threshold', '850', 'Peak load threshold in MW'),
('optimization_frequency', '15', 'Optimization frequency in minutes'),
('auto_optimize', 'true', 'Enable automatic optimization');