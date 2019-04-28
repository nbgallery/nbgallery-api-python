FROM ubuntu:latest
MAINTAINER Matt Kafonek "kafonek@gmail.com"

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3-pip python3-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY app /app
WORKDIR /app

RUN pip3 install -r requirements.txt -q

ENTRYPOINT ["python3"]
CMD ["app.py"]
