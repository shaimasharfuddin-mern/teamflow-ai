from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.teams import router as teams_router
from app.routers.projects import router as projects_router
from app.routers.tasks import router as tasks_router
from app.routers.analytics import router as analytics_router
from app.routers.dashboard import router as dashboard_router


app = FastAPI(
    title="TeamFlow AI API",
    version="1.0.0"
)

# --------------------------
# CORS CONFIGURATION
# --------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# ROUTERS
# --------------------------
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(teams_router)
app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(analytics_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {"message": "TeamFlow AI 🚀"}