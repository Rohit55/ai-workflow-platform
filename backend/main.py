from fastapi import FastAPI

app = FastAPI(
    title="AI-Workforce-Platform",
    version="1.0.0"
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
