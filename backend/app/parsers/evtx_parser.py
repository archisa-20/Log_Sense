import Evtx.Evtx as evtx
from xml.etree import ElementTree
from datetime import datetime
from app.models.log_entry import LogEntry

def parse_evtx(file_path):
    logs = []

    with evtx.Evtx(file_path) as log:
        for record in log.records():
            root = ElementTree.fromstring(record.xml())

            event_id = root.find(".//EventID")
            time_created = root.find(".//TimeCreated")

            logs.append(
                LogEntry(
                    timestamp=datetime.fromisoformat(
                        time_created.attrib["SystemTime"].replace("Z", "")
                    ),
                    event_id=int(event_id.text),
                    message=record.xml()
                )
            )

    return logs
