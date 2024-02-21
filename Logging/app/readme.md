# Logging APP

Test Project
"Logging" to a DB

## AIM

Creating a replacement for openmediavault email messages

curl -X 'POST' 'http://127.0.0.1:8000/api/v1/add' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"entry": "$(sudo docker cp dockerid:/usr/src/paperless/export -)" "app_id": 1 }'


Using docker

## Preperation Steps

1. python3 -m venv venv
2. cd app       Cause i using vscode with open folder Logging
2. .\venv\Scripts\activate
3. pip install fastapi
4. pip install "uvicorn[standard]"
5. pip install python-multipart sqlalchemy jinja2  (jnja for html tmeplates)

## Running the app

1. uvicorn app:app --reload (updates after code changes)

## Problems

## todo

1. Database Changes (not needed for what i want to do)
    1. User Login ??
    2. different User rights ??
    3. postgre ??
2. HTML files
    1. for Apps
    2. Filter on homepage
3. Schemas for
    1. App Creation
    2. App Get List
    3. Entry Add func
    4. entry Delete func
4. automatic Database migration after db Changes
5. Changing the function to use the schemas instead of something like "request: Request, **params" IF it is a POST GET does NOT have a Body
6. Container https://fastapi.tiangolo.com/deployment/docker/

## Done

1. Change Database Models just one for the entries without the logbd
2. HTML Changes
    1. Entry.html now shows Entry Data

## Test

PS:
curl -X 'POST' '<http://127.0.0.1:8000/api/v1/add>' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"entry": "string", "code": "string", "app_id": 0 }'
{"EntryCreated":33}

## To Check

the use of -> schemas.LogEntryCreated in func does not reduce the send data

## Docker

changed folder structur because of the instructions of folleoing link

see https://fastapi.tiangolo.com/deployment/docker/

Created https://fastapi.tiangolo.com/deployment/docker/ && requirements.txt

get info for Version via pip list --local in local directory