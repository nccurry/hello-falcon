FROM python:3

COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080
EXPOSE 8081

ENTRYPOINT ["gunicorn", "-b", "127.0.0.1:8080", "-b", "127.0.0.1:8081", "app:app"]
