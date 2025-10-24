from fastapi import APIRouter, UploadFile, HTTPException
import pandas as pd
from services.data_loader import process_excel

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_excel(file: UploadFile):
    try:
        df = pd.read_excel(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid Excel file: {e}")
    summary = process_excel(df)
    return {"status": "ok", "summary": summary}
