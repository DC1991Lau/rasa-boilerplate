FROM python:3.9-slim AS builder

RUN apt-get update && apt-get install -y gcc && apt-get install -y --no-install-recommends \
   libpq-dev \
   curl \
   uuid \
   poppler-utils \
   && rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Lisbon
ENV VIRTUAL_ENV=/opt/venv

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD requirements.txt requirements.txt

RUN /opt/venv/bin/python -m  pip install --upgrade pip && \
    /opt/venv/bin/python -m  pip install --no-cache-dir -r requirements.txt && \
    find /opt/venv \
        \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' \;


FROM python:3.9-slim AS nlpapi
COPY --from=builder /opt/venv /opt/venv

RUN apt-get update && apt-get install -y --no-install-recommends \
   libtesseract-dev \
   libleptonica-dev \
   tesseract-ocr \
   tesseract-ocr-por \
   poppler-utils \
 && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:$PATH"

ADD ./app /usr/app

CMD ["bash", "-c", "python3 /usr/app/main.py"]