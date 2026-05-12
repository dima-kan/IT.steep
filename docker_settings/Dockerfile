
FROM python:3.14-slim

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt


ENV MIN_NUM=0

CMD ["python", "-u", "main.py"]
