FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

EXPOSE 8000

CMD ["python", "main.py"]
