from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="Choose Your Own Adventure GAme API", 
    description="api to generate cool stories", 
    version="0.1.0", 
    docs_url="/docs", 
    redoc_url="/redoc"
)

# Have our api's used from a different origin
app.add_middleware(
    CORSMiddleware, 
    allow_origins=settings.ALLOWED_ORIGINS, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# coming to this statement, it tells only execute this statement if we are 
# directly executing this file
if __name__ == "__main__": 
    # uvicorn: webserver, used to server our FastAPI application
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
