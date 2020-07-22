# setup

## Create virtual environment
- `virtualenv .venv`
- `source .venv/bin/activate`

## Install Requirements
`pip install requirements.txt`

## create `.env` file (example) within `learn` directory
```
DEBUG = True
SECRET_KEY = '<secret_key>'
ALLOWED_HOSTS=.localhost, 127.0.0.1

```
 ## run
 - `python manage.py migrate`
 - `python manage.py runserver`
