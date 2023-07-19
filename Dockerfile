# syntax=docker/dockerfile:1
FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY bot/requirements.txt /app/
RUN pip install -r requirements.txt
CMD [ "python", "bot.py" ]