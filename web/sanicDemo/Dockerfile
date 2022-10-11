FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

VOLUME [ "/data" ]
EXPOSE 8000
CMD ["python", "-u", "-m", "weiguan.api.app"]