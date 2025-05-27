FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir Flask flask-cors Flask-MySQLdb Flask-SQLAlchemy

EXPOSE 4000

CMD ["python", "run.py"]
