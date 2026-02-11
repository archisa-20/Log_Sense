from datetime import datetime
import uuid
from app.models.security_event import SecurityEvent

FAILED_LOGIN_THRESHOLD = 5

def detect_bruteforce(logs):
    failed = [log for log in logs if log.event_id == 4625]

    if len(failed) >= FAILED_LOGIN_THRESHOLD:
        return SecurityEvent(
            id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            event_type="Auth",
            severity="High",
            title="Possible brute-force login attempt",
            description=f"{len(failed)} failed login attempts detected",
            why_it_matters="Multiple failed logins may indicate an account compromise attempt",
            remediation="Block the IP address and enforce account lockout policies",
            source_ip=failed[0].ip,
            related_logs=[log.message for log in failed]
        )

    return None
