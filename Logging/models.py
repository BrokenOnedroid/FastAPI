#database table definitionsnow

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
#func Datetime now
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

# Base comes of database.py
from database import Base

class Logdb(Base):
    """
    Model for the logdb table.
    """
    __tablename__ = "logdb"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    ts = Column(DateTime(timezone=True), server_default=func.now())         # timestamp of entry

    #relationship needed for working cascade delete
    entry = relationship("LogEntry", back_populates="logdb")                # cascade="all,delete" on parent table

class LogEntry(Base):
    """
    Model for the log_entry table.
    """
    __tablename__ = "log_entry"

    id = Column(Integer, primary_key=True, index=True)                          # id's
    logdb_id = Column(Integer, ForeignKey("logdb.id", ondelete="Cascade") )     # to automatically delete the logdb entry
    app_id = Column(Integer, ForeignKey("app.id"), default=0)
    ts_last_change = Column(DateTime(timezone=True), server_default=func.now()) # timestamp of entry
    entry = Column(String, default='No Data')                                                      # Log string value
    code = Column(String, default='')                                           # for logging http responses
    reviewed = Column(Boolean, default=False)                                   # Entry checked
    review_comment = Column(String)                                             # Comment filed for entrie after check

    # relationship
    logdb = relationship("Logdb", back_populates="entry", cascade="all,delete")

class App(Base):
    """
    Model for the apps table.
    """
    __tablename__ = "app"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    name = Column(String)                                                   # App Name     