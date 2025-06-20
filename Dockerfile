FROM python:3.11.9-slim

WORKDIR /code

COPY .env /code/.env

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]
