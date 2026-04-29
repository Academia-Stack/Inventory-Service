from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import uuid

@dataclass
class LogEntry:
    logId: str
    message: str
    endPoint: str
    method: str
    exceptionClass: str
    timestamp: str

    @staticmethod
    def create(message, endpoint, method, exception_class):
        return LogEntry(
            logId=str(uuid.uuid4()),
            message=message,
            endPoint=endpoint,
            method=method,
            exceptionClass=exception_class,
            timestamp=datetime.now(timezone.utc).isoformat()
        )

    def to_dict(self):
        return asdict(self)