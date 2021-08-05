@echo off
if not exist instance (mkdir instance)
cd timetable

if "%1"=="init-db" (
    python -c "from timetable_lib import init_db; init_db()"
) else if "%1"=="web" (
    set FLASK_APP=web
    set FLASK_ENV=development
    flask run
) else if "%1"=="discord" (
    echo ---Run discord front-end---
) else (
    echo Incorrect params
    echo First parameter: init-db, web, discord
    echo e.g. run.bat web
)
