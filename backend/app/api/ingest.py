from fastapi import APIRouter, UploadFile
from app.parsers.txt_parser import parse_txt_logs
from app.detectors.brute_force import detect_bruteforce
from app.parsers.evtx_parser import parse_evtx
from app.store.memory import parsed_logs, security_events

router = APIRouter()

from app.parsers.router import parse_logs

@router.post("/logs/upload")
async def upload_logs(file: UploadFile):
    logs = parse_logs(file)
    parsed_logs.extend(logs)

    event = detect_bruteforce(logs)
    if event:
        security_events.append(event)

    return {"message": "Logs processed successfully"}
