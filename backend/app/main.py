from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.project_version,
    debug=settings.debug
)


@app.get('/')
async def root():
    return {
        "Message": "Welcome to AI Workforce Platform"
    }


@app.get("/health")
async def health():
    return {
        "status": "Healthy"
    }
