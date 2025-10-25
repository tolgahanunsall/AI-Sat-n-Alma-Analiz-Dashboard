from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routerlar
from routes import upload, forecast, anomalies, reports

app = FastAPI(title="AI Purchase Analysis API")

# CORS ayarları - Vite frontend'i için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API rotaları
app.include_router(upload.router)
app.include_router(forecast.router)
app.include_router(anomalies.router)
app.include_router(reports.router)
