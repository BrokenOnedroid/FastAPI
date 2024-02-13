from datetime import date, datetime, time, timedelta

# for  Pydantic models that define more or less a "schema" (a valid data shape).
from pydantic import BaseModel

class LogEntryCreate(BaseModel):
    logdb_id: int
    entry: str
    code: str = ""
    app_id: int = 0

class LogEntry(BaseModel):
    logdb_id: int

class LogEntryDelete(BaseModel):
    logdb_id: int

class LogData(BaseModel):
    id: int 
    logdb_id: int
    app_id: int
    ts_last_change: datetime = None         # cause i could be empty
    entry: str              
    code: str
    reviewed: bool
    review_comment: str
