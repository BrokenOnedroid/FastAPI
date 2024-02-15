# Logging APP
Test Project
"Logging" to a DB 
So i can post result of programms into a db to controll them later


# Preperation Steps
1.	python3 -m venv venv
2.	.\venv\Scripts\activate                   
3.	pip install fastapi
4. 	pip install "uvicorn[standard]"
5.	pip install python-multipart sqlalchemy jinja2  (jnja for html tmeplates)

# Running the app
1. uvicorn app:app --reload (updates after code changes)

# Problems


# todo

1. postgre Database?
    1. User Login
    2. different User rights
2. HTML files 
    1. for Entries
    2. for Apps
    3. Filter on homepage
3. Schemas for
    1. App Creation
    2. App Get List
    3. Entry Add func
    4. entry Delete func
5. automatic Database migration after db Changes
6. Changing the function to use the schemas instead of something like "request: Request, **params" IF it is a POST GET does NOT have a Body

# Done
4. Change Database Models just one for the entries without the logbd

# Test
PS 
curl -X 'POST' 'http://127.0.0.1:8000/api/v1/add' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"entry": "string", "code": "string", "app_id": 0 }'
{"EntryCreated":33}


# To Check
the use of -> schemas.LogEntryCreated in func does not reduce the send data
