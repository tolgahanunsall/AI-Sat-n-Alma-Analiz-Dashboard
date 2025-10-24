from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, forecast, anomalies, reports

app = FastAPI(title="AI Purchase Analysis API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(upload.router)
app.include_router(forecast.router)
app.include_router(anomalies.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {"message": "AI Purchase Dashboard API is running 🚀"}
