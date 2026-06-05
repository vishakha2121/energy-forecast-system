-- Create forecasts table for storing prediction results
CREATE TABLE IF NOT EXISTS forecasts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    model_used VARCHAR(50) NOT NULL,
    predicted_value FLOAT NOT NULL,
    actual_value FLOAT,
    confidence_interval_lower FLOAT,
    confidence_interval_upper FLOAT,
    accuracy_score FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_forecasts_timestamp ON forecasts(timestamp);
CREATE INDEX idx_forecasts_model_used ON forecasts(model_used);

-- Create forecast_accuracy table for model performance tracking
CREATE TABLE IF NOT EXISTS forecast_accuracy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name VARCHAR(50) NOT NULL,
    mae FLOAT,
    rmse FLOAT,
    mape FLOAT,
    r2_score FLOAT,
    evaluation_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_forecast_accuracy_model ON forecast_accuracy(model_name);
CREATE INDEX idx_forecast_accuracy_date ON forecast_accuracy(evaluation_date);