#!/usr/bin/env python3
"""
Generate sample energy consumption data for testing
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_energy_data(start_date='2023-01-01', end_date='2024-01-01'):
    """Generate synthetic energy consumption data"""
    
    dates = pd.date_range(start=start_date, end=end_date, freq='H')
    
    # Create patterns
    hours = dates.hour
    day_of_week = dates.dayofweek
    month = dates.month
    
    # Daily pattern
    daily_pattern = 300 + 200 * np.sin(np.pi * (hours - 6) / 12)
    daily_pattern = np.clip(daily_pattern, 350, 800)
    
    # Weekly pattern (higher on weekdays)
    weekly_pattern = 50 * (1 - day_of_week / 7)
    
    # Seasonal pattern
    seasonal_pattern = 80 * np.sin(2 * np.pi * (month - 6) / 12)
    
    # Temperature effect
    temp_base = 20 + 10 * np.sin(2 * np.pi * (month - 6) / 12)
    temp_variation = np.random.normal(0, 3, len(dates))
    temperature = temp_base + temp_variation + 5 * np.sin(2 * np.pi * hours / 24)
    
    # Humidity
    humidity = 70 - 0.5 * (temperature - 20) + np.random.normal(0, 5, len(dates))
    humidity = np.clip(humidity, 30, 95)
    
    # Add noise
    noise = np.random.normal(0, 25, len(dates))
    
    # Calculate consumption
    energy_consumption = daily_pattern + weekly_pattern + seasonal_pattern + noise
    energy_consumption = np.maximum(energy_consumption, 200)
    
    # Calculate peak load (similar to consumption but slightly higher)
    peak_load = energy_consumption * np.random.uniform(0.95, 1.05, len(dates))
    
    # Create DataFrame
    df = pd.DataFrame({
        'timestamp': dates,
        'energy_consumption': energy_consumption,
        'temperature': temperature,
        'humidity': humidity,
        'day_of_week': day_of_week,
        'is_holiday': [1 if d.weekday() >= 5 else 0 for d in dates],
        'peak_load': peak_load
    })
    
    return df

def save_to_csv(df, filepath):
    """Save data to CSV file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

def save_to_sqlite(df, db_path):
    """Save data to SQLite database"""
    conn = sqlite3.connect(db_path)
    df.to_sql('energy_data', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data saved to SQLite database: {db_path}")

def main():
    print("Generating sample energy data...")
    
    # Generate data
    df = generate_energy_data()
    print(f"Generated {len(df)} rows of data")
    print(df.head())
    print("\nData Statistics:")
    print(df['energy_consumption'].describe())
    
    # Save to CSV
    csv_path = 'backend/data/raw/energy_data.csv'
    save_to_csv(df, csv_path)
    
    # Save to SQLite (optional)
    # db_path = 'database/energy_db.sqlite'
    # save_to_sqlite(df, db_path)
    
    print("\n✅ Sample data generation complete!")

if __name__ == "__main__":
    main()