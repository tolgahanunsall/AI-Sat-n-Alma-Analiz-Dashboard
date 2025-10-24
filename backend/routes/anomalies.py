from fastapi import APIRouter

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

@router.get("/")
async def list_anomalies():
    # Placeholder: return empty list for now
    return {"anomalies": []}
