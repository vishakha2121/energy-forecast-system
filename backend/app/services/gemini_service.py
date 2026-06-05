import google.generativeai as genai
from app.config import settings
import json

class GeminiService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
            print("Warning: Gemini API key not configured")
    
    async def generate_insights(self, forecast_data):
        """Generate AI insights from forecast data"""
        
        if not self.model:
            return self.get_fallback_insights(forecast_data)
        
        prompt = f"""
        Analyze this energy forecast data and provide insights:
        - Peak load: {forecast_data.get('peak_load', 'N/A')}
        - Average consumption: {forecast_data.get('average_consumption', 'N/A')}
        - Pattern: {forecast_data.get('pattern', 'N/A')}
        
        Provide:
        1. Key observations about energy usage patterns
        2. Potential issues to watch for
        3. Recommendations for optimization
        4. Predicted challenges
        
        Keep response concise and actionable.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self.get_fallback_insights(forecast_data)
    
    async def answer_question(self, forecast_data, question):
        """Answer specific questions about energy data"""
        
        if not self.model or not question:
            return "Please provide a valid question about the energy forecast."
        
        prompt = f"""
        Based on this energy forecast data:
        {json.dumps(forecast_data, default=str)[:500]}
        
        Question: {question}
        
        Provide a clear, concise answer based on the data.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Unable to answer at this time. Error: {str(e)}"
    
    async def explain_forecasting(self):
        """Explain forecasting methods used"""
        
        if not self.model:
            return self.get_method_explanation()
        
        prompt = """
        Explain the differences between LSTM, XGBoost, and ARIMA models for energy load forecasting:
        - When to use each model
        - Their strengths and weaknesses
        - Why ensemble methods work best
        
        Keep it educational but not too technical.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception:
            return self.get_method_explanation()
    
    def get_fallback_insights(self, forecast_data):
        """Fallback insights when Gemini is unavailable"""
        return f"""
        🔍 Key Insights from Your Energy Data:
        
        1. Peak Load Analysis:
           - Peak demand occurs during typical working hours
           - Consider load shifting strategies
        
        2. Efficiency Opportunities:
           - Implement time-of-use pricing
           - Optimize HVAC during peak hours
        
        3. Recommendations:
           - Use LSTM for short-term forecasts (24-48 hours)
           - Use XGBoost for feature-rich predictions
           - Ensemble model gives best overall accuracy
        
        4. Grid Optimization:
           - Balance load across feeders
           - Implement demand response programs
        """
    
    def get_method_explanation(self):
        """Explanation of forecasting methods"""
        return """
        📊 Forecasting Methods Explained:
        
        LSTM (Long Short-Term Memory):
        - Best for: Time series with long-term dependencies
        - Strength: Captures complex patterns
        - Weakness: Requires more data and computation
        
        XGBoost:
        - Best for: When you have many features (temperature, time, holidays)
        - Strength: Fast, handles missing data well
        - Weakness: May miss temporal patterns
        
        ARIMA:
        - Best for: Simple, stable patterns
        - Strength: Interpretable, low computation
        - Weakness: Assumes linear patterns
        
        Ensemble (Best Overall):
        - Combines all three models
        - More robust and accurate
        - Recommended for production use
        """