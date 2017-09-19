# Advertima django REST API
Django web server with REST functionality

## Requirements
You need to have installed such packages:
- docker
- docker-compose

## Build and start project
Go to the project folder and run command: `make init`

## Start and Stop project
- start: `make start`
- stop: `make stop`

## Django admin
Superuser already created.

View admin dashboard here 'http://127.0.0.1:9000'

login: `admin`
password: `superadmin`

## Description
- It is a Django 1.11.5 web application with Django ORM
- Python 3.6
- Database PostgreSQL

All db_data is in a dump file and uploaded to db on `init` step.

Dump was created after running `init_database` script, which uses
`init_data` csv files.

## Check results
Web server runs on localhost: http://127.0.0.1:9000

To check results run, for example,
`http://127.0.0.1:9000/gender-dist/?start=2016-01-01%2012:23:00&end=2016-01-10%2012:20:00&device=1&content=2`

The same for `http://127.0.0.1:9000/viewer-count/?...` and
for `http://127.0.0.1:9000/avg-age/?...`

### Check if result is correct:
Example:

content-device started at '20106-01-01 19:50:00' and ended at '20106-01-01 19:50:30'

Person which disappeared at '20106-01-01 19:50:00' will be included as a viewer of the device-content.

Person which appeared at '20106-01-01 19:50:30' will be included as a viewer of the device-content.

=> In other words I do not include any threshold for the content viewer.
