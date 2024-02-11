import logging
from fastapi import FastAPI, Depends, Request, Form, status

# ASGI Framework
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

#local folder for html tmplate files
templates = Jinja2Templates(directory="templates")

# for usage of the db && model declartions
from sqlalchemy.orm import Session

import models
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
     

#homepage function
@app.get("/")
# function declartion and definition
# request is arguments
# db is a session object
def home(request: Request, db: Session = Depends(get_db)):
  todos = db.query(models.Todo).all()
  
  for todo in todos:
    logging.debug(f"Entry with title: {todo.title}")

  return templates.TemplateResponse("base.html", {"request": request, "todo_list": todos})

@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session= Depends(get_db)):
  # Log request data
  logging.debug(f"Received POST request to add todo item with title: {title}")

  # Create a new todo item
  new_todo = models.Todo(title=title)
  db.add(new_todo)
  db.commit()

  # redirecting to homepage
  # staus need because change von post to get route
  # app.url_path_for("home") get the inforamtion fpr homepage form def home
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


# update existing todo entry
@app.get("/update/{todo_id}") #why not put?
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
  todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
  # reseting boolean of db model
  todo.complete = not todo.complete
  db.commit()

  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

# delte route
@app.get("/delte/{todo_id}")
def delte(request: Request, todo_id: int, db: Session = Depends(get_db)):
  todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
  db.delete(todo)
  db.commit()

  # redirecting to homepage
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

# Enable debug mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)


# basic functions
""" basic Home-Route
@app.get("/")
def home():
    return {"Hello": "World"}

# get for an item or simmila depending on setting in {} eg. {item_id}
# automatic type checking against item_id: int
@app.get("/items/{item_id}")
def read_item(item_id: int):
  return{"item_id": item_id}
"""  