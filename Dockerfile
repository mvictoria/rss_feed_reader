FROM python:3.10 AS builder 

WORKDIR /tmp

COPY ./pyproject.toml ./poetry.lock /tmp/

RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# ----------------------------------

FROM python:3.10

WORKDIR /code

COPY --from=builder /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./rss_feed_reader /code/rss_feed_reader

EXPOSE 80

CMD ["uvicorn", "rss_feed_reader.main:app", "--host=0.0.0.0", "--port=80"]
