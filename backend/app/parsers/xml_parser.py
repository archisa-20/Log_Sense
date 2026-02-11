from xml.etree import ElementTree
from datetime import datetime
from app.models.log_entry import LogEntry


def parse_xml_logs(file_path: str):
    logs = []

    # Read XML file
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Parse XML content
    root = ElementTree.fromstring(content)

    # Iterate through each Event
    for event in root.findall(".//Event"):
        event_id_elem = event.find(".//EventID")
        time_elem = event.find(".//TimeCreated")

        # Safety checks
        if event_id_elem is None or time_elem is None:
            continue

        try:
            timestamp = datetime.fromisoformat(
                time_elem.attrib["SystemTime"].replace("Z", "")
            )
            event_id = int(event_id_elem.text)
        except Exception:
            continue

        logs.append(
            LogEntry(
                timestamp=timestamp,
                event_id=event_id,
                message=ElementTree.tostring(event, encoding="unicode")
            )
        )

    return logs
