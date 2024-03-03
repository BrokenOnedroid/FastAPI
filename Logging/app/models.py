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
    app_name = Column(String, default="unknown")                                # App anme
    ts = Column(DateTime(timezone=True), server_default=func.now())             # timestamp of entry
    ts_last_change = Column(DateTime(timezone=True), server_default=func.now()) # timestamp of entry
    entry = Column(String)                                                      # Log string value
    reviewed = Column(Boolean, default=False)                                   # Entry checked
    review_comment = Column(String)                                             # Comment filed for entrie after check
