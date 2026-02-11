from datetime import datetime
from app.models.log_entry import LogEntry

def parse_txt_logs(content: str):
    logs = []

    for line in content.splitlines():
        if "4625" in line:
            logs.append(LogEntry(
                timestamp=datetime.now(),
                event_id=4625,
                user="Administrator",
                ip="192.168.1.10",
                message=line
            ))

    return logs
