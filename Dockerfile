FROM python:3.12

WORKDIR /app

COPY . /app

ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
RUN poetry install
RUN apt-get update && apt-get install -y poppler-utils

VOLUME /app/files/output_pngs /app/prompts

ENTRYPOINT ["python"]
CMD ["extract_and_transform.py"]