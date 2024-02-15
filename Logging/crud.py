from sqlalchemy.orm import Session

import models, schemas

#def create_logdb_entry(db: Session):
#  """
#  create Entry in logdb table
#  """
#  new_log = models.Logdb()
#  db.add(new_log)
#  db.commit()
#  db.refresh(new_log)
#  return new_log.id

def create_entry_user(db: Session, log: str):
  """
  create Entry in LogEntry table
  """
  new_entry = models.LogEntry(entry=log)
  db.add(new_entry)
  db.commit()
  db.refresh(new_entry)
  return new_entry.id

def create_entry(db: Session, log: schemas.CreateLogEntry):
  """
  create Entry in LogEntry table
  """
  new_entry = models.LogEntry(entry=log.entry, code=log.code, app_id=log.app_id)
  db.add(new_entry)
  db.commit()
  db.refresh(new_entry)
  return new_entry

def delete_log_entry(db: Session, log_id: int):
  """
  delete Entry in LogEntry table
  """
  log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
  db.delete(log)
  db.commit()

def get_entry_data(db: Session, log_id: int):
  """
  gets all data of one entry
  """    
  log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
  return log


def check_entry_exists(db: Session, log_id: int):
  """
  checks if entry in logEntry exists
  """ 
  log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
  # log is None if the is no Entry
  return log