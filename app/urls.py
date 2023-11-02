from fastapi import APIRouter, FastAPI
from .api.v1.endpoints import health, teams, heroes

def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix="/api/v1")
    v1.include_router(health.router, tags=["Health"])
    v1.include_router(teams.router, tags=["Team"])
    v1.include_router(heroes.router, tags=["Hero"])
    app.include_router(v1)
    return app