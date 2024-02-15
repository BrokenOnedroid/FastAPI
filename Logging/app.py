import logging
from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from pydantic import BaseModel

# ASGI Framework
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.templating import Jinja2Templates

#Jspon Return for schemas.LogEntyData
from fastapi.encoders import jsonable_encoder

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
     
##################################################################################################################################################################
#    API FUNCTIONS
##################################################################################################################################################################    
@app.post("/api/v1/add")
# async def add(request: Request, log_entry: str = Form(...), db: Session= Depends(get_db)) -> schemas.LogEntryCreate:
async def add(log_entry :schemas.CreateLogEntry, db: Session= Depends(get_db)) -> schemas.LogEntryCreated:
  """
  Creating new Item API Endpoint
  based on schmea for request

  """
  response_data = crud.create_entry(db=db, log=log_entry)
  response_data = {"EntryCreated": response_data.id}
  return JSONResponse(status_code=status.HTTP_201_CREATED, media_type='application/json', content=jsonable_encoder(response_data))

@app.get("/api/v1/entry/{log_id}") 
def entry_data(request: Request, log_id: int, db: Session = Depends(get_db)) -> schemas.LogEntryData:
  """
  gets all data of 1 Entry 
  """
  response_data = crud.get_entry_data(db=db, log_id=log_id)

  if response_data is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{log_id} not found")  
  
  return JSONResponse(status_code=status.HTTP_302_FOUND, media_type='application/json', content=jsonable_encoder(response_data))

# delete route API
# Works with e.g. curl -X DELETE http://127.0.0.1:8000/api/v1/delete/1
@app.delete("/api/v1/delete/{log_id}")
def delte(request: Request, log_id: int, db: Session = Depends(get_db)) -> schemas.LogEntryDelete:
  """
  delting log entry
  checking befor if entry even exits
  """
  log = crud.check_entry_exists(db=db, log_id=log_id)

  if log is None:
    raise HTTPException(status_code=404, detail="{log_id} not found")
  
  crud.delete_log_entry(db=db, log_id=log_id)
  return JSONResponse(content={"deleted": True}, status_code=status.HTTP_202_ACCEPTED)


##################################################################################################################################################################
#    UI FUNCTIONS
##################################################################################################################################################################    

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
  """
  homepage function gets all entries

  todo add a macx amount and pages
  """
  logs = db.query(models.LogEntry).all()
  return templates.TemplateResponse("base.html", {"request": request, "log_list": logs})

@app.post("/add")
def add(request: Request, log_entry: str = Form(...), db: Session= Depends(get_db)) -> schemas.LogEntryCreated:
  """
  Adding per html fomrular
  """
  # Create a new item
  data = crud.create_entry_user(db=db, log=log_entry)
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND )


# deleting work still need to understand the relationship in models
@app.get("/delete/{log_id}")
def delte(request: Request, log_id: int, db: Session = Depends(get_db)):
  """
  delting log entry
  checking befor if entry even exits
  """
  log = crud.check_entry_exists(db=db, log_id=log_id)
  if log is None:
    url = app.url_path_for("home")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log entry not found")

  crud.delete_log_entry(db=db, log_id=log_id) 
  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.put("/update/{log_id}") 
def update(request: Request, log_id: int, db: Session = Depends(get_db)):
  """
  update with html interface
  """  
  log = db.query(models.LogEntry).filter(models.LogEntry.id == log_id).first()
  # reseting boolean of db model
  #log.log_reviewed = not log.log_reviewed
  db.commit()

  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


# Enable debug mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
