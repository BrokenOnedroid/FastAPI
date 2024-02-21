from datetime import date, datetime, time, timedelta

# for  Pydantic models 
# Optional setting in Model
from typing import Optional

# for  Pydantic models that define more or less a "schema" (a valid data shape).

from pydantic import BaseModel, StrictStr

class CreateLogEntry(BaseModel):
    entry: StrictStr 
    code: Optional[str] = None
    app_id: Optional[int] = 0

class LogEntryCreated(BaseModel):
    log_id: int
    entry: str
    code: str = ""
    app_id: int = 0

class LogEntry(BaseModel):
    log_id: int

class LogEntryDelete(BaseModel):
    log_id: int

class LogEntryData(BaseModel):
    id: int 
    app_id: int
    ts_last_change: datetime = None         # cause i could be empty
    entry: str              
    code: str
    reviewed: bool
    review_comment: str

# Comments and Thoughts
# ConfigDict so number can be used in string for e.g. api call 
# https://stackoverflow.com/questions/77220728/pydantic-accept-integer-as-string-input
#    model_config = ConfigDict(coerce_numbers_to_str=True, strict=False)    
