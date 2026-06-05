import numpy as np
from typing import List, Dict, Any
from datetime import datetime
import random

class GridOptimizer:
    def __init__(self):
        self.grid_capacity = 1000  # MW
        self.peak_threshold = 850  # MW
        
    def optimize(self, current_load: List[float], forecasted_load: List[float], goal: str = "minimize_peak"):
        """Optimize grid load distribution"""
        
        if goal == "minimize_peak":
            result = self.minimize_peak_load(current_load, forecasted_load)
        elif goal == "balance_load":
            result = self.balance_load_distribution(current_load, forecasted_load)
        else:
            result = self.optimize_efficiency(current_load, forecasted_load)
        
        return result
    
    def minimize_peak_load(self, current: List[float], forecasted: List[float]):
        """Strategy to minimize peak load"""
        
        peak_hours = self.find_peak_hours(forecasted)
        smoothing_strategy = self.generate_smoothing_strategy(peak_hours)
        
        optimized_load = self.apply_strategy(forecasted, smoothing_strategy)
        peak_reduction = max(forecasted) - max(optimized_load)
        
        return {
            "strategy": "peak_load_smoothing",
            "original_peak": max(forecasted),
            "optimized_peak": max(optimized_load),
            "peak_reduction": peak_reduction,
            "reduction_percentage": (peak_reduction / max(forecasted)) * 100,
            "recommendations": self.get_peak_reduction_tips(),
            "optimized_load": optimized_load.tolist()
        }
    
    def balance_load_distribution(self, current: List[float], forecasted: List[float]):
        """Balance load across time periods"""
        
        average_load = np.mean(forecasted)
        balanced_load = [min(self.grid_capacity, max(0.5 * average_load, load)) for load in forecasted]
        
        return {
            "strategy": "load_balancing",
            "average_load": average_load,
            "max_deviation_before": max(forecasted) - min(forecasted),
            "max_deviation_after": max(balanced_load) - min(balanced_load),
            "balanced_load": balanced_load,
            "recommendations": [
                "Shift non-critical loads to off-peak hours",
                "Implement demand response programs",
                "Use energy storage during peak hours"
            ]
        }
    
    def optimize_efficiency(self, current: List[float], forecasted: List[float]):
        """Optimize for maximum efficiency"""
        
        efficiency_scores = self.calculate_efficiency(forecasted)
        optimization_points = np.where(efficiency_scores < 0.7)[0]
        
        return {
            "strategy": "efficiency_optimization",
            "efficiency_scores": efficiency_scores.tolist(),
            "optimization_needed": len(optimization_points),
            "recommendations": [
                "Upgrade transformers at identified points",
                "Add capacitor banks for power factor correction",
                "Implement voltage optimization"
            ]
        }
    
    def find_peak_hours(self, load: List[float]):
        """Find hours with peak load"""
        threshold = np.percentile(load, 85)
        peak_hours = [i for i, l in enumerate(load) if l > threshold]
        return peak_hours
    
    def generate_smoothing_strategy(self, peak_hours):
        """Generate load smoothing strategy"""
        strategy = {}
        for hour in peak_hours:
            strategy[hour] = {
                "action": "reduce",
                "amount": random.uniform(5, 15),
                "method": "load_shifting"
            }
        return strategy
    
    def apply_strategy(self, load: List[float], strategy):
        """Apply optimization strategy to load"""
        optimized = np.array(load)
        for hour, action in strategy.items():
            if hour < len(optimized):
                optimized[hour] *= (1 - action['amount'] / 100)
        return optimized
    
    def get_peak_reduction_tips(self):
        """Get tips for peak reduction"""
        return [
            "Implement Time-of-Use pricing",
            "Deploy battery storage systems",
            "Use demand response programs",
            "Shift industrial processes to off-peak hours",
            "Optimize HVAC scheduling"
        ]
    
    def calculate_efficiency(self, load: List[float]):
        """Calculate efficiency scores"""
        ideal_load = np.mean(load)
        efficiency = [min(1.0, ideal_load / max(0.1, l)) for l in load]
        return np.array(efficiency)
    
    def balance_load(self, current_peak: float, capacity: float):
        """Get load balancing strategy"""
        load_percentage = (current_peak / capacity) * 100
        
        if load_percentage > 90:
            strategy = "CRITICAL: Immediate load reduction needed"
            actions = ["Activate emergency reserves", "Initiate load shedding", "Request demand reduction"]
        elif load_percentage > 75:
            strategy = "WARNING: High load, consider load balancing"
            actions = ["Shift non-critical loads", "Enable demand response", "Use distributed generation"]
        else:
            strategy = "NORMAL: Load within safe limits"
            actions = ["Monitor continuously", "Prepare for peak periods", "Optimize for efficiency"]
        
        return {
            "current_load_percentage": load_percentage,
            "strategy": strategy,
            "recommended_actions": actions,
            "available_capacity": capacity - current_peak
        }
    
    async def run_simulation(self, scenario: str):
        """Run different simulation scenarios"""
        
        simulations = {
            "peak_load_reduction": self.simulate_peak_reduction(),
            "renewable_integration": self.simulate_renewable_integration(),
            "emergency_response": self.simulate_emergency_response()
        }
        
        return simulations.get(scenario, {"error": "Scenario not found"})
    
    def simulate_peak_reduction(self):
        """Simulate peak load reduction"""
        original_peak = np.random.normal(900, 50)
        reduced_peak = original_peak * np.random.uniform(0.7, 0.85)
        
        return {
            "scenario": "Peak Load Reduction",
            "original_peak_mw": original_peak,
            "reduced_peak_mw": reduced_peak,
            "reduction_percentage": ((original_peak - reduced_peak) / original_peak) * 100,
            "estimated_savings_mwh": (original_peak - reduced_peak) * 4,  # 4 hours peak duration
            "roi_months": random.randint(6, 18)
        }
    
    def simulate_renewable_integration(self):
        """Simulate renewable energy integration"""
        renewable_percentage = random.uniform(20, 45)
        carbon_reduction = renewable_percentage * 0.8
        
        return {
            "scenario": "Renewable Integration",
            "renewable_percentage": renewable_percentage,
            "carbon_reduction_percentage": carbon_reduction,
            "grid_stability_impact": random.choice(["Positive", "Neutral", "Requires Storage"]),
            "recommended_storage_capacity_mwh": renewable_percentage * 2
        }
    
    def simulate_emergency_response(self):
        """Simulate emergency response"""
        return {
            "scenario": "Emergency Response",
            "response_time_minutes": random.randint(5, 30),
            "load_reduction_achieved_mw": random.uniform(100, 300),
            "affected_customers": random.randint(1000, 10000),
            "restoration_time_hours": random.uniform(0.5, 4)
        }
    
    async def what_if_analysis(self, load_changes: Dict[str, float]):
        """Run what-if analysis for load changes"""
        
        analysis = {
            "input_changes": load_changes,
            "predicted_impacts": {},
            "recommendations": []
        }
        
        for change_type, percentage in load_changes.items():
            if change_type == "temperature_increase":
                impact = percentage * 2.5  # 1% temp increase = 2.5% load increase
                analysis["predicted_impacts"][change_type] = f"{impact:.1f}% load increase"
                analysis["recommendations"].append("Increase cooling efficiency, adjust setpoints")
            
            elif change_type == "economic_activity":
                impact = percentage * 1.2
                analysis["predicted_impacts"][change_type] = f"{impact:.1f}% load change"
                analysis["recommendations"].append("Monitor industrial load patterns")
            
            elif change_type == "renewable_output":
                impact = -percentage * 0.8
                analysis["predicted_impacts"][change_type] = f"{impact:.1f}% grid load change"
                analysis["recommendations"].append("Adjust dispatch of conventional generation")
        
        return analysis