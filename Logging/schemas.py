# for  Pydantic models that define more or less a "schema" (a valid data shape).
from pydantic import BaseModel

class LogEntryCreate(BaseModel):
    logdb_id: int
    entry: str
    code: str = ""
    app_id: int = 0