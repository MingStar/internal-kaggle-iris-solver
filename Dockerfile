FROM python:3.6-alpine3.7 AS runner

RUN pip install pandas sklearn

WORKDIR /app
COPY . /app
CMD ["./entrypoint.sh"]
