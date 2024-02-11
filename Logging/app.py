import logging
from fastapi import FastAPI, Depends, Request, Form, status
from pydantic import BaseModel

# ASGI Framework
from starlette.responses import RedirectResponse, Response
from starlette.templating import Jinja2Templates

#local folder for html tmplate files
templates = Jinja2Templates(directory="templates")

# for usage of the db && model declartions
from sqlalchemy.orm import Session

# local .py 
import crud, models, schemas
from database import SessionLocal, engine

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# creating the db tabels
models.Base.metadata.create_all(bind=engine)

class EntryCreated(BaseModel):
  id: int

# FastAPI "instance"
app = FastAPI()

# helper function to access database session
# dependency for the home function 
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
     

#homepage function
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
  logs = db.query(models.Logdb).all()
  return templates.TemplateResponse("base.html", {"request": request, "log_list": logs})

@app.post("/add")
def add(request: Request, log_entry: str = Form(...), db: Session= Depends(get_db)) -> EntryCreated:
  # Create a new item
  entry_id = crud.create_logdb_entry(db)
  data_id = crud.create_entry(db, logdb_id=entry_id, new_entry=log_entry, new_code= "", app_id= 0)
  return Response(status_code=status.HTTP_201_CREATED, media_type='Entry added: {data_id}')



# @app.post("/add")
# def add(request: Request, log: schemas.LogEntryCreate, log_entry: str = Form(...), db: Session= Depends(get_db)) -> EntryCreated:
#   # Create a new item
#   entry_id = crud.create_logdb_entry(db)
#   data_id = crud.create_logdb_entry(db, log, entry_id, log_entry)
#   return Response(status_code=status.HTTP_201_CREATED, media_type='Entry added: {data_id}')


# update existing todo entry
# inverse log_reviewed entry 
@app.put("/update/{log_id}") 
def update(request: Request, log_id: int, db: Session = Depends(get_db)):
  log = db.query(models.Logdb).filter(models.Logdb.id == log_id).first()
  # reseting boolean of db model
  log.log_reviewed = not log.log_reviewed
  db.commit()

  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


# delte route
@app.get("/delte/{log_id}")
def delte(request: Request, log_id: int, db: Session = Depends(get_db)):
  log = db.query(models.Logdb).filter(models.Logdb.id == log_id).first()
  db.delete(log)
  db.commit()

  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

# Enable debug mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
