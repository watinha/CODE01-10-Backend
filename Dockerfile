FROM python:3.13.2-alpine3.21

WORKDIR /app

RUN apk add sqlite
RUN pip install Flask Faker flask-cors \
      Flask-JWT-Extended pydantic flask_pydantic \
      Flask_Caching bleach flask_limiter bcrypt \
      django fastapi[standard] aiosqlite

expose 3000

CMD ["python", "app.py"]
