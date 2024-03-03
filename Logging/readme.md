# Logging APP

Test Project
"Logging" to a DB

## AIM

Creating a replacement for openmediavault email messages on cron jobs

curl -X 'POST' 'http://127.0.0.1:8000/api/v1/add' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"entry": "log_string" "app_name": "App" }'

Using docker container

Project finished


## Preperation Steps

1. python3 -m venv venv
2. .\venv\Scripts\activate
3. pip install fastapi
4. pip install "uvicorn[standard]"
5. pip install python-multipart sqlalchemy jinja2  (jnja for html tmeplates)

## Running the app

1. uvicorn app:app --reload (updates after code changes)

## Problems

## todo

1. Filter on homepage

## Done

1. Change Database Models just one for the entries without the logbd
2. HTML Changes
    1. Entry.html now shows Entry Data
3. Container https://fastapi.tiangolo.com/deployment/docker/

## Test

PS:
curl -X 'POST' '<http://127.0.0.1:8000/api/v1/add>' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"entry": "string", "code": "string", "app_name": "OMV_PAPERLESS" }'
{"EntryCreated":33}

## Docker

changed folder structur from better overview

https://fastapi.tiangolo.com/deployment/docker/

Created https://fastapi.tiangolo.com/deployment/docker/ && requirements.txt

get info for Version via pip list --local/ freez in local directory

to create image
docker build --platform=linux/arm64  -t fastapi-app .

to run image
docker run -p 8080:80 fastapi-app

push to to docker.io
- login per cli
- get imageId per cli: docker images
- tag the image with something e.g. latest-arm64: docker tag imageId dockerhubRepoName:tagForBuildVersion
- push to docker repo: docker push dockerhubRepoName:tagForBuildVersion

if there is data in the db it will be part of the container...

# How to use

1. Build docker Image and Import this with e.g. Portainier.
2. Use commands like sudo docker exec paperless document_exporter ../export -z && curl -X 'POST' 'http://127.0.0.1:8000/api/v1/add/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "entry": "string", "code": "string", "app_name": "unknown" }'
3. check page for entries