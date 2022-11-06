FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY README.md /README.md
COPY main.py /main.py

RUN apk add aspell
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]