#!/bin/bash

# Install dependencies
pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput