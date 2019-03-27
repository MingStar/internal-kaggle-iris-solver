FROM python:3.6-alpine3.7 AS runner

WORKDIR /app
COPY . /app
CMD ["./entrypoint.sh"]
