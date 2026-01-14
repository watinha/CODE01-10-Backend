FROM python:3.13.2-alpine3.21

WORKDIR /app

RUN pip install Flask

expose 3000

CMD ["python", "app.py"]
