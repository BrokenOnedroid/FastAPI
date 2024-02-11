#database table definitions

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
#func Datetime now
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

# Base comes of database.py
from database import Base

class Logdb(Base):
    __tablename__ = "logdb"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    ts = Column(DateTime(timezone=True), server_default=func.now())         # timestamp of entry

class Log_Entry_Data(Base):
    __tablename__ = "log_entry"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    logdb_id = Column(Integer, ForeignKey("logdb.id"))
    #app_id = Column(Integer, ForeignKey("App.id"), default=0)
    app_id = Column(Integer, default=0)
    ts_last_change = Column(DateTime(timezone=True), server_default=func.now())  # timestamp of entry
    entry = Column(String)                                                  # Log string value
    code = Column(String, default='')                                       # for logging http responses
    reviewed = Column(Boolean, default=False)                               # Entry checked
    review_comment = Column(String)                                         # Comment filed for entrie after check

class App(Base):
    __tablename__ = "Apps"

    id = Column(Integer, primary_key=True, index=True)                      # id's
    name = Column(String)                                                   # App Name     