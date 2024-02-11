# for  Pydantic models that define more or less a "schema" (a valid data shape).
from pydantic import BaseModel

class LogBase(BaseModel):
    id: int

class LogEntryCreate(LogBase):
    logdb_id: int