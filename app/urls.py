from fastapi import APIRouter, FastAPI
from .api.v1.endpoints import health

def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix="/api/v1")
    v1.include_router(health.router, tags=["Health"])
    app.include_router(v1)
    return app