FROM python:3.13.2-alpine3.21

WORKDIR /app

RUN apk add sqlite
RUN pip install Flask Faker

expose 3000

CMD ["python", "app.py"]
