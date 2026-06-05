import numpy as np
from datetime import datetime, timedelta
import random

class CarbonCalculator:
    def __init__(self):
        # Carbon intensity factors (kg CO2 per kWh)
        self.carbon_intensity_factors = {
            "default": 0.45,  # Average global mix
            "renewable_high": 0.15,
            "coal_heavy": 0.85,
            "gas_heavy": 0.40,
            "nuclear_heavy": 0.05
        }
        
    def calculate_emissions(self, energy_consumption_kwh: float, timestamp: str = None):
        """Calculate CO2 emissions for given energy consumption"""
        
        # Get time-based intensity factor
        intensity = self.get_time_based_intensity(timestamp)
        
        # Calculate emissions
        co2_emissions = energy_consumption_kwh * intensity
        
        # Calculate equivalent trees needed to offset
        trees_needed = co2_emissions / 21.77  # 1 tree absorbs 21.77 kg CO2/year
        
        return {
            "energy_consumption_kwh": energy_consumption_kwh,
            "carbon_intensity_kgCO2_per_kWh": intensity,
            "co2_emissions_kg": co2_emissions,
            "co2_emissions_tons": co2_emissions / 1000,
            "equivalent_trees_needed_per_year": trees_needed,
            "equivalent_car_miles": co2_emissions * 2.5  # ~2.5 miles per kg CO2
        }
    
    def get_time_based_intensity(self, timestamp: str = None):
        """Get carbon intensity based on time of day"""
        
        if timestamp:
            dt = datetime.fromisoformat(timestamp)
            hour = dt.hour
        else:
            hour = datetime.now().hour
        
        # Simulate lower carbon intensity during daytime (solar)
        if 10 <= hour <= 15:  # Solar peak hours
            return 0.35
        elif 19 <= hour <= 22:  # Evening peak
            return 0.55
        elif 23 <= hour or hour <= 5:  # Night time
            return 0.40
        else:
            return 0.45
    
    async def forecast_emissions(self, days: int):
        """Forecast carbon emissions for next N days"""
        
        forecast = []
        current_date = datetime.now()
        
        for i in range(days):
            forecast_date = current_date + timedelta(days=i)
            
            # Simulate daily variation
            base_energy = np.random.normal(1000, 100)  # kWh
            weekday_factor = 1.2 if forecast_date.weekday() < 5 else 0.9
            
            daily_energy = base_energy * weekday_factor
            emissions = self.calculate_emissions(daily_energy, forecast_date.isoformat())
            
            forecast.append({
                "date": forecast_date.date().isoformat(),
                "forecasted_energy_kwh": daily_energy,
                "forecasted_emissions_kg": emissions['co2_emissions_kg'],
                "carbon_intensity": emissions['carbon_intensity_kgCO2_per_kWh']
            })
        
        total_emissions = sum(f['forecasted_emissions_kg'] for f in forecast)
        
        return {
            "daily_forecast": forecast,
            "total_forecasted_emissions_kg": total_emissions,
            "total_forecasted_emissions_tons": total_emissions / 1000,
            "average_intensity": np.mean([f['carbon_intensity'] for f in forecast])
        }
    
    def get_intensity_factor(self, region: str = "default"):
        """Get carbon intensity factor for specific region"""
        return self.carbon_intensity_factors.get(region, 0.45)
    
    def get_recommendations(self, current_consumption: float):
        """Get carbon reduction recommendations"""
        
        recommendations = []
        
        if current_consumption > 500:
            recommendations.append({
                "priority": "HIGH",
                "action": "Shift heavy loads to off-peak hours",
                "potential_savings_kgCO2": current_consumption * 0.15 * 0.45
            })
            recommendations.append({
                "priority": "HIGH",
                "action": "Implement energy efficiency measures",
                "potential_savings_kgCO2": current_consumption * 0.20 * 0.45
            })
        
        recommendations.append({
            "priority": "MEDIUM",
            "action": "Install solar panels or renewable sources",
            "potential_savings_kgCO2": current_consumption * 0.30 * 0.45
        })
        
        recommendations.append({
            "priority": "LOW",
            "action": "Optimize HVAC scheduling and setpoints",
            "potential_savings_kgCO2": current_consumption * 0.10 * 0.45
        })
        
        return recommendations