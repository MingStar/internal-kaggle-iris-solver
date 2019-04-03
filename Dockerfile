FROM python:3.7-alpine3.9

WORKDIR /app
CMD ["./entrypoint.sh"]

RUN apk --update add --no-cache g++ openblas-dev

RUN pip install --no-cache-dir numpy==1.16.2
RUN pip install --no-cache-dir scikit-learn==0.20.3
RUN pip install --no-cache-dir pandas==0.24.2


COPY . /app
