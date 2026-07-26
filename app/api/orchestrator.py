from fastapi import APIRouter
from app.services.orchestrator import Orchestrator

router = APIRouter(
    prefix="/orchestrator",
    tags=["Orchestrator"]
)

orchestrator = Orchestrator()


@router.post("/")
def run(request: str):
    return orchestrator.run(request)