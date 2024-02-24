#database table definitionsnow

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

# Base comes of database.py
from app.database import Base
class LogEntry(Base):
    """
    Model for the log_entry table.
    """
    __tablename__ = "log_entry"

    id = Column(Integer, primary_key=True, index=True)                          # id's
    app_id = Column(Integer, ForeignKey("app.id"), default=0)
    ts = Column(DateTime(timezone=True), server_default=func.now())         # timestamp of entry
    ts_last_change = Column(DateTime(timezone=True), server_default=func.now()) # timestamp of entry
    entry = Column(String)                                                      # Log string value
    code = Column(String)                                           # for logging http responses
    reviewed = Column(Boolean, default=False)                                   # Entry checked
    review_comment = Column(String)                                             # Comment filed for entrie after check

class App(Base):
    """
    Model for the apps table.
    """
    __tablename__ = "app"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    name = Column(String)                                                   # App Name     