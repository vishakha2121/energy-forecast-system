-- Insert sample energy data for testing
INSERT INTO energy_data (timestamp, energy_consumption, temperature, humidity, day_of_week, is_holiday, peak_load)
VALUES 
    (datetime('now', '-7 days'), 452.3, 15.2, 65.4, 0, 0, 452.3),
    (datetime('now', '-6 days'), 428.7, 14.8, 67.2, 1, 0, 428.7),
    (datetime('now', '-5 days'), 589.7, 13.8, 70.8, 2, 0, 589.7),
    (datetime('now', '-4 days'), 678.2, 14.5, 68.5, 3, 0, 678.2),
    (datetime('now', '-3 days'), 723.4, 15.2, 65.2, 4, 0, 723.4),
    (datetime('now', '-2 days'), 845.6, 19.8, 52.1, 5, 1, 845.6),
    (datetime('now', '-1 days'), 798.4, 18.9, 56.2, 6, 1, 798.4);

-- Insert sample forecast accuracy data
INSERT INTO forecast_accuracy (model_name, mae, rmse, mape, r2_score, evaluation_date)
VALUES 
    ('lstm', 12.5, 18.3, 8.2, 0.89, date('now')),
    ('xgboost', 10.2, 15.7, 6.8, 0.92, date('now')),
    ('arima', 14.8, 21.2, 9.5, 0.85, date('now')),
    ('ensemble', 9.5, 14.2, 6.1, 0.94, date('now'));

-- Insert sample grid optimization data
INSERT INTO grid_optimizations (optimization_type, optimization_strategy, energy_saved, peak_reduction, efficiency_gain)
VALUES 
    ('peak_load_reduction', 'load_smoothing', 125.5, 85.3, 12.5),
    ('load_balancing', 'demand_response', 98.2, 62.1, 8.3);

-- Insert sample carbon recommendations
INSERT INTO carbon_recommendations (recommendation_text, priority, potential_savings)
VALUES 
    ('Shift heavy loads to off-peak hours', 'HIGH', 187.5),
    ('Implement energy efficiency measures', 'HIGH', 250.0),
    ('Install solar panels or renewable sources', 'MEDIUM', 375.0),
    ('Optimize HVAC scheduling', 'LOW', 93.75);