FROM python:3.7-alpine3.9

RUN apk --update add --no-cache g++ openblas-dev

RUN pip install --no-cache-dir scikit-learn==0.20.3
RUN pip install --no-cache-dir pandas==0.24.2

WORKDIR /app
COPY . /app
CMD ["./entrypoint.sh"]
