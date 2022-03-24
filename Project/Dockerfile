FROM python:3.8

WORKDIR /Users/aleks/Innow

RUN pip install Django==4.0.3 djangorestframework==3.13.1 \
    Pillow==9.0.1 djoser==2.1.0 \
    djangorestframework-simplejwt==4.8.0 celery==5.2.3 flower==1.0.0 \
    redis==4.1.4 psycopg2==2.9.3 && \
    rm -rf /var/lib/apt/lists/*

COPY . /Users/aleks/Innow

# EXPOSE 8000

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]