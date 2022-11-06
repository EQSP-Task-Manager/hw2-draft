FROM python:3.10-alpine

WORKDIR /opt/action/

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY entrypoint.sh .

RUN apk add aspell
RUN chmod a+x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]