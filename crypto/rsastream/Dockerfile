FROM python:3-alpine

RUN apk --update add socat && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache

COPY app /app
ENTRYPOINT socat tcp-l:1234,reuseaddr,fork exec:/app/script.py
EXPOSE 1234
