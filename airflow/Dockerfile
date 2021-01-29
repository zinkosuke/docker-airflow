FROM python:3.8-slim

ARG OWNER=airflow

ENV PYTHONDONTWRITEBYTECODE=1
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW_LOG_DIR=/var/log/airflow
ENV AIRFLOW_DB_URL=sqlite:////tmp/sqlite.airflow.db

WORKDIR ${AIRFLOW_HOME}

COPY . .

RUN set -x \
 && groupadd -g 1000 ${OWNER} \
 && useradd -u 1000 -g 1000 -m -s /bin/bash ${OWNER} \
 && chown ${OWNER}:${OWNER} ${AIRFLOW_HOME} \
 && mkdir -p ${AIRFLOW_LOG_DIR} \
 && chown -R ${OWNER}:${OWNER} ${AIRFLOW_LOG_DIR} \
 && pip install -U pip setuptools poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

USER ${OWNER}
EXPOSE 8080
