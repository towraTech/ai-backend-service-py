from fastapi import FastAPI

app = FastAPI(
    title="TowraTech AI Backend",
    description="AI Video Creation API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to TowraTech AI Backend!"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }