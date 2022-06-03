FROM docker.io/python:3.9 as stage

WORKDIR /tmp

RUN pip install --user pipenv

COPY ./Pipfile ./Pipfile.lock /tmp/

RUN /root/.local/bin/pipenv requirements > /tmp/requirements.txt

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN mkdir /todo
WORKDIR /todo

COPY ./prestart.sh /todo/prestart.sh
COPY --from=stage /tmp/requirements.txt /todo/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /todo/requirements.txt

COPY ./api/*.py /todo/api/

RUN useradd --system --user-group --shell /bin/false --create-home todoapi; \
    chown -R todoapi:todoapi /todo

USER todoapi
