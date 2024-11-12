from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    """Health Check"""

    return {"status": "healthy"}
