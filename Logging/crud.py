from sqlalchemy.orm import Session

import models, schemas

def create_logdb_entry(db: Session):
  new_log = models.Logdb()
  db.add(new_log)
  db.commit()
  db.refresh(new_log)
  return new_log.id

def create_entry(db: Session, log: schemas.LogEntryCreate):
# def create_entry(db: Session, new_entry: str, new_code: str, logdb_id: int, app_id: int):
  new_entry = models.Log_Entry_Data(logdb_id=log.logdb_id, entry=log.entry, code=log.code, app_id=log.app_id)
  db.add(new_entry)
  db.commit()
  db.refresh(new_entry)
  return new_entry.id
