FROM python:3.10-alpine

WORKDIR /opt/action/

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY entrypoint.sh .

RUN apk add aspell
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]