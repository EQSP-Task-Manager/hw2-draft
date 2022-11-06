FROM alpine:3.16

WORKDIR /opt/action/

COPY main.py .
COPY entrypoint.sh .

RUN apk add aspell
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]