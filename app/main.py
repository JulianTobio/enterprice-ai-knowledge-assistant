from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "Enterprise AI Knowledge Assistant",
    }