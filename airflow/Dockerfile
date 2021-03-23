##################################################
# Local development environment.
##################################################
FROM python:3.8-slim as development

ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW_LOG_DIR=/var/log/airflow
ENV AIRFLOW_DB_URL=sqlite:////tmp/sqlite.airflow.db
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR ${AIRFLOW_HOME}

COPY . .

RUN set -x \
 && pip install -U pip setuptools poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

##################################################
# Production environment.
##################################################
FROM python:3.8-slim as production

ARG OWNER=airflow

ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW_LOG_DIR=/var/log/airflow
ENV AIRFLOW_DB_URL=sqlite:////tmp/sqlite.airflow.db

COPY --from=development /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=development /usr/local/bin/airflow /usr/local/bin/airflow
COPY --from=development /usr/local/bin/celery /usr/local/bin/celery
COPY --from=development /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR ${AIRFLOW_HOME}

RUN set -x \
 && useradd -r -s /bin/false ${OWNER} \
 && mkdir -p ${AIRFLOW_LOG_DIR} \
 && chown -R ${OWNER} ${AIRFLOW_LOG_DIR}

COPY airflow.cfg .
COPY dags .
COPY plugins .
COPY webserver_config.py .

USER ${OWNER}
EXPOSE 8080
