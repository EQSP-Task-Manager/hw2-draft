FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /
COPY entrypoint.sh /
COPY accepted-words.txt /

RUN apk add aspell aspell-en
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]