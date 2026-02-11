from fastapi import APIRouter
from app.store.memory import security_events

router = APIRouter()

@router.get("/events")
def get_events():
    return security_events
