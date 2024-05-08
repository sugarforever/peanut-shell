FROM python:3.11 as python-base

RUN mkdir app
WORKDIR  /app
COPY /pyproject.toml /poetry.lock /app/

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
