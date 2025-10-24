from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/")
async def get_reports():
    # Placeholder summary
    return {"reports": []}
