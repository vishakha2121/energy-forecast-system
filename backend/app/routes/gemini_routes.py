from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gemini_service import GeminiService

router = APIRouter()
gemini_service = GeminiService()

class InsightRequest(BaseModel):
    forecast_data: dict
    question: str = None

@router.post("/insights")
async def get_ai_insights(request: InsightRequest):
    """Get AI-powered insights about energy forecast"""
    try:
        insights = await gemini_service.generate_insights(request.forecast_data)
        return {"insights": insights}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask")
async def ask_question(request: InsightRequest):
    """Ask questions about energy data"""
    try:
        answer = await gemini_service.answer_question(
            request.forecast_data,
            request.question
        )
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/explain-forecast")
async def explain_forecast_method():
    """Get explanation of forecasting methods"""
    explanation = await gemini_service.explain_forecasting()
    return explanation