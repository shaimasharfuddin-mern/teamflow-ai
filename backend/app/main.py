from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.teams import router as teams_router

app = FastAPI(
    title="TeamFlow AI API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(teams_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to TeamFlow AI 🚀"
    }