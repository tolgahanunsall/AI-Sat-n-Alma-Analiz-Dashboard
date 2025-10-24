from fastapi import APIRouter, HTTPException
import pandas as pd
from models.forecast_model import forecast_purchases

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/")
async def forecast(data: list[dict], months_ahead: int = 6):
    try:
        df = pd.DataFrame(data)
        result = forecast_purchases(df, months_ahead=months_ahead)
        return {
            "forecast": result.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
