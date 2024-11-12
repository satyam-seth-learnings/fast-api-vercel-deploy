from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

app = FastAPI()

class Settings(BaseSettings):
    """App Settings"""

    allowed_hostname: str

    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()

@app.get("/")
async def health_check():
    """Health Check"""

    return {"status": "healthy", "allowed_hostname": settings.allowed_hostname}
